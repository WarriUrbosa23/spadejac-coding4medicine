import gffutils
from Bio import SeqIO
from Bio.Seq import Seq


def main(): 
    chr12 = list(SeqIO.parse("/share/Human/chr12.fa", "fasta"))
    #print(type(chr12[0]))
    w = (chr12[0][111803961])
    if w == 'G':
        print("Normal")
        return 0
    elif w == 'A':
        print("Asian Flush")
        return 0
    else:
        print("??")
        return 1
    chr12 = chr12[0].seq
    #print(type(chr12))
    #print(chr12[13])
    chr = chr12[0].split('\n')
    #print(chr)

main()