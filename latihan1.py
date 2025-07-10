# variabel & tipe data 
nama = "Syahril"
umur = 20
tinggi = 170.5
menikah = True

print(nama, umur, tinggi, menikah)

# aritmatika dasar
gaji = 1000000
bonus = 250000
total_gaji = gaji + bonus
print("Total gaji:", total_gaji)

# cara menghitung potongan 10%
potongan = total_gaji * 10 / 100
total_gaji_setelah_potongan = total_gaji - potongan
print("Total gaji setelah dipotong 10%:", total_gaji_setelah_potongan)

# pengkondisian
umur = 60
if umur >= 60:
    print("Lansia")
elif umur >= 30:
    print("Dewasa")
elif umur >= 18:
    print("Remaja")
else:
    print("Anak-anak")

# perulangan
for i in range(1):
    print("loop ke-", i)

# bitwise kecil
x = 6
y = 3
print("x & y =", x & y)  # AND
print("x | y =", x | y)  # OR
print("x ^ y =", x ^ y)  # XOR
print("~x =", ~x)  # NOT
print("x << 1 =", x << 1)  # Shift left
print("x >> 1 =", x >> 1)  # Shift right