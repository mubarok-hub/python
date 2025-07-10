Operator AND (&)

Operator ini membandingkan dua angka bit per bit.
Hasilnya 1 hanya jika kedua bit sama-sama 1.
Jika salah satu bit 0, hasilnya 0.

Contoh:
x = 6   # biner: 110
y = 3   # biner: 011

Bandingkan per bit dari kanan ke kiri:

   1  1  0   (x = 6)
&  0  1  1   (y = 3)
-------------
   0  1  0   (hasil = 2)

Bit paling kanan: 0 & 1 = 0
Bit tengah: 1 & 1 = 1
Bit kiri: 1 & 0 = 0
Jadi, jika salah satu bit 0, hasilnya 0. Hanya jika dua-duanya 1, hasilnya 1.
Itulah kenapa hasilnya 2 (010 dalam biner).


Operator OR (|)
Operator ini membandingkan dua angka bit per bit.
Hasilnya 1 jika salah satu atau kedua bit bernilai 1.
Hanya jika kedua bit 0, hasilnya 0.

Contoh:
x = 6   # biner: 110
y = 3   # biner: 011

Bandingkan per bit:
   1  1  0   (x = 6)
|  0  1  1   (y = 3)
-------------
   1  1  1   (hasil = 7)

Bit paling kanan: 0 | 1 = 1
Bit tengah: 1 | 1 = 1
Bit kiri: 1 | 0 = 1
Jadi, jika salah satu bit 1, hasilnya 1.
Itulah kenapa hasilnya 7 (111 dalam biner).


Operator XOR (^)
Operator ini membandingkan dua angka bit per bit.
Hasilnya 1 jika kedua bit berbeda (satu 1, satu 0).
Jika kedua bit sama (dua-duanya 0 atau dua-duanya 1), hasilnya 0.

Contoh:
x = 6   # biner: 110
y = 3   # biner: 011

Bandingkan per bit:
   1  1  0   (x = 6)
^  0  1  1   (y = 3)
-------------
   1  0  1   (hasil = 5)

Bit kanan: 0 ^ 1 = 1 (beda)
Bit tengah: 1 ^ 1 = 0 (sama)
Bit kiri: 1 ^ 0 = 1 (beda)
Jadi, hasilnya 5 (101 dalam biner).
XOR cocok untuk mencari perbedaan antara dua nilai bit.