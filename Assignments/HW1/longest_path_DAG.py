import math


class Node:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.visited = False
        self.max_d = -math.inf
        self.parent = None


def topological_sort(s):
    stack = list()
    stack.append(nodes[s])
    tpl_list = list()

    for u in nodes[s].adj:
        if u[0].visited is False:
            stack.insert(0, u[0])
            topological_sort_util(u[0], stack, tpl_list)

    v = stack.pop(0)
    v.visited = True
    tpl_list.append(v)

    return tpl_list


def topological_sort_util(node, stack, l):
    for v in node.adj:
        if v[0].visited is False:
            stack.insert(0, v[0])
            topological_sort_util(v[0], stack, l)

    v = stack.pop(0)
    v.visited = True
    l.append(v)


if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/rosalind_ba5d.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))

    x, y = int(inp_txt[0][0]), int(inp_txt[1][0])
    lst = []
    maximum = 0
    for i in range(2, len(inp_txt)):
        string = inp_txt[i][0]
        st, end, w, ind = 0, 0, 0, 0
        for j in range(len(string)):
            if string[j] == '-':
                st = int(string[0:j])
                ind = j + 2

            if string[j] == ':':
                end, w = int(string[ind:j]), int(string[j+1:])

        lst.append([st, end, w])
        if end > maximum:
            maximum = end

    nodes = [Node(i) for i in range(maximum+1)]

    for i in range(len(lst)):
        nodes[lst[i][0]].adj.append([nodes[lst[i][1]], lst[i][2]])
    sorted_node = topological_sort(x)
    sorted_node.reverse()

    sorted_node[0].max_d = 0
    for i in range(len(sorted_node)):
        for element in sorted_node[i].adj:
            if sorted_node[i].max_d + element[1] > element[0].max_d:
                element[0].max_d = sorted_node[i].max_d + element[1]
                element[0].parent = sorted_node[i]

    print(nodes[y].max_d)

    parent_list = list()
    per = nodes[y]
    while per is not None:
        parent_list.append(per.num)
        per = per.parent

    parent_list.reverse()
    for i in range(len(parent_list)):
        if i == len(parent_list)-1:
            print(str(parent_list[i]))
        else:
            print(str(parent_list[i])+"->", end="")
