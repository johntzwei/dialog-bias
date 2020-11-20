CUDA_VISIBLE_DEVICES=3 python ../../dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts ./questions_5000_MW.tsv \
    --sample_dir ./ \
    --name top_k_10_temp_1.txt \
    --topk 10 \
    --temperature 1 \
    --batches 3 \
    --batch_size 64 \
    --do_sample

CUDA_VISIBLE_DEVICES=3 python ../../dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts ./questions_5000_MW.tsv \
    --sample_dir ./ \
    --name top_k_10_temp_0.7.txt \
    --topk 10 \
    --temperature 0.7 \
    --batches 3 \
    --batch_size 64 \
    --do_sample
