nama = input("Masukkan nama: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))
nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.30) + (nilai_uas * 0.50)

print(f"Nilai akhir {nama} adalah: {nilai_akhir:.2f}")