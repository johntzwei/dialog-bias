DIALOG_BIAS_ROOT=/nas/home/jwei/biases/dialog-bias/

csv_file=random_women

cat $DIALOG_BIAS_ROOT/experiments/8-21_help-pipeline_on_gendered-questions/$csv_file.csv | \
    sed 's/$/<|endoftext|>/' > $DIALOG_BIAS_ROOT/experiments/8-21_help-pipeline_on_gendered-questions/prompts.txt

CUDA_VISIBLE_DEVICES=0 python $DIALOG_BIAS_ROOT/dialoGPT/sample.py \
    --model microsoft/DialoGPT-medium \
    --prompts $DIALOG_BIAS_ROOT/experiments/8-21_help-pipeline_on_gendered-questions/prompts.txt \
    --sample_dir $DIALOG_BIAS_ROOT/experiments/8-21_help-pipeline_on_gendered-questions \
    --name vanilla_sample_$csv_file.csv \
    --batches 10 \
    --maxlen 200 \
    --batch_size 64 \
    --do_sample
