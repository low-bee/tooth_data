# print(sum(list(map(int, input().strip().split(" ")))))
n = eval(input())
wind = list(map(eval, input().strip().split()))
ret = [0 for _ in range(n)]

for i in range(0, n):

    j = 1
    for k in range(0, i):
        if wind[i] > wind[k]:
            ret[k] += 1
        elif wind[i] == wind[k]:
            pass
        else:
            j += 1

    ret[i] = j

print(" ".join(map(str, ret)))

