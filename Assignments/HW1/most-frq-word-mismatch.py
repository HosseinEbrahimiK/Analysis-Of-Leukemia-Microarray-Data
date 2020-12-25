from itertools import product

if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/rosalind_ba1j.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))

    text = inp_txt[0][0]
    k, d = map(int, inp_txt[1][0].split())

    pattern = list(product("ACGT", repeat=k))
    maximum = 0
    lst = []
    lst_pointer = 0

    for i in range(len(pattern)):
        s = ""
        for element in pattern[i]:
            if element == 'A':
                s += 'T'
            elif element == 'T':
                s += 'A'
            elif element == 'C':
                s += 'G'
            else:
                s += 'C'

        inv_pattern = s[::-1]
        count, inv_count = 0, 0

        for j in range(len(text) - k):
            miss1, miss2 = 0, 0
            t = 0
            for r in range(j, j+k):
                if pattern[i][t] != text[r]:
                    miss1 += 1

                if inv_pattern[t] != text[r]:
                    miss2 += 1
                t += 1

            if miss1 <= d:
                count += 1

            if miss2 <= d:
                inv_count += 1

        if maximum < count + inv_count:
            maximum = count + inv_count
            lst.append(pattern[i])
            lst_pointer = len(lst)-1

        elif maximum == count + inv_count:
            lst.append(pattern[i])

    for i in range(lst_pointer, len(lst)):
        print("".join(lst[i]))

