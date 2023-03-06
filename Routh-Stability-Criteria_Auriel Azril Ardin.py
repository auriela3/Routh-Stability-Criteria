import numpy as np


def get_poly():
    poly = input("Masukkan koefisien polinomial: ")
    poly = poly.split()
    poly = [float(p) for p in poly]
    return poly


def get_table(poly, k):
    num_rows = len(poly)//2 + len(poly) % 2
    num_cols = len(poly) - 1

    table = np.zeros((num_rows, num_cols))
    table[0, :] = poly[::2]
    table[1, :] = poly[1::2]

    for i in range(2, num_rows):
        for j in range(num_cols):
            if table[i-1, 0] == 0:
                table[i, j] = 0
            else:
                table[i, j] = ((table[i-1, 0]*table[i-2, j+1]) -
                               (table[i-2, 0]*table[i-1, j+1])) / table[i-1, 0]

    table[0, 0] += k
    return table


poly = get_poly()
print(f"\nPolinomial: {np.poly1d(poly)}\n")

table = get_table(poly, 1)
print("Tabel Routh Awal:")
print(table)

k = float(input("\nMasukkan nilai K: "))

table = get_table(poly, k)
print("\nTabel Routh yang Diperbarui:")
print(table)
