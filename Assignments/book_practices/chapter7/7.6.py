import math


class Node:
    def __init__(self, num):
        self.meb = []
        self.num = num
        self.age = 0
        self.parent = None
        self.edge = 0


def compute(mat, c1, c2):
    count = 0
    for v in c1.meb:
        for u in c2.meb:
            count += (mat[v.num][u.num])

    return count / (len(c1.meb)*len(c2.meb))


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

    clusters = [Node(i) for i in range(len(matrix))]

    for i in range(len(matrix)):
        clusters[i].meb.append(clusters[i])
    k = n
    s = []
    while len(clusters) != 1:

        minimum = math.inf
        index = (0, 0)
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                t = compute(matrix, clusters[i], clusters[j])
                if minimum > t:
                    minimum = t
                    index = (i, j)

        clusters.append(Node(k))

        k += 1
        for c in clusters[index[0]].meb:
            clusters[-1].meb.append(c)
        for d in clusters[index[1]].meb:
            clusters[-1].meb.append(d)

        clusters[index[0]].parent = clusters[-1]
        clusters[index[1]].parent = clusters[-1]

        clusters[-1].age = minimum / 2

        clusters[index[0]].edge = clusters[-1].age - clusters[index[0]].age
        clusters[index[1]].edge = clusters[-1].age - clusters[index[1]].age

        s.append(clusters.pop(index[0]))
        s.append(clusters.pop(index[1]-1))

    for v in s:
        print(str(v.num) + "->" + str(v.parent.num)+":"+"%.3f" % v.edge)
        print(str(v.parent.num) + "->" + str(v.num)+":" + "%.3f" % v.edge)
