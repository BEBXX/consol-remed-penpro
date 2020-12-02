try:
    a,b,c,d,e = map(int,input().split())
    cond1 = (a <= b <= c <= d <= e)
    cond2 = (a >= b >= c >= d >= e)
    print(cond1 or cond2)

except ValueError:
    print("input tidak valid")