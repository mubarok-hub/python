# list
belanja = ["beras", "minyak", "telur"]
belanja[1] = "mie"
belanja.remove("telur")
print(len(belanja))  # jumlah item

# dict
produk = {"nama": "laptop", "harga": 15000000}
produk["stok"] = 10  # tambah key dan value baru
produk["harga"] = 20000000  # ubah value
print(produk)

# set
angka = {1, 2, 2, 3, 3, 3, 4,}
angka.add(5)  # tambah angka 5
angka.remove(2)  # hapus angka 2