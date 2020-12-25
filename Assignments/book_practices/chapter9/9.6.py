class Suffix:
    def __init__(self, string, pos):
        self.str = string
        self.pos = pos


def binary_search(arr, l, r, x):

    if r < l:
        return -1

    mid = (r+l) // 2

    if arr[mid].str[:len(x)] == x:
        return mid

    if x < arr[mid].str[:len(x)]:
        return binary_search(arr, l, mid-1, x)
    else:
        return binary_search(arr, mid+1, r, x)


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

    suffixes = [Suffix(text[i:], i) for i in range(len(text))]

    suffixes.sort(key=lambda element: element.str)

    ans = []
    for p in patterns:
        ind = binary_search(suffixes, 0, len(suffixes)-1, p)
        if ind != -1:
            low, high = ind-1, ind+1
            while suffixes[low].str[:len(p)] == p:
                low -= 1

            while suffixes[high].str[:len(p)] == p:
                high += 1

            ans.append([low+1, high-1])

    for i in range(len(ans)):
        for j in range(ans[i][0], ans[i][1]+1):
            print(suffixes[j].pos, end=" ")
