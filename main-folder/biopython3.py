import gffutils
from Bio import SeqIO
from Bio.Seq import Seq

def main():
    global accCecoli
    global coaEecoli
    global dnaKecoli
    global rpsGecoli
    global yqeKecoli
    global accCstrep
    global coaEstrep
    global dnaKstrep
    global rpsGstrep
    global yqeKstrep
    ecoli = list(SeqIO.parse("/home/spadejac/main-folder/ecoli.aln", "fasta"))
    ecoli_seq = ecoli[0].seq
    strep = list(SeqIO.parse("/home/spadejac/main-folder/strep.aln", "fasta"))
    strep_seq = strep[0].seq
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
                f = fields[8].split(';')
                #print(f)
                #print(f[2])
                w = f[2].split('=')
                name = w[1]
                #print(name)
                start = int(fields[3]) - 1  # GFF is 1-based, Python is 0-based
                end = int(fields[4])
                strand = fields[6]
                attributes = fields[8]
                seq = ecoli_seq[start:end]  
                if name == "coaE":
                    coaEecoli = seq
                    #print(fields)
                #    print(seq, "\n")
                elif name == "accC":
                    accCecoli = seq
                    #print(fields)
                #    print(seq, "\n")
                elif name == "dnaK":
                    dnaKecoli = seq
                    #print(fields)
                #    print(seq, "\n")
                elif name == "rpsG":
                    rpsGecoli = seq
                    #print(fields)
                #    print(seq, "\n")
                elif name == "yqeK":
                    yqeKecoli = seq
                    #print(fields)
                #    print(seq, "\n")
    with open("/share/Streptococcus/GCF_030020365.1_ASM3002036v1_genomic.gff") as gff:
        for line in gff:
            if line.startswith("#"):
                continue  # Skip comments
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue  # Skip incomplete lines
            feature_type = fields[2]
            if feature_type == "gene":
                #print(fields[8], "\n")
                f = fields[8].split(';')
                #print(f)
                #print(f[1])
                w = f[1].split('=')
                name = w[1]
                #print(name)
                start = int(fields[3]) - 1  # GFF is 1-based, Python is 0-based
                end = int(fields[4])
                strand = fields[6]
                attributes = fields[8]
                seq = strep_seq[start:end]  
                if name == "coaE":
                    coaEstrep = seq
                    #print(fields)
                #    print(seq, "\n")
                elif name == "accC":
                    accCstrep = seq
                    #print(fields)
                #    print(seq, "\n")
                elif name == "dnaK":
                    dnaKstrep = seq
                    #print(fields)
                #    print(seq, "\n")
                elif name == "rpsG":
                    rpsGstrep = seq
                    #print(fields)
                elif name == "yqeK":
                    yqeKstrep = seq
                    #print(fields)
                   # print(seq, "\n")
                   # print(seq, "\n")
    print("There is a difference of", difference(accCecoli, accCstrep), "nucleotides between the accC proteins.")
    print("There is a difference of", difference(coaEecoli, coaEstrep), "nucleotides between the coaE proteins.")
    print("There is a difference of", difference(dnaKecoli, dnaKstrep), "nucleotides between the dnaK proteins.")
    print("There is a difference of", difference(rpsGecoli, rpsGstrep), "nucleotides between the rpsG proteins.")
    print("There is a difference of", difference(yqeKecoli, yqeKstrep), "nucleotides between the yqeK proteins.")
    #print("There is a difference of", difference(accCecoli.translate(), accCstrep.translate()), "codons between the accC proteins.")
    #print("There is a difference of", difference(coaEecoli.translate(), coaEstrep.translate()), "codons between the coaE proteins.")
    #print("There is a difference of", difference(dnaKecoli.translate(), dnaKstrep.translate()), "codons between the dnaK proteins.")
    #print("There is a difference of", difference(rpsGecoli.translate(), rpsGstrep.translate()), "codons between the rpsG proteins.")
    #print("There is a difference of", difference(yqeKecoli.translate(), yqeKstrep.translate()), "codons between the yqeK proteins.")

def difference(ecoli, strep):
    lastlististg = []
    diff = 0
    #print(len(ecoli), len(strep))

    #Moving Padding to the end of the shorter sequence
    if len(ecoli) > len(strep):
        for x in range(0, len(ecoli) - len(strep)):
            strep += " "
            print(len(strep))
    if len(ecoli) < len(strep):
        for x in range(0, len(strep) - len(ecoli)):
            ecoli += " "

    for eeeee in range(0, len(ecoli)):
        #print(len(accCecoli))    
        #print(len(accCecoli), len(accCstrep))
        if ecoli[eeeee] != strep[eeeee]:
            string = (eeeee, ecoli[eeeee], strep[eeeee])
            lastlististg.append(string)
            diff+=1
    
    print(ecoli, '\n')
    print(strep, "\n")
    print(lastlististg)
    return diff


main()