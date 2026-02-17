f = open("whale.aln")
lines=f.readlines()

whales=["","",""]
for i in range(0, 3):
	for j in range(10*i+1,10*i+9):
		whales[i] += lines[j].rstrip('\n')
print("beluga\n",whales[0],"\ndolphin\n",whales[1],"\norca\n",whales[2])
