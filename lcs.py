def best_value(p, q):
    largest = 0
    for x in [p, q]:
        if len(x) >= largest:
            largest = len(x)
            best = x
    return best

def lcs(s, t, D):
    for _ in range(len(s) + 1):
        D.append([""] * (len(t) + 1))
    for j in range(len(t)-1, -1, -1):
        for i in range(len(s)-1, -1, -1):
            if s[i] == t[j]:
                D[i][j] = s[i] + D[i+1][j+1]
            else:
                D[i][j] = best_value(D[i+1][j], D[i][j+1])
    return D[0][0]

s = "AAGTAACTTGGCATACCGTTT"
t = "AAGATATAGCTTATTTGC"

matrix = []

print(lcs(s, t, matrix))