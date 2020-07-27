import os
from os import path

STRICTER = True
pronouns = [ 'this', 'that', 'he', 'him', 'her', 'she', 'they', 'them', 'it' ]

with open(path.join(os.environ['DIALOG_BIAS_ROOT'], 'Switchboard-Corpus/swda_data/full_set.txt'), 'rt') as fh:
    question = None
    for line in fh:
        if line.strip().endswith('?|qy'):
            if STRICTER and any(i in line.lower() for i in pronouns):
                continue

            if STRICTER and len(line.strip().split(' ')) < 3:
                continue

            question = line.strip()
            continue

        if question is not None:
            if question[0] != line[0]:  # turn changes in speaker
                print('%s\t%s' % (question, line.strip()))
            question = None
