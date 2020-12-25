class Node:
    def __init__(self):
        self.mark = False
        self.edges = [None] * 4


def insert(node, string, index):

    if len(string) == index:
        node.mark = True
        return

    if string[index] == 'A':
        cur = 0
    elif string[index] == 'T':
        cur = 1
    elif string[index] == 'G':
        cur = 2
    else:
        cur = 3

    if node.edges[cur] is None:
        node.edges[cur] = Node()

    insert(node.edges[cur], string, index+1)


def search(node, string, index, k):

    if node.mark is True:
        return True

    if index + k >= len(text):
        return False

    if string[index] == 'A':
        cur = 0
    elif string[index] == 'T':
        cur = 1
    elif string[index] == 'G':
        cur = 2
    else:
        cur = 3

    if node.edges[cur] is None:
        return False

    return search(node.edges[cur], string, index+1, k)


if __name__ == "__main__":

    inp_txt = []
    with open('/Users/joliaserm/Desktop/dataset_206161_3.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))
    input_file.close()

    text = inp_txt[0][0]
    patterns = []

    for i in range(1, len(inp_txt)):
        patterns.append(inp_txt[i][0])

    root = Node()
    for p in patterns:
        insert(root, p, 0)

    ans = []
    for i in range(len(text)):
        if search(root, text[i:], 0, i) is True:
            ans.append(i)

    for a in ans:
        print(a, end=" ")
