# list
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
print(buah[1]) #jeruk
print(buah[-1]) #pisang
print(buah[1:3]) #['jeruk', 'mangga']

# dictionary
user = {"nama": "syahril", "umur": 24, "menikah": true}
print(user["nama"]) #syahril
print(user.get("umur")) #24
print(user.keys()) #dict_keys(['nama', 'umur', 'menikah'])
print(user.values()) #dict_values(['syahril', 24, True])

# tuple
data = ("apel", "jeruk", "mangga")
print(data[0]) #apel
print(data[-1]) #mangga
koordinat = (10, 20)
print(koordinat[0]) #10
print(koordinat[1]) #20

# set
angka = {1, 2, 3, 4, 5}
print(angka) #{1, 2, 3, 4, 5}
angka.add(6)
print(angka) #{1, 2, 3, 4, 5, 6}
angka.remove(3)
print(angka) #{1, 2, 4, 5, 6}
