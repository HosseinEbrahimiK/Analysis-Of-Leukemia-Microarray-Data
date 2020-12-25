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
