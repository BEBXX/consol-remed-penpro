n, t = [int(x) for x in input().split()]
s = input()
s = list(s)
cek = -1

while t > 0:
    for i in range(0, len(s)):
        if i < len(s) - 1:
            if (s[i] == 'L') and (s[i+1] == 'P') and (i != cek):
                s[i] = 'P'
                s[i+1] = 'L'
                cek = i + 1
    cek = -1
    t -= 1

print(''.join(s))