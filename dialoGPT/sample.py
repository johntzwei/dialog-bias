from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelWithLMHead, AutoTokenizer

import os
import torch
import argparse
from tqdm import tqdm

def chunks(my_list, n=64):
    return [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]

def main(args):
    # load model and tokenizer
    print('Loading model...')
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelWithLMHead.from_pretrained(args.model)

    # gpu
    model.to('cuda')
    print('Done.')

    print('Reading prompts...')
    prompts = [ i.split('\t') for i in open(args.prompts, 'rt') ]
    prompts.sort(key=lambda x: len(x[1]))

    labels = [ p[0] for p in prompts ]
    tensors = [ torch.LongTensor(tokenizer.encode(p[1])).to('cuda') for p in prompts ]

    num_examples = len(prompts) * args.batches
    print('(%d prompts) * (%d batches) *  = %d examples' % (len(prompts), args.batches, num_examples))

    print('Sampling parameters: (do_sample=%s, num_beams=%s, max_length=%s, top_p=%s, top_k=%s, temperature=%s)' %
            (str(args.do_sample), str(args.num_beams), str(args.maxlen), str(args.topp), str(args.topk), str(args.temperature)))
    fh = open(os.path.join(args.sample_dir, args.name), 'wt')

    tensor_chunks = chunks(tensors)
    label_chunks = chunks(labels)

    # generate
    for i in tqdm(range(0, args.batches)):
        for label_chunk, tensor_chunk in tqdm(zip(label_chunks, tensor_chunks), total=len(tensor_chunks)):

            padded = torch.nn.utils.rnn.pad_sequence([torch.flip(i, [0]) for i in tensor_chunk], batch_first=True)
            padded = torch.flip(padded, [1])
            mask = (padded != 0.0).float()

            generations = model.generate(padded,
                    attention_mask=mask,
                    bos_token_id=None,  # only works for gpt2 styled models
                    pad_token_id=50256,
                    do_sample=args.do_sample, 
                    num_beams=args.num_beams,
                    max_length=args.maxlen,
                    top_p=args.topp, 
                    top_k=args.topk, 
                    temperature=args.temperature,
                )

            for label, line in zip(label_chunk, tokenizer.batch_decode(generations.tolist())):
                line = line.replace('\n','')
                fh.write('%s\t%s\n' % (label, line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
            "--model",
            default="microsoft/DialoGPT-medium",
            type=str,
            )

    parser.add_argument(
            "--prompts",
            default="demographics.txt",
            type=str,
            )

    parser.add_argument(
            "--sample_dir",
            default="samples/",
            type=str,
            )

    parser.add_argument(
            "--name",
            default="samples.txt",
            type=str,
            )

    parser.add_argument(
            "--batches",
            default=10,
            type=int,
            )

    parser.add_argument(
            "--batch_size",
            default=10,
            type=int,
            )

    # -----
    # sampling arguments
    # -----
    parser.add_argument(
            "--maxlen",
            default=50,
            type=int,
            )

    parser.add_argument(
            "--do_sample",
            default=False,
            action='store_true',
            )

    parser.add_argument(
            "--num_beams",
            default=None,
            type=int,
            )

    parser.add_argument(
            "--topp",
            default=None,
            type=float,
            )

    parser.add_argument(
            "--topk",
            default=None,
            type=int,
            )

    parser.add_argument(
            "--temperature",
            default=None,
            type=float,
            )

    args = parser.parse_args()

    main(args)
