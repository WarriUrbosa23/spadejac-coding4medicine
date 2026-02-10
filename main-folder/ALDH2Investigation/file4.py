import gffutils
from Bio import SeqIO
from Bio.Seq import Seq


def main():
    file_object = open("/home/spadejac/main-folder/ALDH2Investigation/extra.txt", "w")
    ALDH2 = open("/home/spadejac/main-folder/ALDH2Investigation/aldh2.aln")
    ALDH2 = ALDH2.readlines()
    final = ""
    for i in range(1, len(ALDH2)):
        final += ALDH2[i].rstrip('\n')
    ALDH2 = str(final)
    orig = Seq(ALDH2).translate()
    #print(ALDH2[1509])
    ALDH2 = list(ALDH2)
    ALDH2[1509] = 'A'
    ALDH2 = ''.join(ALDH2)
    file_object.write(ALDH2)
    file_object.close()
    #print(ALDH2[1509])
    flush = Seq(ALDH2).translate()
    print(len(flush))
    
    for i in range(0, len(flush)):
        if flush[i] != orig[i]:
            print("The difference is at", i+1, "where the original is", orig[i], "and the flush is", flush[i])
    #chr12 = list(SeqIO.parse("/share/Human/chr12.fa", "fasta"))
    #chr12 = chr12[0].translate()
    #print(chr)

main()