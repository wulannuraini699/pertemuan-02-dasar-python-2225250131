print("Masukkan koordinat Titik A:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("\nMasukkan koordinat Titik B:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Menghitung perubahan koordinat dx dan dy
dx = x2 - x1
dy = y2 - y1

# Menghitung jarak Euclidean tanpa pustaka eksternal (math)
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# Menghitung titik tengah
titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

# Menampilkan hasil dengan presisi dua angka desimal
print("\nRingkasan Koordinat")
print(f"Titik A       : ({x1:.2f}, {y1:.2f})")
print(f"Titik B       : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan     : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak         : {jarak:.2f}")
print(f"Titik Tengah  : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")