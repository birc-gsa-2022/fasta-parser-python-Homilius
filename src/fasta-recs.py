import sys

def read_fasta():
    # load input:
    inFile = sys.argv[1]
    with open(inFile,'r') as f:
        lines = f.readlines()
    
    # make fasta parser:
    record_list = []
    header = ''
    sequence = []
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if header != "":
                record_list.append([header.strip(), ''.join(sequence).strip()])
                sequence = []
            header = line[1:]
        else:
            sequence.append(line)
    record_list.append([header.strip(), ''.join(sequence).strip()])

    # clean output:
    for i in record_list:
        #print('> ' + i[0].strip() + '\t' + i[1]) 
        print(i[0].strip() + '\t' + i[1]) 
    
    return ''
read_fasta()


