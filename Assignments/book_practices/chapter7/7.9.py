def find_dist(str1, str2):
    n = len(str1)
    ans = 0
    for i in range(n):
        if str1[i] != str2[i]:
            ans += 1
    return ans


class node:
    def __init__(self, parent,  name):
        self.parent = parent
        self.children = []
        self.name = name
        self.label = ""
        self.current_char = ''
        self.s = [100000] * 4
        self.keep = [[0, 0] for i in range(4)]

    def check_ripe(self, visited):
        for i in range(len(self.children)):
            if visited[self.children[i].name] == False:
                return False
        return True

    def ret_min(self, c):w
        minimum = 100000000
        index = 0
        deltas = [1, 1, 1, 1]
        deltas[c] = 0
        for i in range(4):
            if self.s[i] + deltas[i] < minimum:
                minimum = self.s[i] + deltas[i]
                index = i
        return minimum, index


def sp(nodes):
    characters = ['A', 'T', 'C', 'G']
    visited = [False] * len(nodes)
    ripes = []
    for i in range(len(nodes)):
        if nodes[i].name < num_leaf:
            visited[i] = True
            nodes[i].s = [100000] * 4
            isRipe =  nodes[i].parent.check_ripe(visited)
            if isRipe:
                ripes.append(nodes[i].parent)
            for j in range(len(characters)):
                if nodes[i].current_char == characters[j]:
                    nodes[i].s[j] = 0

    while len(ripes) > 0:
        current = ripes[0]
        ripes.pop(0)
        visited[current.name] = True
        isRipe = False
        if current.parent != None:
            isRipe = current.parent.check_ripe(visited)
        if isRipe:
            ripes.append(current.parent)
        for c in range(len(characters)):
            daughter = current.children[0]
            son = current.children[1]
            d_min, d_in = daughter.ret_min(c)
            s_min, s_in = son.ret_min(c)
            current.s[c] = d_min + s_min
            current.keep[c][0] = d_in
            current.keep[c][1] = s_in

    minimum = 100000
    min_ind = 0
    for i in range(4):
        if current.s[i] < minimum:
            minimum = current.s[i]
            min_ind= i
    current.current_char = characters[min_ind]
    current.label += current.current_char

    queue = [current]
    inds = [min_ind]
    while len(queue) > 0:
        now = queue.pop(0)
        now_ind = inds.pop(0)
        if now.name >= num_leaf:
            d = now.children[0]
            s = now.children[1]
            if d.name < num_leaf:
                continue
            if s.name < num_leaf:
                continue
            d.current_char = characters[now.keep[now_ind][0]]
            s.current_char = characters[now.keep[now_ind][1]]
            d.label += d.current_char
            s.label += s.current_char
            queue.append(d)
            queue.append(s)
            inds.append(now.keep[now_ind][0])
            inds.append(now.keep[now_ind][1])


    return min(current.s)


lines = list(open('data.txt', 'r'))
num_leaf = int(lines[0])
characters = ['A', 'T', 'C', 'G']
leaf = 0
nodes = [None for i in range(len(lines))]
for i in range(1,len(lines)):
    string = str(lines[i])
    string = string.replace("\n", "")
    symbol1 = string.find('-')
    symbol2 = string.find('>')
    fr = int(string[0:symbol1])
    if not nodes[fr]:
        nodes[fr] = node(None, fr)
    to = string[symbol2 + 1:]
    if ord(to[0]) >= 65:
        nodes[leaf] = node(nodes[fr], leaf)
        nodes[fr].children.append(nodes[leaf])
        nodes[leaf].label = to
        nodes[leaf].current_char = to[0]
        leaf += 1
    else:
        to = int(to)
        if not nodes[to]:
            nodes[to] = node(nodes[fr], to)
        nodes[to].parent = nodes[fr]
        nodes[fr].children.append(nodes[to])


res = 0
for i in range(len(nodes[0].label)):
    for j in range(num_leaf):
        nodes[j].current_char = nodes[j].label[i]
    res += sp(nodes)

print(res)

l = len(nodes)

r = [[0 for i in range(l)] for j in range(l)]
for i in range(l):
    if nodes[i].parent is not None:
        r[i][nodes[i].parent.name] = find_dist(nodes[i].label, nodes[i].parent.label)
        r[nodes[i].parent.name][i] = find_dist(nodes[i].label, nodes[i].parent.label)


for i in range(l):
    for j in range(l):
        if r[i][j] > 0:
            print(nodes[i].label + "->" + nodes[j].label + ":" + str(r[i][j]))