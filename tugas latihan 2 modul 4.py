# Input nilai
kehadiran = float(input("Masukkan total nilai kehadiran: "))
tugas = float(input("Masukkan total nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Hitung total nilai
total_nilai = kehadiran + tugas + uts + uas

# Tentukan grade
if total_nilai >= 90:
    grade = 'A'
elif total_nilai >= 80:
    grade = 'B'
elif total_nilai >= 70:
    grade = 'C'
elif total_nilai >= 60:
    grade = 'D'
else:
    grade = 'E'

# Tampilkan hasil
print("Total nilai Anda adalah", total_nilai)
print("Grade Anda adalah", grade)

