from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

my_dna = input("what is the DNA sequence ")

#counting the DNA sequence

dna_lenght = len(my_dna) 
print ("The lenght of the DNA sequence is: " + "\n" + str(dna_lenght))

# Takes the DNA sequence and print the lower case version of it. 
my_dna_lc = my_dna.lower()
print ("The DNA sequence in lower case is: " + "\n" + my_dna_lc)

#Takes de DNA sequence and print the upper case version of it. 

my_dna_uc = my_dna.upper()
print ("The DNA sequence in UPPER case is: " + "\n" + my_dna_uc)

#Reverse compliment of the sequence

replace1 = my_dna.replace("A","t")
replace2 = replace1.replace("T","a")
replace3 = replace2.replace("C","g")
replace4 = replace3.replace("G","c")

rev_comp = replace4[::-1]
dna_revcomp = rev_comp

print ("The reverse complement of the sequence is: " + dna_revcomp + " 'or' " + dna_revcomp.upper())

#Calculting GC content using Biopython tools. 

#if gc_input == True
gc_content = GC(my_dna)

print ("The GC content of the sequence is: %f", gc_content)