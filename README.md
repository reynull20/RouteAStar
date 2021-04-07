# RouteAStar
RouteAStar merupakan program python sederhana yang mencari sebuah path dengan cost terendah menggunakan algoritma A*

# Algoritma
Algoritma decrease and conquer: 
1.	Hitung derajat masuk setiap simpul pada graf (N).
2.	Eliminasi n simpul dengan derajat = 0 dan simpan simpul tersebut pada sebuah tuple solusi. Untuk setiap simpul yang dieliminasi, lakukan pengurangan derajat masuk dari simpul yang bersisian dari simpul yang dieliminasi (next node )
3.	Ulangi proses 1-2 terhadap N-n simpul yang tersisa.

# Cara Penggunaan
1. Buka cmd
2. pindahkan cd ke lokasi main.py
3. Run main.py dengan mengetik "Python3 main.py"
4. Masukkan nama file pada saat muncul pesan "Enter Graf File Name : ". Pastikan file terdapat pada folder test dan format isi file sesuai dengan berikut.

 <jumlah node>
 <nama node1> <posisi X node1> <posisi Y node1>
 .
 .
 .
 <nama nodeN> <posisi X nodeN> <posisi Y nodeN>
 //Matriks ketetanggaan dengan nilai berupa boolean
 //nilai matriks menyatakan nodeA dan nodeB terhubung
 //Contoh
 1 0 0 1
 0 1 0 1
 0 1 0 0 
 0 0 0 0 

5. Graf akan ditampilkan pada layar beserta pilihan node
6. Tutup window graf, lalu masukkan Node asal dan Node tujuan pada CLI
7. Path akan tertulis pada CLI beserta costnya, dan akan ditampilkan Pathnya pada graf yang ditandai dengan node berwarna putih

# Batasan 
program ini tidak menyediakan data dalam bentuk peta,

# AUTHOR
13519045 - M.Reyhanullah Budiaman
