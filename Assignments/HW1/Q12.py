class Node:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.in_degree = 0
        self.out_degree = 0
        self.visited = False


if __name__ == "__main__":

    inp_txt = []
    with open("/Users/joliaserm/Desktop/rosalind_ba3c.txt") as input_file:
        for line in input_file:
            inp_txt.append(line.strip())

    edges = []
    for i in range(len(inp_txt)):
        s = str(inp_txt[i]).split()
        integers = list(map(int, s[2].split(',')))
        edges.append([int(s[0])] + [integers[j] for j in range(len(integers))])

    maximum = max(max(edges))
    nodes = [Node(i) for i in range(maximum+1)]

    for element in edges:
        for i in range(1, len(element)):
            nodes[element[0]].adj.append(nodes[element[i]])
            nodes[element[i]].in_degree += 1
            nodes[element[0]].out_degree += 1

    paths = []
    for v in nodes:
        if v.in_degree != 1 or v.out_degree != 1:
            if v.out_degree > 0:
                for w in v.adj:
                    NonBranchingPath = [v.num]
                    k = 0
                    while w.in_degree == 1 and w.out_degree == 1:
                        NonBranchingPath.append(w.num)
                        w = w.adj[k]
                    NonBranchingPath.append(w.num)
                    paths.append(NonBranchingPath)

    cycles = []
    for v in nodes:
        flag = 1
        v.visited = True
        if v.in_degree == 1 and v.out_degree == 1:
            w = v.adj[0]
            cycle = [v.num]
            while w != v:
                if w.in_degree == 1 and w.out_degree == 1 and w.visited is False:
                    cycle.append(w.num)
                    w.visited = True
                    w = w.adj[0]
                else:
                    flag = 0
                    break

            if flag == 1:
                cycle.append(v.num)
                cycles.append(cycle)

    out = paths + cycles

    for i in range(len(out)):
        for j in range(len(out[i])):
            if j == len(out[i])-1:
                print(out[i][j])
            else:
                print(str(out[i][j]), end=" -> ")
