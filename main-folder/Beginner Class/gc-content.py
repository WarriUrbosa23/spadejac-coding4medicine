f=open("/share/SARS-class/RaTG13.fasta")
lines=f.readlines()
key = {"A": 0, "T": 0, "C": 0, "G": 0}
final = []
#print(lines, "\n")
for i in range(1, len(lines)):
	final += lines[i].rstrip('\n')
for i in range(0, len(final)):
    key[final[i]] += 1
print(key["G"], key["C"])
first = key["G"]+key["C"]
finish = 100*(first/len(final))
print(finish, "%, or approximately ", round(finish), "%.", sep='')
