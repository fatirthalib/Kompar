import numpy as np

# 1. Menyiapkan data A dan B (seperti A1-A4 dan B1-B4 di gambar)
# NumPy menyimpan data ini dalam blok memori yang berurutan
A = np.array([10, 20, 30, 40])
B = np.array([5, 15, 25, 35])

# 2. Instruksi: C = A + B
# Di balik layar, NumPy memicu instruksi SIMD pada CPU (seperti AVX atau SSE)
# Ini mengeksekusi A1+B1, A2+B2, dst. secara paralel, bukan satu per satu.
C = A + B

# Menampilkan hasil
print(f"Array A: {A}")
print(f"Array B: {B}")
print(f"Hasil C: {C}") # Output: [15 35 55 75]