from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelWithLMHead, AutoTokenizer

import os
import torch
import argparse

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
    prompts = [ (p[0], torch.LongTensor(tokenizer.encode(p[1])).to('cuda')) for p in prompts ]
    num_examples = len(prompts) * args.batch_size * args.batches
    print('(%d prompts) * (%d batch size) * (%d batches) = %d examples' % (len(prompts), args.batch_size, args.batches, num_examples))

    name = 'sample_%s_topp_%.2f_maxlen_%d.txt' % (args.sample, args.topp, args.maxlen)
    fh = open(os.path.join(args.sample_dir, name), 'wt')
    fh2 = open(os.path.join(args.sample_dir, 'labels.txt'), 'wt')

    # generate
    for label, prompt in prompts:
        for i in range(0, args.batches):
            generations = model.generate(prompt.unsqueeze(0).repeat(args.batch_size, 1),
                    bos_token_id=None,  # only works for gpt2 styled models
                    do_sample=args.sample, 
                    max_length=args.maxlen,
                    top_p=args.topp, 
                    top_k=args.topk, 
                    temperature=args.temperature,
                )

            for line in tokenizer.batch_decode(generations.tolist()):
                line = line.replace('\n','')
                fh.write(line + '\n')

                fh2.write(label + '\n')

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
            default=True,
            action='store_true',
            )

    parser.add_argument(
            "--topp",
            default=0.99,
            type=float,
            )

    parser.add_argument(
            "--topk",
            default=0,
            type=int,
            )

    parser.add_argument(
            "--temperature",
            default=0,
            type=float,
            )

    args = parser.parse_args()

    main(args)
