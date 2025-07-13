def halo(nama):
    return f"Halo, {nama}!"

print(halo("alin"))

def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print('hasil:', hasil)

def cek_nilai(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 75:
        return "B"
    else:
        return "C"

print(cek_nilai(85))  # Output: B