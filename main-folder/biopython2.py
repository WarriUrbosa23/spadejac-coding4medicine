import gffutils
from Bio import SeqIO
from Bio.Seq import Seq

#Can you combine the e.coli genome and gff to find the protein-coding genes? 
def main():
    # gff = open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.gff")
    # gff = gff.readlines()
    # #print(gff)
    genome = list(SeqIO.parse("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna", "fasta"))
    genome_seq = genome[0].seq
    # print(type(gff))
    # for e in range(223, 224):
    #     print(gff[e])
    #     gff[e].split('\t')
    #     print(gff[e])
    final = []


    with open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.gff") as gff:
        for line in gff:
            if line.startswith("#"):
                continue  # Skip comments
            fields = line.strip().split('\t')
            #print(fields, "\n")
            if len(fields) < 9:
                continue  # Skip incomplete lines
            feature_type = fields[2]
            if feature_type == "CDS":
                start = int(fields[3]) - 1  # GFF is 1-based, Python is 0-based
                end = int(fields[4])
                strand = fields[6]
                attributes = fields[8]
                seq = genome_seq[start:end]
                if strand == "-":
                    seq = seq.reverse_complement()
                    final.append(start)
                    seq2 = seq.translate()
                    #print(seq2, "\n")
                    #print(f"CDS: {attributes}\nSequence: {seq}\n")
                elif strand == "+":
                    seq2 = seq.translate()
                    start_pos = t.find(seq2)
                    #print(seq2, "\n")
                #print(fields[8], "\n")
                
    #print(gff[111])
    #print(final)
    #print(genome)

main()