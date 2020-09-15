CUDA_VISIBLE_DEVICES=1 python $DIALOG_BIAS_ROOT/dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts $DIALOG_BIAS_ROOT/experiments/7-31_general-helpfulness/just_q.txt \
    --sample_dir $DIALOG_BIAS_ROOT/experiments/7-31_general-helpfulness \
    --name topp_9e-1.txt \
    --batches 1 \
    --batch_size 1 \
    --do_sample \
    --topp 0.9
