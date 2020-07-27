cat $DIALOG_BIAS_ROOT/experiments/7-17_swda-qy/sampled_justq.txt | \
    sed 's/^/0\t/' | \
    sed 's/$/<|endoftext|>/' > $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples/prompts.txt

CUDA_VISIBLE_DEVICES=0 python $DIALOG_BIAS_ROOT/dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples/prompts.txt \
    --sample_dir $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples \
    --name vanilla_sampling.txt \
    --batches 1 \
    --batch_size 1 \
    --do_sample

CUDA_VISIBLE_DEVICES=0 python $DIALOG_BIAS_ROOT/dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples/prompts.txt \
    --sample_dir $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples \
    --name beams_10.txt \
    --batches 1 \
    --batch_size 1 \
    --num_beams 10

CUDA_VISIBLE_DEVICES=0 python $DIALOG_BIAS_ROOT/dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples/prompts.txt \
    --sample_dir $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples \
    --name topk_10.txt \
    --batches 1 \
    --batch_size 1 \
    --do_sample \
    --topk 10

CUDA_VISIBLE_DEVICES=0 python $DIALOG_BIAS_ROOT/dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples/prompts.txt \
    --sample_dir $DIALOG_BIAS_ROOT/experiments/7-17_dialoGPT-samples \
    --name topp_9e-1.txt \
    --batches 1 \
    --batch_size 1 \
    --do_sample \
    --topp 0.9
