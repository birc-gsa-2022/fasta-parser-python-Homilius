#!/usr/bin/python3

import sys

def read_fasta():
    # load input:
    inFile = sys.argv[1]  # The list of command line arguments. e.g sys.argv[0] is the script name itself.
    with open(inFile,'r') as j:
        lines = j.readlines()
    
    # make fasta parser:
    record_list = []
    header = ''
    sequence = ''
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if header != "":
                record_list.append([header, sequence])
                sequence = ""
            header = line[1:]
        else:
            sequence = sequence + line
    record_list.append([header, sequence])

    # clean output:
    for i in record_list:
        #print('> ' + i[0].strip() + '\t' + i[1]) 
        print(i[0].strip() + '\t' + i[1]) 
    
    return ''
read_fasta()
