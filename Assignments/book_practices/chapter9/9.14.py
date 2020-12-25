class Permutations:
    def __init__(self):
        self.string = None
        self.pos = -1


def index(char):
    if char == 'A':
        return 0
    elif char == 'T':
        return 1
    elif char == 'C':
        return 2
    elif char == 'G':
        return 3
    elif char == '$':
        return 4


def bwm_matching(pattern, top, bot, mis_match, first_occurrence, cnt):
    if not pattern:
        internals.append([top, bot])
        return

    char = pattern[-1]
    aux = pattern[:-1]
    symbol = index(char)

    if cnt[bot + 1][symbol] - cnt[top][symbol] > 0:
        top = first_occurrence[symbol] + cnt[top][symbol]
        bot = first_occurrence[symbol] + cnt[bot+1][symbol] - 1
        bwm_matching(aux, top, bot, mis_match, first_occurrence, cnt)

    if mis_match > 0:
        mis_match -= 1
        for k in range(4):
            if k != symbol:
                if cnt[bot+1][k] - cnt[top][k] > 0:
                    top = first_occurrence[k] + cnt[top][k]
                    bot = first_occurrence[k] + cnt[bot+1][k] - 1
                    bwm_matching(aux, top, bot, mis_match, first_occurrence, cnt)


if __name__ == "__main__":

    inp_txt = []
    with open('/Users/joliaserm/Desktop/dataset_206161_3.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))
    input_file.close()

    text = inp_txt[0][0] + "$"
    patterns = inp_txt[1][0].split()
    d = int(inp_txt[2][0])
    permutations = [Permutations() for _ in range(len(text))]
    string = text
    permutations[0].string, permutations[0].pos = string, 0

    for i in range(1, len(text)):
        string = string[1:len(string)] + string[0]
        permutations[i].string, permutations[i].pos = string, i

    permutations.sort(key=lambda element: element.string)
    first_column, last_column = [], []

    for p in permutations:
        first_column.append([p.string[0], p.pos])
        last_column.append([p.string[-1], p.pos])

    first_occurrence = [0] * 5
    for i in range(1, len(first_column)):
        if first_column[i][0] != first_column[i-1][0]:
            first_occurrence[index(first_column[i][0])] = i

    count = [[0 for _ in range(5)] for _ in range(len(last_column)+1)]

    for i in range(1, len(last_column)+1):
        count[i][index(last_column[i-1][0])] = count[i-1][index(last_column[i-1][0])] + 1
        for j in range(5):
            if j != index(last_column[i-1][0]):
                count[i][j] = count[i-1][j]

    internals = []
    bwm_matching(patterns[0], 0, len(last_column) - 1, d, first_occurrence, count)
    print(internals)

    for e in internals:
        if e is not None:
            if e[1] != e[0]:
                print(last_column[e[0]][1], end=" ")
                print(last_column[e[1]][1], end=" ")
            else:
                print(last_column[e[0]][1], end=" ")

