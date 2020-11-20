CUDA_VISIBLE_DEVICES=0 python ../../dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts ./qy_M.csv \
    --sample_dir ./ \
    --name top_k_10_temp_1.txt \
    --topk 10 \
    --temperature 1 \
    --batches 3 \
    --batch_size 64 \
    --do_sample

CUDA_VISIBLE_DEVICES=0 python ../../dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts ./qy_M.csv \
    --sample_dir ./ \
    --name top_k_10_temp_0.7.txt \
    --topk 10 \
    --temperature 0.7 \
    --batches 3 \
    --batch_size 64 \
    --do_sample
