def hitung_biaya_pengiriman(panjang, lebar, tinggi, berat):
    # Biaya untuk paket kecil dan besar
    biaya_per_kg_kecil = 5000
    biaya_per_kg_besar = 7000
    tambahan_biaya_besar = 50000
    biaya_minimal = 8000

    # Cek dimensi paket
    if panjang < 50 and lebar < 50 and tinggi < 50:
        biaya = max(biaya_per_kg_kecil * berat, biaya_minimal)
    else:
        biaya = max(biaya_per_kg_besar * berat + tambahan_biaya_besar, biaya_minimal)

    return biaya

# Input dari user
try:
    lokasi = input("Masukkan lokasi pengiriman (Kota/Kabupaten Pasuruan): ").strip().lower()
    if lokasi not in ["kota pasuruan", "kabupaten pasuruan"]:
        print("Maaf, layanan hanya tersedia di Kota dan Kabupaten Pasuruan.")
    else:
        panjang = float(input("Masukkan panjang paket (cm): "))
        lebar = float(input("Masukkan lebar paket (cm): "))
        tinggi = float(input("Masukkan tinggi paket (cm): "))
        berat = float(input("Masukkan berat paket (kg): "))

        if panjang <= 0 or lebar <= 0 or tinggi <= 0 or berat <= 0:
            print("Dimensi dan berat harus lebih dari 0.")
        else:
            biaya = hitung_biaya_pengiriman(panjang, lebar, tinggi, berat)
            print(f"Biaya pengiriman adalah: Rp {biaya}")
except ValueError:
    print("Harap masukkan angka yang valid untuk dimensi dan berat!")
