I am editing the README file. Adding some more details about the project description.
# Routh-Stability-Criteria

#Import library numpy
import numpy as np
def get_poly():

# Menerima masukan pengguna untuk koefisien polinomial
 poly = input("Masukkan koefisien polinomial: ")
 poly = poly.split()
 poly = [float(p) for p in poly]
 return poly
def get_table(poly, k):

# Mendapatkan jumlah baris dan kolom untuk tabel Routh
 num_rows = len(poly)//2 + len(poly) % 2
 num_cols = len(poly) - 1
 
# Membuat tabel Routh
 table = np.zeros((num_rows, num_cols))
 table[0,:] = poly[::2]
 table[1,:] = poly[1::2]
 
# Mengisi baris tabel Routh yang tersisa
 for i in range(2, num_rows):
 for j in range(num_cols):
 if table[i-1,0] == 0:
 table[i,j] = 0
 else:
 
# Menghitung nilai elemen saat ini menggunakan rumus Routh
 table[i,j] = ((table[i-1,0]*table[i-2,j+1]) -
 (table[i-2,0]*table[i-1,j+1])) / table[i-1,0]
 
# Menambahkan nilai umpan balik ke kolom pertama tabel Routh
 table[0,0] += k
 return table
 
# Menerima polinomial dari pengguna
poly = get_poly()

# Menampilkan polinomial
print(f"\nPolinomial: {np.poly1d(poly)}\n")

# Menampilkan tabel Routh awal
table = get_table(poly, 1)
print("Tabel Routh Awal:")
print(table)

# Meminta user untuk input nilai K baru
k = float(input("\nMasukkan nilai K: "))

# Menampilkan tabel Routh yang diperbarui
table = get_table(poly, k)
print("\nTabel Routh yang Diperbarui:")
print(table)
