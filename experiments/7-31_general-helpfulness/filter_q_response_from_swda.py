import os
from os import path

valid_questions = ['qw', 'qo']

with open(path.join(os.environ['DIALOG_BIAS_ROOT'], 'Switchboard-Corpus/swda_data/full_set.txt'), 'rt') as fh:
    question = None
    for line in fh:

        if any(line.strip().endswith('|%s' % i) for i in valid_questions):
            question = line.strip()
            continue

        if question is not None:
            if question[0] != line[0]:  # turn changes in speaker
                print('%s\t%s' % (question, line.strip()))
            question = None
