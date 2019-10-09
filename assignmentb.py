from itertools import permutations as permute
import numpy as np
seq1 = 'TGGTATATTAGGCCGAATCCT T AAGT AAAAACT GGTA'
seq2 = 'TGT T AT AT T AGGCCGAAT CCT T AAGT AAAAACAGGTT'
seq3 = 'TGT T AT AT GAGGCCGAAT CCT T CAGT AAT AACT GGTT'
seq4 = 'TGT T AT AT GCGGCCGAAT CCT T CAGT AAAAACT CGT T'
"""seq5 = 'AGT T AT AT GCGGCCGAAT CCAT CAGT AAAAACT CGT A'"""



seq1 = 'TGGGTCTG'
seq2 = 'TGGCTCTG'
seq3 = 'CATGCTGG'
seq4 = 'CATGCTTA'
"""
#seq1 = seq1.replace(" ","")
#seq2 = seq2.replace(" ","")
#seq3 = seq3.replace(" ","")
#seq4 = seq4.replace(" ","")
#seq5 = seq5.replace(" ","")
"""
def countdiffs(seqa,seqb):
	n = len([i for i, j in zip(seqa, seqb) if i != j ])
	return n
"""
#seqs = [seq1,seq2,seq3,seq4,seq5]
"""
seqs = [seq1,seq2,seq3,seq4]
diffs = []

for i in range(0,len(seqs)):
	for j in range(0,len(seqs)):
		diffs.append(countdiffs(seqs[i],seqs[j]))


diffs = np.array(diffs)
diffs = np.reshape(diffs, (-len(seqs),len(seqs)))
print(diffs)

print(np.where(diffs == np.min(np.ma.masked_equal(diffs, 0, copy= False))))
print(np.min(np.ma.masked_equal(diffs, 0, copy= False)))

def jukeCantor(seqa, seqb):
	ndiff = len([i for i, j in zip(seqa, seqb) if i != j ])
	p = ndiff/float(len(seqa))
	k = (-3/4)*np.log10(1-(4/3)*p)
	return k 

diffs = []
for i in range(0,len(seqs)):
	for j in range(0,len(seqs)):
		diffs.append(jukeCantor(seqs[i],seqs[j]))


diffs = np.array(diffs)
diffs = np.reshape(diffs, (-len(seqs),len(seqs)))

print(diffs)

