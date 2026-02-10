#Use your translation code to translate the SARS coronavirus genome in three reading frames. Find all proteins longer than 100 amino acids and tell me how many.

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}
def main():
    f=open("/share/SARS-class/SARS-2020.fasta")
    lines=f.readlines()
    #print(lines)
    final = ""
    for i in range(1, len(lines)):
        final += lines[i].rstrip('\n')
    lines = str(final)
    proteins = proteinsfunc()
    finallist = []
    for i in range(0, len(proteins)):
        if (len(proteins[i]) > 100):
            for w in range(0, len(lines)):
                x = lines[w:len(proteins[i])]
                if x == proteins[i]:
                    finallist.append(w)
    # #last = ', '.join(finallist)
    #print(proteins)
    print(finallist)
    print(len(finallist))
    print(len(proteins[3]))



def translate(dna):
    final = []
    triplets = [dna[i:i+3] for i in range(1, len(dna)-2, 3)]
    for i in range(0, len(triplets), 1):
        final += gencode[triplets[i]]
    final = ''.join(final)
    #print(final)
    return(final)

def proteinsfunc():
    f=open("/share/SARS-class/SARS-2020.fasta")
    lines=f.readlines()
    final = ""
    for i in range(1, len(lines)):
	    final += lines[i].rstrip('\n')
    lines = str(final)
    #print(len(lines))
    lines = translate(lines)
    lines = lines.split("*")
    return(lines)

main()