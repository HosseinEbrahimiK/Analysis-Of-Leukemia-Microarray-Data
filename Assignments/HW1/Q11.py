class Node:
    def __init__(self, string):
        self.string = string
        self.adj = []
        self.in_adj = []
        self.in_degree = 0
        self.out_degree = 0


def odd_node():
    for w in nodes:
        if w.out_degree == 1:
            r = w.adj[0]
            if r.in_degree == 1:
                return True

    return False


def combine():
    for v in nodes:
        if v.out_degree == 1:
            u = v.adj[0]
            if u.in_degree == 1:
                u.string = v.string + u.string[-1]
                for w in v.in_adj:
                    ind = w.adj.index(v)
                    w.adj[ind] = u

                u.in_degree = v.in_degree
                index = nodes.index(v)
                del nodes[index]


if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/rosalind_ba3c.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))

    input_file.close()

    n = len(inp_txt)
    nodes = [Node(inp_txt[i][0]) for i in range(n)]

    for i in range(n):
        for j in range(n):
            if nodes[i].string[1:] == nodes[j].string[:-1]:
                nodes[i].adj.append(nodes[j])
                nodes[j].in_adj.append(nodes[i])

                nodes[i].out_degree += 1
                nodes[j].in_degree += 1

    while odd_node():
        combine()

    for i in range(len(nodes)):
        print(nodes[i].string)
