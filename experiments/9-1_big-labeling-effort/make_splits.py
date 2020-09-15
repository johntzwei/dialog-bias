import csv
import random

fh = open('./big_annotation.tsv', 'rt')
annotations = list(fh)[1:]
annotations = [ i.strip().split('\t') for i in annotations ]

random.seed(1)
random.shuffle(annotations)
print(annotations[0])

header = ['index', 'text', 'label']
writer = csv.writer(open('train.csv', 'wt'))
writer.writerow(header)
[ writer.writerow((i, '[CLS] %s [SEP] %s [SEP]' % (tsv[1], tsv[2]), tsv[3])) 
        for i, tsv in enumerate(annotations[0:500]) ]

writer = csv.writer(open('val.csv', 'wt'))
writer.writerow(header)
[ writer.writerow((i, '[CLS] %s [SEP] %s [SEP]' % (tsv[1], tsv[2]), tsv[3])) 
        for i, tsv in enumerate(annotations[500:700]) ]

writer = csv.writer(open('test.csv', 'wt'))
writer.writerow(header)
[ writer.writerow((i, '[CLS] %s [SEP] %s [SEP]' % (tsv[1], tsv[2]), tsv[3])) 
        for i, tsv in enumerate(annotations[700:1000]) ]
