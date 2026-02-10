#Can you check the sequence for all 4 nucleotide word and print the locations for all 4-nucleotide palindromes?

#(Let us say dna[4:8] is a palindrome and so is dna[15:19]. Your answer will be 4, 15.)
def main():
    palindromes = []
    Full = input("Provide a sequence: ")
    for w in range(0, len(Full)-3):
      #  print(w)
        reversed = reverse(Full[w:w+4])
     #   print(Full[w:w+4])
    #    print(reversed, "r")
   #     print(" ")
        if reversed == Full[w:w+4]:
            palindromes.append(w)
    print(', '.join(map(str, palindromes)))
    #print(''.join(palindromes))

    

def reverse(Sequence):
    counts = {"A": "T", "T": "A", "C": "G", "G": "C"}
    Sequence = list(Sequence)
 #   print(Sequence, "original")
    for i in range(0, len(Sequence), 1):
        Sequence[i] = counts[Sequence[i]]
#        print(Sequence, "flipping")
    Sequence = Sequence[::-1]
    Sequence = ''.join(Sequence)
  #  print(Sequence, "s")
    return(Sequence)

main()
