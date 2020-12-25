from itertools import product


if __name__ == "__main__":
    inp_txt = []
    with open('/Users/joliaserm/Desktop/rosalind_ba1n.txt') as input_file:
        for line in input_file:
            inp_txt.append(line.strip().split(','))

    pattern = tuple(inp_txt[0][0])
    d = int(inp_txt[1][0])

    all_cases = list(product("ACGT", repeat=len(pattern)))

    for case in all_cases:
        mismatch = 0
        for i in range(len(pattern)):
            if case[i] != pattern[i]:
                mismatch += 1
            if mismatch > d:
                break

        if mismatch <= d:
            print("".join(case))
