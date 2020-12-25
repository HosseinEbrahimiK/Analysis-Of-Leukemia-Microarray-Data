import math


class Node:
    def __init__(self, num):
        self.num = num
        self.adj = []


def nj(D, n, r, idx):
    if n == 2:

        tree = [Node(i) for i in range(r+1)]
        tree[idx[0]].adj.append([tree[idx[1]], D[0][1]])
        tree[idx[1]].adj.append([tree[idx[0]], D[0][1]])
        return tree

    D_prime = [[0 for _ in range(n)] for _ in range(n)]
    total_d = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            total_d[i] += D[i][j]

    minimum = math.inf
    index = ()
    limb = (0, 0)
    for i in range(n):
        for j in range(i + 1, n):
            D_prime[i][j] = (n - 2) * D[i][j] - total_d[i] - total_d[j]
            D_prime[j][i] = D_prime[i][j]

            if D_prime[i][j] < minimum:
                minimum = D_prime[i][j]
                index = (i, j)

    delta = (total_d[index[0]] - total_d[index[1]]) / (n-2)
    limb = ((D[index[0]][index[1]] + delta) / 2, (D[index[0]][index[1]] - delta) / 2)

    D_pass = [[0 for _ in range(n-1)] for _ in range(n-1)]
    arr = []

    for k in range(n):
        if k != index[0] and k != index[1]:
            arr.append((D[k][index[0]] + D[k][index[1]] - D[index[0]][index[1]]) / 2)

    arr.append(0)

    for row in D:
        del row[index[0]]
        del row[index[1] - 1]

    del D[index[0]]
    del D[index[1] - 1]

    for i in range(n-2):
        for j in range(n-2):
            D_pass[i][j] = D[i][j]

    for i in range(n-1):
        D_pass[n-2][i], D_pass[i][n-2] = arr[i], arr[i]

    r += 1
    idx2 = idx.copy()
    idx2.pop(index[0])
    idx2.pop(index[1]-1)
    idx2.append(r)

    T = nj(D_pass, n-1, r, idx2)
    T[idx[index[0]]].adj.append([T[r], limb[0]])
    T[idx[index[1]]].adj.append([T[r], limb[1]])
    T[r].adj += [[T[idx[index[0]]], limb[0]]] + [[T[idx[index[1]]], limb[1]]]

    return T


if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/dataset_206161_3.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))
    input_file.close()

    n = int(inp_txt[0][0])
    matrix = [[] for _ in range(n)]
    for i in range(1, n+1):
        matrix[i-1] = list(map(int, inp_txt[i][0].split()))

    idx = [i for i in range(n)]
    derakht = nj(matrix, n, n-1, idx)

    for v in derakht:
        for u in v.adj:
            print(str(v.num) + "->" + str(u[0].num) + ":" + "%.3f" % u[1])
