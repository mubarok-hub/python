# list
buah = ["apel", "jeruk", "mangga"]

buah.append("mangga") #tambah di akhir
buah[1] = "nanas" #ubah item ke1
buah.remove("apel") #hapus item apel
print(buah)
print(len(buah)) #jumlah item

# loop isi list
for item in buah:
    print("buah:",item)


#tuple
#data yang tidak bisa di ubah
data = ("apel", "jeruk", "mangga")
print(data[0]) #apel
print(data[-1]) #mangga

# dictionary(dist)
#data berpasangan key dan value
user = {
    "nama": "syahril",
    "umur": 20,
    "aktif": True
}

print(user["nama"]) #syahril #akses value
user["umur"] = 21 #ubah value
user["email"] = "syharil@gmail.com" #tambah key dan value baru
del user["aktif"] #hapus key dan value
print(user)

# loop isi dict
for key, value in user.items():
    print(key, ":", value)



# set
#data unik, tidak berurutan
#cocok unutk menghilangkan duplikat
angka = {1, 2, 3, 4, 5}
print(angka) #hasil: {1, 2, 3, 4, 5}

angka.add(4)
angka.remove(2)
print(angka) #hasil: {1, 3, 4, 5}
