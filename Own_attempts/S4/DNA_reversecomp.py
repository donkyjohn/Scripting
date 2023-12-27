def reverse_complement(dna_seq):
    dna_seq = dna_seq.upper()
    dna_seq = dna_seq.replace('A', 't')
    dna_seq = dna_seq.replace('T', 'a')
    dna_seq = dna_seq.replace('G', 'c')
    dna_seq = dna_seq.replace('C', 'g')
    dna_seq = dna_seq.upper()
    dna_seq = dna_seq[::-1]
    return dna_seq