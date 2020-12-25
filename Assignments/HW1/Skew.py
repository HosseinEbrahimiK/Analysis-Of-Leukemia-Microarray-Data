if __name__ == "__main__":

    inp_txt = open("/Users/joliaserm/Desktop/rosalind_ba1f.txt", "r").read()

    min_dif = 0
    index = []
    index_pointer = 0
    cnt = 0

    for i in range(len(inp_txt)):
        if inp_txt[i] == 'C':
            cnt -= 1

        elif inp_txt[i] == 'G':
            cnt += 1

        if min_dif > cnt:
            min_dif = cnt
            index += [i+1]
            index_pointer = len(index)-1

        elif min_dif == cnt:
            index += [i+1]

    print(index)

    for i in range(index_pointer, len(index)):
        if i == len(index)-1:
            print(index[i])
        else:
            print(index[i], end=" ")
