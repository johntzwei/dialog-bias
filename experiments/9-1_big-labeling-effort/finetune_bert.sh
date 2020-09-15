CUDA_VISIBLE_DEVICES=2 python train.py ./ ./ ./output/
CUDA_VISIBLE_DEVICES=2 python test.py ./output ./test.csv ./predictions.txt
