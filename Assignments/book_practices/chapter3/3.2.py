if __name__ == "__main__":

    k = int(input())
    s = input()
    n = len(s)
    for i in range(n - k+1):
        print(s[i:i+k])
