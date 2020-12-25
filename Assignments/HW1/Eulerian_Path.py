class Node:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.in_degree = 0
        self.out_degree = 0


if __name__ == "__main__":

    inp_txt = []
    with open("/Users/joliaserm/Desktop/rosalind_ba3g.txt") as input_file:
        for line in input_file:
            inp_txt.append(line.strip())

    edges = []
    for i in range(len(inp_txt)):
        s = str(inp_txt[i]).split()
        integers = list(map(int, s[2].split(',')))
        edges.append([int(s[0])] + [integers[j] for j in range(len(integers))])

    maximum = max(max(edges))
    nodes = [Node(i) for i in range(maximum+1)]
    num_edges = 0

    for element in edges:
        for i in range(1, len(element)):
            nodes[element[0]].adj.append(nodes[element[i]])
            nodes[element[i]].in_degree += 1
            nodes[element[0]].out_degree += 1
            num_edges += 1

    start = None
    for i in range(len(nodes)):
        if nodes[i].out_degree - nodes[i].in_degree == 1:
            start = nodes[i]
            break

    node = start
    path = [node]
    euler_path = []

    while len(path) != 0:

        if len(node.adj) != 0:
            path.insert(0, node)
            node = node.adj.pop(0)

        else:
            euler_path.append(node)
            node = path.pop(0)

    for i in range(len(euler_path)-1, -1, -1):
        if i != 0:
            print(euler_path[i].num, end="->")
        else:
            print(euler_path[i].num)
