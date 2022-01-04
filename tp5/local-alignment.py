import numpy as np
import itertools as it

def matrix(m, n, match_score, gap_penalty):
    D = np.zeros((len(m) + 1, len(n) + 1), np.int)
    for i, j in it.product(range(1, D.shape[0]), range(1, D.shape[1])):
        match = D[i-1, j-1] + (match_score if m[i-1] == n[j-1] else -match_score)
        delete = D[i - 1, j] - gap_penalty
        insert = D[i, j - 1] - gap_penalty
        D[i, j] = max(match, delete, insert, 0)
    return D

def traceback(D, n, n_='', old_i=0):
    flipD = np.flip(np.flip(D, 0), 1)
    i_, j_ = np.unravel_index(flipD.argmax(), flipD.shape)
    i, j = np.subtract(D.shape, (i_ + 1, j_ + 1))
    if D[i, j] == 0:
        return n_, j
    n_ = n[j - 1] + '-' + n_ if old_i - i > 1 else n[j - 1] + n_
    return traceback(D[0:i, 0:j], n, n_, i)

def smith_waterman(m, n, match_score, gap_penalty):
    m, n = m.upper(), n.upper()
    D = matrix(m, n, match_score, gap_penalty)
    n_, pos = traceback(D, n)
    return pos, pos + len(n_)

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

alignment = smith_waterman(sequences[0], sequences[1], match_score=3, gap_penalty=2)
print(sequences[1][alignment[0]: alignment[1]+1])