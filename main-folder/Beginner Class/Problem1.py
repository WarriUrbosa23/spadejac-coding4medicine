f=open("small-genome")
lines=f.readlines()
final = []
#print(lines, "\n")
for i in range(1, len(lines)):
	final += lines[i].rstrip('\n')
final = ''.join(final)
print(len(final))