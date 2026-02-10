import gffutils
from Bio import SeqIO
from Bio.Seq import Seq



def main():
    ALDH2 = open("/home/spadejac/main-folder/ALDH2Investigation/aldh2.aln")
    ALDH2 = ALDH2.readlines()
    final = ""
    for i in range(1, len(ALDH2)):
        final += ALDH2[i].rstrip('\n')
    ALDH2 = str(final)
    #print(ALDH2)
    ALDH2 = Seq(ALDH2).translate()
    ALDH2 = ALDH2.rstrip('*')
    print(ALDH2, "\n")
    other = open("/home/spadejac/main-folder/ALDH2Investigation/uniprotALDH2.aln")
    other = other.readlines()
    eee = ""
    for i in range(1, len(other)):
        eee += other[i].rstrip('\n')
    other = str(eee)
    print(other, "\n")
    if ALDH2 != other:
        print("Not equal")
    else:
        print("Same")
        return 0

main()