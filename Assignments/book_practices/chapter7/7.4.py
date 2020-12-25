import math


class Node:
    def __init__(self, num):
        self.adj = []
        self.num = num
        self.visited = False
        self.parent = None


def limb(D, n):
    minimum = math.inf
    id1, id2 = 0, 0
    for i in range(n):
        for k in range(i+1, n):
            if i != n-1 and k != n-1:
                if (D[i][n-1] + D[n-1][k] - D[i][k]) / 2 < minimum:
                    minimum = (D[i][n-1] + D[n-1][k] - D[i][k]) / 2
                    id1, id2 = i, k

    return minimum, id1, id2


def BFS(s, t):
    queue = list()
    queue.append(s)
    s.visited = True

    while queue:
        s = queue.pop(0)

        for node in s.adj:

            if node[0].visited is False:
                queue.append(node[0])
                node[0].parent = s
                node[0].visited = True
            if t.visited is True:
                break

    path = []
    pre = t
    while pre is not None:
        path.append(pre.num)
        pre = pre.parent

    path.reverse()
    return path


def AdditivePhylogeny(D):
    global r
    global er
    n = len(D)

    if n == 2:
        tree = [Node(i) for i in range(er)]
        tree[0].adj.append([tree[1], D[0][1]])
        tree[1].adj.append([tree[0], D[0][1]])
        return tree

    limb_length, i_node, k_node = limb(D, n)

    for j in range(n):
        D[j][n-1] = D[j][n-1] - limb_length
        D[n-1][j] = D[j][n-1]

    x = D[i_node][n - 1]

    for row in D:
        del row[n - 1]

    del D[n - 1]

    T = AdditivePhylogeny(D)

    for v in T:
        v.visited, v.parent = False, None

    p = BFS(T[i_node], T[k_node])

    count = 0
    for i in range(len(p)-1):
        c = count
        for v in T[p[i+1]].adj:
            if v[0].num == p[i]:
                count += v[1]
                break

        if count == x:
            T[n-1].adj.append([T[p[i+1]], limb_length])
            T[p[i+1]].adj.append([T[n-1], limb_length])

        elif count > x:

            id1, id2 = 0, 0
            T.append(Node(r))
            r += 1
            for j in range(len(T[p[i]].adj)):
                if T[p[i]].adj[j][0].num == p[i+1]:
                    id1 = j
                    break

            for j in range(len(T[p[i+1]].adj)):
                if T[p[i+1]].adj[j][0].num == p[i]:
                    id2 = j
                    break

            T[p[i]].adj[id1][0], T[p[i]].adj[id1][1] = T[-1], x - c
            T[p[i+1]].adj[id2][0], T[p[i+1]].adj[id2][1] = T[-1], count - x
            T[-1].adj += [[T[p[i]], x-c]] + [[T[p[i+1]], count-x]]

            T[-1].adj.append([T[n-1], limb_length])
            T[n-1].adj.append([T[-1], limb_length])

    return T


inp_txt = []
with open('/Users/joliaserm/Desktop/dataset_206161_3.txt') as input_file:
    for line in input_file:
        inp_txt.append(line.strip().split(','))
input_file.close()

er = int(inp_txt[0][0])
matrix = [[]for _ in range(er)]

for i in range(1, er+1):
    matrix[i-1] = list(map(int, inp_txt[i][0].split()))
r = er
g = AdditivePhylogeny(matrix)

for v in g:
    for u in v.adj:
        print(str(v.num) + "->" + str(u[0].num) + ":" + str(u[1]))
