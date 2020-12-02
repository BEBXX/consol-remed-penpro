exit = []
enter = []

n = int(input())

for i in range(0, n):
    newExit, newEnter = [int(x) for x in input().split()]
    exit.append(newExit)
    enter.append(newEnter)

a = 0
passenger = 0
max = 0


while a < len(enter):
    passenger -= exit[a]
    passenger += enter[a]
    if passenger > max:
        max = passenger
    
    a += 1

print(max)


# versi lebih pendek
# total = 0
# out = []
# for i in range (int(input())):
#     a, b = map(int, input().split())
#     total = total - a + b
#     out.append(total)

# print(max(out))