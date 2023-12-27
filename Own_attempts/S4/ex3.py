#ibin/python3

dna_seq = input("\nEnter DNA sequence: ")

def check_dna(dna_seq):
    nucA = 0
    nucT = 0
    nucG = 0
    nucC = 0

    for base in dna_seq:
        if base == 'A':
            nucA += 1
        elif base == 'T':
            nucT += 1
        elif base == 'G':
            nucG += 1
        elif base == 'C':
            nucC += 1
        else:
            print("Please provide a nucleotide sequence")

    conclusion = {'A': nucA, 'T': nucT, 'G': nucG, 'C': nucC}
    print("\nBase counts: ")
    print(conclusion)

    seqlen = len(dna_seq)
    nucAfreq = nucA/seqlen
    nucTfreq = nucT/seqlen
    nucGfreq = nucG/seqlen
    nucCfreq = nucC/seqlen

    conclusion2 = {'A': nucAfreq, 'T': nucTfreq, 'G': nucGfreq, 'C': nucCfreq}
    print("\nBase frequencies: ")
    print(conclusion2)

check_dna(dna_seq)
