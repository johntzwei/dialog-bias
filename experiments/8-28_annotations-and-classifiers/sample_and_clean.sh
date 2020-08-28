cat vanilla_sample_random_equal_t1.csv | grep '^M' | shuf | head -300 > men_responses.csv
cat vanilla_sample_random_equal_t1.csv | grep '^W' | shuf | head -300 > women_responses.csv

cat men_responses.csv | sed 's/!//g' | sed 's/<|endoftext|>/\t/g' | cut -d=   -f1,2,3 > clean_men_responses.tsv
cat women_responses.csv | sed 's/!//g' | sed 's/<|endoftext|>/\t/g' | cut -d=    -f1,2,3 > clean_women_responses.tsv
