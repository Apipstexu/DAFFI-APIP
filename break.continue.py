# Contoh break - berhenti saat bertemu angka 5
for i in range(1, 11):
    if i == 5:
        break          # keluar dari loop 
    print(i, end=" ")
# Output: 1 2 3 4

# Contoh continue - lewati angka GENAP
for i in range(1, 11):
    if i % 2 == 0:
        continue       # lewati iterasi ini
    print(i, end=" ")  # Cetak angka ganjil saja
# Output: 1 3 5 7 9