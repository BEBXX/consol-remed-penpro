berat = int(input())
if berat >= 1000:
    kg = berat//1000
    gr = berat%1000
elif berat < 1000:
    kg = 0
    gr = berat

print(f"{berat} gram = {kg} kilogram {gr} gram")
