def pattern(n):
    for L in n:
        print("|", end = " " )
        print("*" * int(L))


n = "01325"
pattern(n)