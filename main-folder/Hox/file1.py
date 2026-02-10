import gffutils
from Bio import SeqIO
from Bio.Seq import Seq


def main():
    global hox_genes
    global fruitfly
    fruitfly = list(SeqIO.parse("/share/Hox/GCF_000001215.4_Release_6_plus_ISO1_MT_protein.faa", "fasta"))
    #print(len(fruitfly))
    #print(type(fruitfly[0]))
    print(fruitfly[0])
    #print(fly_seq)
    with open("/share/Hox/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.gff") as gff:
        for line in gff:
            if line.startswith("#"):
                continue  # Skip comments
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue  # Skip incomplete lines
            feature_type = fields[2]
            if feature_type == "CDS":
                #print(fields)
                #print(fields[8], "\n")
                geneInformation = fields[8].split(';')
                #print(geneInformation)
                #print(geneInformation[2])
                for i in range(0, len(geneInformation)):
                    if "gene=" in geneInformation[i]:
                        nameEquals = geneInformation[i]
                #print(nameEquals)
                nameEquals = nameEquals.split('=')
                name = nameEquals[1]
                #print(name) #string
                start = int(fields[3]) - 1  # GFF is 1-based, Python is 0-based
                end = int(fields[4])
                strand = fields[6]
                attributes = fields[8]
                #seq = fly_seq[start:end]
                hox_genes = {
                    "lab": '',
                    "pb": '',
                    "Dfd": '',
                    "Scr": '',
                    "Antp": '',
                    "Ubx": '',
                    "abd-A": '',
                    "Abd-B": ''}
                if name in hox_genes:
                    #print(name)
                    for z in range(0, len(geneInformation)): 
                        if "protein_id=" in geneInformation[z]:
                            proteinid = geneInformation[z].split('=')
                            proteinid = proteinid[1]
                            for o in range(0, len(fruitfly)):
                                if proteinid in fruitfly[o]:
                                    print(fruitfly[o])
                        #    print(proteinid) 
                    #print(fields, "\n")
                    #print(seq)
                    #hox_genes[name] = seq
                    #print(hox_genes)
    print(hox_genes["pb"])
main()    