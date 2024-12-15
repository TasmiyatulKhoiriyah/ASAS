def hitung_biaya_parkir(jam):
    tarif_awal = 3000
    tarif_tambahan_per_jam = 1500
    biaya_lebih_24_jam = 10000

    # Jika parkir 2 jam atau kurang
    if jam <= 2:
        return tarif_awal
    else:
        # Menghitung biaya untuk lebih dari 2 jam
        total = tarif_awal + (jam - 2) * tarif_tambahan_per_jam
        
        # Tambahan biaya jika lebih dari 24 jam
        if jam > 24:
            total += biaya_lebih_24_jam
        
        return total

# Input durasi parkir dari user
try:
    jam_parkir = int(input("Masukkan durasi parkir (jam): "))
    if jam_parkir < 0:
        print("Durasi parkir tidak bisa negatif.")
    else:
        biaya = hitung_biaya_parkir(jam_parkir)
        print(f"Biaya parkir untuk {jam_parkir} jam adalah: Rp {biaya}")
except ValueError:
    print("Harap masukkan angka yang valid!")
