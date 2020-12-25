class Word:
    def __init__(self, char):
        self.char = char
        self.ind = 0


if __name__ == "__main__":

    inp_txt = []
    with open('/Users/joliaserm/Desktop/dataset_206161_3.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))
    input_file.close()

    bwt = inp_txt[0][0]

    last_column = [Word(bwt[i]) for i in range(len(bwt))]
    first_column = sorted(last_column, key=lambda element: element.char)

    for i in range(1, len(first_column)):
        if first_column[i].char == first_column[i-1].char:
            first_column[i].ind += first_column[i-1].ind + 1
    index = 0
    for i in range(len(last_column)):
        if last_column[i].char == '$':
            index = i
            break

    string = ""
    while len(string) != len(bwt):
        string += first_column[index].char
        for i in range(len(last_column)):
            if last_column[i].char == first_column[index].char and last_column[i].ind == first_column[index].ind:
                index = i
                break

    print(string)
