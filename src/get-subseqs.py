import sys
import numpy as np

def get_subseqs():

    f1_lines = open(sys.argv[1]).readlines()
    f2_lines = (sys.stdin if len(sys.argv) < 3 else open(sys.argv[2])).readlines()

    record_list = []
    header = ''
    sequence = []
    for line in f1_lines:
        line = line.strip()
        if line.startswith('>'):
            if header != "":
                record_list.append([header.strip(), ''.join(sequence).strip()])
                sequence = []
            header = line[1:]
        else:
            sequence.append(line)
    record_list.append([header.strip(), ''.join(sequence).strip()])
    record_list = np.array(record_list)

    for line in f2_lines:
        chrom = line.split()[0]
        start = int(line.split()[1])
        end = int(line.split()[2])
        find_seqs = np.where(record_list == chrom)
        seq = record_list[find_seqs[0]][0][1]
        print(seq[start-1:end-1])

    return ''
get_subseqs()