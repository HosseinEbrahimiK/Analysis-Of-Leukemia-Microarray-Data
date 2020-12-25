if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/rosalind_ba1h.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))

    pattern = inp_txt[0][0]
    string = inp_txt[1][0]
    num_mismatch = int(inp_txt[2][0])
    index = []

    for i in range(len(string)-len(pattern)):
        k = 0
        cnt = 0
        for j in range(i, i+len(pattern)):
            if string[j] != pattern[k]:
                cnt += 1

            if cnt > num_mismatch:
                break
            k += 1

        if cnt <= num_mismatch:
            index.append(i)

    for i in range(len(index)):
        if i == len(index)-1:
            print(index[i])
        else:
            print(index[i], end=" ")
