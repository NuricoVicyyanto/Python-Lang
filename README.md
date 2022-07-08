# Python-Lang

<hr>

## Belajar dasar-dasar bahasa pemrograman python

### Python

<p>Menurut pengertian dari Python Software Foundation (2016), Python adalah bahasa pemrograman interpretatif, berorinetasi objek dan semantik yang dinamis. Python memiliki high-level struktur data, dynamic typing dan dynamic binding.</p>
<p>Untuk sejarah bahasa pemrograman Python sendiri seperti dikutip dari laman baktikominfo.id => <a href="https://www.baktikominfo.id/id/informasi/pengetahuan/bahasa_pemrograman_python_pengertian_sejarah_kelebihan_dan_kekurangannya-954">Link</a> Python dibuat dan dikembangkan oleh Guido Van Rossum, yaitu seorang programmer yang berasal dari Belanda. Pembuatannya berlangsung di kota Amsterdam, Belanda pada tahun 1990. Pada tahun 1995 Python dikembangkan lagi agar lebih kompatibel oleh Guido Van Rossum. Selanjutnya pada awal tahun 2000, terdapat pembaharuan versi Python hingga mencapai Versi 3 sampai saat ini. Pemilihan nama Python sendiri diambil dari sebuah acara televisi yang lumayan terkenal yang bernama Mothy Python Flying Circus yang merupakan acara sirkus favorit dari Guido van Rossum.</p>

### Instalasi Python Windows

Untuk menjalankan Python pada windows kita harus melakukan penginstallan interpreter python terlebih dahulu, adapun langkah-langkah instalasi adalah sebagai berikut :

- Buka browser dan kunjungi link berikut => <https://www.python.org/>
- Masuk ke menu download dan pilih versi python yang akan diunduh
- Buka file installer ang baru saja diunduh
- Ikuti langkah instalasi sampai selesai (pastikan python ditambahkan ke path)

### Menjalankan Program Python

Untuk menjalankan program python kita dapat menggunakan terminal python atau menggunakan code editor seperti PyCharm, VSCode, Sublime Text dll. dan untuk membuat sebuah file project python pada text editor kita harus membuat file dengan format .py yang merupakan format untuk bahasa pemrograman Python. berikut merupakan contoh program sederhana python yaitu mencetak Hello World :

```python
print("Hello World")
```

** Python bersifat case sansitif, artinya huruf besar dan kecil dianggap berbeda, sebagai contoh `print()` akan berhasil dieksekusi dan `Print()` akan gagal dieksekusi,keduanya dianggap berbeda karena perbedaan huruf besar dan kecil.

### Komentar

<p>Komentar adalah sebuah baris pada program yang tidak dieksekusi, tujuan dari dibuatnya komentar pada baris program adalah untuk menandai serta memberikan keterangan pada baris program.</p>
<p>Komentar biasa digunakan untuk tujuan agar kita dapat mengingat kembali alur program yang kita tulis dan juga agar orang lain dapat memahami alur program yang kita tulis.</p>

Pada python sendiri penulisan komentar dapat menngunakan tanda `#` untuk komentar satu baris dan tanda `""" """` untuk penulisan komentar lebih dari satu baris. Berikut adalah contoh penulisan komentar pada bahasa pemrograman Python:

```python
# ini adalah komentar
# tulisan dengan tanda komentar tidak akan dieksekusi

# komentar dengan menggunakan tanda pagar hanya dapat
# digunakan untuk satu baris tulisan

"""pada penulisan komentar untuk kalimat lebih satu baris menggunakan tanda 
kutip 2 sebanyak 3 kali pada awal dan akhir"""

print("Tulisan ini akan dieksekusi karena tidak terdapat tanda komentar")
```

### Tipe Data

<p>Tipe data merupakan nilai yang disimpan dalam memori komputer, Python memiliki beberapa macam tipe data dan setiap tipe data disimpan pada variabel untuk digunakan.</p>
<p>Berikut merupakan tipe data dari bahasa pemrograman Python :</p>

| Tipe Data | Penjelasan |
| ------- | ----- |
| **Boolean** | Menyatakan benar `True` yang memiliki nilai `1` dan False yang memiliki nila `0` |
| **String** | Menyatakan kalimat atau karakter bisa berupa huruf atau angka dll., untuk menggunakan string ditandai dengan tanda `" "` atau `' '` |
| **Integer** | Menyatakan bilangan bulat |
| **Float** | Menyatakan bilangan desimal |
| **hexadecimal** | Menyatakan bilangan dalam format hexadecimal yaitu bilangan berbasis 16 |
| **Complex** | Menyatakan pasangan angka real dan imajiner |
| **List** | Merupakan untaian data yang dapat menyimpan berbagai tipe data dan isinya dapat dirubah |
| **Tuple** | Merupakan untaian data yang dapat menyimpan berbagai tipe data dan isinya tidak dapat dirubah |
| **Dictionary** | Merupakan untaian data yang dapat menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai |

Adapun berikut merupakan contoh dari penggunaan tipe data pada bahasa pemrograman Python :

```python
# fungsi dari type() adalah untuk mengetahui dari tipe data yang dieksekusi
# tipe data boolean
print(type(True))
print(type(False))

# tipe data string
print(type("Tipe data string"))
print(type('tipe data string'))

# tipe data integer
print(type(26))

# tipe data float
print(type(26.8))

# tipe data data hexadesimal
print(hex(26))

# tipe data complex
print(type(5j))

# tipe data list
list = ["angga", "anggi", "anggun"]
print(type(list))

# tipe data tuple
tuple = ("angga", "anggi", "anggun")
print(tuple)
print(type(tuple))

# tipe data dictionary
dict = {"nama":"angga", "status":"pengguna"}
print(dict)
print(type(dict))

```

### Variabel

<p>Variabel adalah tempat yang digunakan untuk menampung data di memori yang memiliki nilai yang dapat diubah selama proses program. Pada Python variabel dapat menyimpan berbagai tipe data dan juga variabel di Python memiliki sifat yang dinamis dimana kita tidak perlu mendaklarasikan tipe data tertentu.</p>

<p>Berikut merupakan contoh penggunaan variabel menggunakan bahasa pemrograman Python :</p>

```python
# variabel
nama = "Nurico Vicyyanto"
print(nama)

namaDepan = "Nurico"
namaBelakang = "Vicyyanto"
hobi = "Badminton"
# tanda \n dapat ditambahkan pada teks jika memerlukan spasi
teks = namaDepan + " " + namaBelakang + " hobi bermain\n" + hobi
print(teks)

# tipe data string dapat dikalikan dengan integer
print("=" * 10)

# operasi perkalian dengan pendefinisial angka pada variabel
panjang = 10
lebar = 10
luas = panjang * lebar
print(luas)
```

#### Coming Soon...
