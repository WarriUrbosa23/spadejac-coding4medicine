import gffutils
from Bio import SeqIO
from Bio.Seq import Seq

def main():
    global things
    ecoli = list(SeqIO.parse("/home/spadejac/main-folder/ecoli.aln", "fasta"))
    ecoli_seq = ecoli[0].seq
    things = {"dnaA": '', 
              "rpmH": ''}
    with open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.gff") as gff:
        for line in gff:
            if line.startswith("#"):
                continue  # Skip comments
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue  # Skip incomplete lines
            feature_type = fields[2]
            if feature_type == "gene":
                #print(fields[8], "\n")
                important = fields[8].split(';')
                #print(f)
                #print(f[2])
                nameEquals = important[2].split('=')
                name = nameEquals[1]
                #print(name)
                start = int(fields[3]) - 1  # GFF is 1-based, Python is 0-based
                end = int(fields[4])
                strand = fields[6]
                attributes = fields[8]
                seq = ecoli_seq[start:end]  
                
                if name in things:
                    print("e")
                    if fields[6] == '+':    
                        translated = seq.translate()
                        things[name]= translated
                    elif fields[6] == '-':
                        revc = seq.reverse_complement()
                        translated = revc.translate()
                        things[name] = translated
                    #print(fields)
                #    print(seq, "\n"
    print(things["rpmH"])
main()