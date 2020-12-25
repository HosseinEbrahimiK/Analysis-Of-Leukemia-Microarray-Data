import math

if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/rosalind_ba3c.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))
    input_file.close()

    m = len(inp_txt[0][0])
    n = len(inp_txt[1][0])
    k = len(inp_txt[2][0])
    seq1 = inp_txt[0][0]
    seq2 = inp_txt[1][0]
    seq3 = inp_txt[2][0]

    table = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(k+1)]
    parent_table = [[[(0, 0, 0) for _ in range(n+1)] for _ in range(m+1)]for _ in range(k+1)]

    for i in range(1, k+1):

        for j in range(1, m+1):

            for t in range(1, n+1):
                score = [-math.inf] * 7
                ind = [(0, 0, 0)] * 7

                if seq1[j-1] == seq2[t-1] == seq3[i-1]:
                    score[0] = 1 + table[i-1][j-1][t-1]
                    ind[0] = (i-1, j-1, t-1)

                for r in range(i):
                    if table[r][j][t] > score[1]:
                        score[1] = table[r][j][t]
                        ind[1] = (r, j, t)

                for r in range(j):
                    if table[i][r][t] > score[2]:
                        score[2] = table[i][r][t]
                        ind[2] = (i, r, t)

                for r in range(t):
                    if table[i][j][r] > score[3]:
                        score[3] = table[i][j][r]
                        ind[3] = (i, j, r)

                for r in range(i):
                    for s in range(j):
                        if table[r][s][t] > score[4]:
                            score[4] = table[r][s][t]
                            ind[4] = (r, s, t)

                for r in range(i):
                    for s in range(t):
                        if table[r][j][s] > score[5]:
                            score[5] = table[r][j][s]
                            ind[5] = (r, j, s)

                for r in range(j):
                    for s in range(t):
                        if table[i][r][s] > score[6]:
                            score[6] = table[i][r][s]
                            ind[6] = (i, r, s)

                table[i][j][t] = max(score)
                parent_table[i][j][t] = ind[score.index(max(score))]

    cur = (k, m, n)
    align_seq = [""] * 3
    p = [k-1, m-1, n-1]
    seq = [seq3, seq1, seq2]
    path = []

    while cur != (0, 0, 0):

        path.append(cur)
        cur = parent_table[cur[0]][cur[1]][cur[2]]
    path.append((0, 0, 0))

    for i in range(len(path)-1):
        dif = [path[i][j] - path[i+1][j] for j in range(3)]
        maximum = max(dif)
        for j in range(3):
            for _ in range(dif[j]):
                align_seq[j] = seq[j][p[j]] + align_seq[j]
                p[j] -= 1
            for _ in range(maximum - dif[j]):
                align_seq[j] = '-' + align_seq[j]

    print(table[k][m][n])
    print(align_seq[1])
    print(align_seq[2])
    print(align_seq[0])
