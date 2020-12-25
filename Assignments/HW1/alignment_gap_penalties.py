from BLOSUM62 import get_score
import math

if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/dataset_206211_3.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))
    input_file.close()

    m, n, seq1, seq2 = len(inp_txt[0][0]), len(inp_txt[1][0]), inp_txt[0][0], inp_txt[1][0]
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    parent_table = [[(0, 0) for _ in range(n+1)] for _ in range(m+1)]

    opening_penalty, extension_penalty = -11, -1

    for i in range(1, m+1):

        for j in range(1, n+1):

            max_row, max_col = -math.inf, -math.inf
            index = list()
            maxes = list()
            ind = (0, 0)
            for k in range(j):
                s = table[i][k] + opening_penalty + (j-k-1) * extension_penalty
                if max_row < s:
                    max_row = s
                    ind = (i, k)

            index.append(ind)
            maxes.append(max_row)

            for k in range(i):
                s = table[k][j] + opening_penalty + (i-k-1) * extension_penalty
                if max_col < s:
                    max_col = s
                    ind = (k, j)

            index.append(ind)
            index.append((i-1, j-1))

            table[i][j] = max(max_row, max_col, table[i-1][j-1] + get_score(seq1[i-1], seq2[j-1]))
            parent_table[i][j] = index[[max_row, max_col, table[i-1][j-1] + get_score(seq1[i-1], seq2[j-1])].index(table[i][j])]

    cur = (m, n)
    align_seq1, align_seq2 = "", ""
    p1, p2 = m-1, n-1

    while cur != (0, 0):

        if cur[1] - parent_table[cur[0]][cur[1]][1] == 1 and cur[0] - parent_table[cur[0]][cur[1]][0] == 1:
            align_seq1 = seq1[p1] + align_seq1
            align_seq2 = seq2[p2] + align_seq2
            p1 -= 1
            p2 -= 1

        elif cur[1] == parent_table[cur[0]][cur[1]][1]:
            for i in range(cur[0] - parent_table[cur[0]][cur[1]][0]):
                align_seq1 = seq1[p1] + align_seq1
                align_seq2 = '-' + align_seq2
                p1 -= 1

        elif cur[0] == parent_table[cur[0]][cur[1]][0]:
            for i in range(cur[1] - parent_table[cur[0]][cur[1]][1]):
                align_seq1 = '-' + align_seq1
                align_seq2 = seq2[p2] + align_seq2
                p2 -= 1

        cur = parent_table[cur[0]][cur[1]]

    print(table[m][n])
    print(align_seq1)
    print(align_seq2)

