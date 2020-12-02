a, b,c = map(int, input().split())
total = (a + b + c)/3
if total > 0:
    print("positif")
elif total < 0:
    print("negatif")
elif total == 0:
    print("nol")
