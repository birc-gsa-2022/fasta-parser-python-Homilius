import sys
import numpy as np

def get_subseqs():

    try:
        inFile_1 = sys.argv[1]
        inFile_2 = sys.argv[2]

        with open(inFile_1,'r') as f1:
            f1_lines = f1.readlines()
        with open(inFile_2,'r') as f2:
            f2_lines = f2.readlines()

        record_list = []
        header = ''
        sequence = ''
        interval = []
        for line in f1_lines:
            line = line.strip()
            if line.startswith('>'):
                if header != "":
                    record_list.append([header.strip(), sequence.strip()])
                    sequence = ""
                header = line[1:]
            else:
                sequence = sequence + line
        record_list.append([header.strip(), sequence.strip()])
        record_list = np.array(record_list)

        for line in f2_lines:
            chrom = line.split()[0]
            start = int(line.split()[1])
            end = int(line.split()[2])
            find_seqs = np.where(np.array(record_list) == chrom)
            seq = record_list[find_seqs[0]][0][1]
            print(seq[start-1:end-1])
            
    except:
        inFile_1 = sys.argv[1]
        inFile_2 = sys.stdin

        with open(inFile_1,'r') as f1:
            f1_lines = f1.readlines()
        f2_lines = inFile_2.readlines()

        record_list = []
        header = ''
        sequence = ''
        interval = []
        for line in f1_lines:
            line = line.strip()
            if line.startswith('>'):
                if header != "":
                    record_list.append([header.strip(), sequence.strip()])
                    sequence = ""
                header = line[1:]
            else:
                sequence = sequence + line
        record_list.append([header.strip(), sequence.strip()])
        record_list = np.array(record_list)

        for line in f2_lines:
            chrom = line.split()[0]
            start = int(line.split()[1])
            end = int(line.split()[2])
            find_seqs = np.where(np.array(record_list) == chrom)
            seq = record_list[find_seqs[0]][0][1]
            print(seq[start-1:end-1]) 

    return ''
get_subseqs()
