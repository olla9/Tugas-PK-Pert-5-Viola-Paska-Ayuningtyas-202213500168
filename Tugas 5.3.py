def hitung_ips():
    # Input jumlah mata kuliah
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))
    
    # Inisialisasi total nilai dan total bobot
    total_nilai = 0
    total_bobot = 0
    
    # Loop untuk setiap mata kuliah
    for i in range(jumlah_mata_kuliah):
        nilai = input(f"Masukkan nilai untuk mata kuliah ke-{i + 1} (A/B/C/D): ").upper()
        
        # Menentukan bobot nilai berdasarkan input
        if nilai == 'A':
            bobot = 4.0
        elif nilai == 'B':
            bobot = 3.0
        elif nilai == 'C':
            bobot = 2.0
        elif nilai == 'D':
            bobot = 1.0
        else:
            print("Nilai tidak valid. Silakan masukkan A, B, C, atau D.")
            continue
        
        # Menambahkan bobot ke total
        total_nilai += bobot
        total_bobot += 1  # Setiap mata kuliah memiliki bobot 1
        
    # Menghitung IPS
    if total_bobot > 0:
        ips = total_nilai / total_bobot
        print(f"Indeks Prestasi Semester (IPS) Anda adalah: {ips:.2f}")
    else:
        print("Tidak ada mata kuliah yang dihitung.")

# Memanggil fungsi untuk menjalankan program
hitung_ips()
