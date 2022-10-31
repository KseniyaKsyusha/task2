m, n = map(int, input('Введіть розмір шахової дошки m x n: ').split())
for i in range(m):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(chr(9633), end=" ")
        else:
            print(chr(9632), end=" ")
    print("")
##################################################
for i in range(m):
    # print(*[print(chr(9633), end=" ") for j in range(n) if (i + j) % 2 == 0])
    print(*[print(chr(9633), end=" ") if (i + j) % 2 == 0 else print(chr(9632), end=" ") for j in range(n)])
############################################################