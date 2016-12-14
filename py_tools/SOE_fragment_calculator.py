
# coding: utf-8

# In[6]:

#from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
#from Bio.SeqUtils import GC


# In[7]:

#getting user input on what are the sequences to be joined

seq_1 = input("What is the 1st sequence to be joined?")
seq_2 = input("What is the 2nd sequence to be joined?")


# In[8]:

seq1_len = len(seq_1)
seq2_len = len(seq_2)


# In[9]:

if seq1_len > seq2_len:
    base_seq = seq_1
    short_seq = seq_2
    out_write = "Add 100 nanograms of fragment 1 to the reaction"
    out_write2 = "For fragment 2, add: "
elif seq2_len > seq1_len:
    base_seq = seq_2
    short_seq = seq_1
    out_write = "Add 100 nanograms of fragment 2 to the reaction"
    out_write2 = "For fragment 1, add: "

base_mw = len(base_seq)*660
short_mw = len(short_seq)*660


# In[10]:

#calculate the nanograms to match at the molar level the longest fragment, default for long fragment is 100 nanograms
base_pmols = ((100/10**9)/(base_mw))*(10**12)
nanograms_short = (base_pmols/(10**12))*(short_mw)*(10**9)


# In[14]:

print(out_write)
print (out_write2 + str(nanograms_short) + " nanograms")


# In[ ]:



