# Input total belanja
total_belanja = float(input("Masukkan total belanja: "))

# Cek apakah total belanja mencapai Rp. 250.000
if total_belanja >= 250000:
    # Hitung diskon
    diskon = total_belanja * 50 / 100
    print("Selamat! Anda mendapatkan diskon sebesar Rp.", diskon)
else:
    print("Maaf, Anda tidak menerima diskon karena total belanjaan tidak mencapai Rp. 250.000")
    print("Total belanjaan Anda adalah Rp.", total_belanja)