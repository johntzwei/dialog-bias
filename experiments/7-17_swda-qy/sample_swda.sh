python ./filter_qy_response_from_swda.py > all_qy_responses.tsv
cat all_qy_responses.tsv | \
    shuf | \
    head -100 > sampled.tsv

cat sampled.tsv | \
    sed 's/|/\t/g' | \
    cut -f2 > sampled_justq.txt
