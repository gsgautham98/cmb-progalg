import numpy as np

# ----- Verification code ----- #
#from Levenshtein import distance
#distances_lev = []
#distances_lev.append([distance(sequences[i], sequences[j]) for j in range(len(sequences))])

def edit_distance(s, t):
    D = []
    for _ in range(len(s)+1):
        D.append([0]*(len(t)+1))
    for i in range(len(s)+1):
        D[i][0] = i
    for j in range(len(t)+1):
        D[0][j] = j
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            hor_dist = D[i][j-1] + 1
            ver_dist = D[i-1][j] + 1
            if s[i-1] == t[j-1]:
                diag_dist = D[i-1][j-1]
            else:
                diag_dist = D[i-1][j-1] + 1
            D[i][j] = min(hor_dist, ver_dist, diag_dist)
    return D[-1][-1]

def hamming_distance(s, t):
    if len(s) == len(t):
        dist = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                dist += 1
        return dist
    return "not possible"

sequences = ['ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC',
'GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA',
'TTTTCCGTCGGATTTGCTATAGCCCCTGAACGCTACATGCACGAAACCAC',
'AGTTATGTATGCACGTCATCAATAGGACATAGCCTTGTAGTTAACAG',
'TGTAGCCCGGCCGTACAGTAGAGCCTTCACCGGCATTCTGTTTG',
'ATTAAGTTATTTCTATTACAGCAAAACGATCATATGCAGATCCGCAGTGCGCT',
'GGTAGAGACACGTCCACCTAAAAAAGTGA',
'ATGATTATCATGAGTGCCCGGCTGCTCTGTAATAGGGACCCGTTATGGTCGTGTTCGATCAGAGCGCTCTA',
'TACGAGCAGTCGTATGCTTTCTCGAATTCCGTGCGGTTAAGCGTGACAGA',
'TCCCAGTGCACAAAACGTGATGGCAGTCCATGCGATCATACGCAAT',
'GGTCTCCAGACACCGGCGCACCAGTTTTCACGCCGAAAGCATC',
'AGAAGGATAACGAGGAGCACAAATGAGAGTGTTTGAACTGGACCTGTAGTTTCTCTG',
'ACGAAGAAACCCACCTTGAGCTGTTGCGTTGTTGCGCTGCCTAGATGCAGTGG',
'TAACTGCGCCAAAACGTCTTCCAATCCCCTTATCCAATTTAACTCACCGC',
'AATTCTTACAATTTAGACCCTAATATCACATCATTAGACACTAATTGCCT',
'TCTGCCAAAATTCTGTCCACAAGCGTTTTAGTTCGCCCCAGTAAAGTTGT',
'TCAATAACGACCACCAAATCCGCATGTTACGGGACTTCTTATTAATTCTA',
'TTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGGTGGTATGGA']

output = input("Write output to file? (y/n) ")
if output.strip() in "yY":
    mode = True
else:
    mode = False

distances = []
for i in range(len(sequences)):
    distances.append([edit_distance(sequences[i], sequences[j]) for j in range(len(sequences))])
if mode:
    with open("distances", "w") as handle:
        for i in range(len(distances)):
            for j in range(len(distances)):
                handle.write(str(distances[i][j]) + " ")
            handle.write("\n")
else:
    print(np.array(distances))

