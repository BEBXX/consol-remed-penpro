gol = input("Masukkan golongan karyawan: ")
while not (gol == "A" or gol == "B" or gol == "C" or gol == "D"):
    gol = input("Masukkan golongan karyawan: ")

if gol == "A":
    print("Gaji Pokok: 2000000")
elif gol == "B":
    print("Gaji Pokok: 3000000")
elif gol == "C":
    print("Gaji Pokok: 4000000")
elif gol == "D":
    print("Gaji Pokok: 5000000")
