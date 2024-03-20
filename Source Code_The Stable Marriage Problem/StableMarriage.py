def stableMarriageProblem(pilihan_pria, pilihan_wanita):
    n = len(pilihan_pria)

    # Inisialisasi pencocokan semua orang menjadi None
    pencocokan_pria = [None] * n
    pencocokan_wanita = [None] * n

    # Inisialisasi array untuk melacak langkah terakhir pria
    langkah_terakhir = [0] * n

    # Fungsi untuk menentukan peringkat wanita dalam pilihan pria
    def peringkat_wanita(pria, wanita):
        return pilihan_pria[pria].index(wanita)

    # Fungsi untuk mengecek apakah ada pria yang belum cocok
    def ada_pria_belum_cocok():
        return None in pencocokan_pria

    # Fungsi untuk memilih pria yang belum cocok
    def pilih_pria_belum_cocok():
        return pencocokan_pria.index(None)

    # Iterasi sampai semua pria mendapat pasangan
    while ada_pria_belum_cocok():
        pria = pilih_pria_belum_cocok()  # Pria yang belum mendapat pasangan

        # Pilih wanita sesuai pilihan pria
        wanita = pilihan_pria[pria][langkah_terakhir[pria]]
        langkah_terakhir[pria] += 1  # Pindahkan langkah pria ke wanita berikutnya

        if pencocokan_wanita[wanita] is None:  # Jika wanita belum tercocokkan
            pencocokan_pria[pria] = wanita
            pencocokan_wanita[wanita] = pria
        else:
            pria_terdahulu = pencocokan_wanita[wanita]  # Pria yang sebelumnya cocok dengan wanita ini
            if peringkat_wanita(pria, wanita) < peringkat_wanita(pria_terdahulu, wanita):
                # Pria saat ini lebih disukai oleh wanita
                pencocokan_pria[pria] = wanita
                pencocokan_pria[pria_terdahulu] = None  # Pria sebelumnya menjadi tidak cocok
                pencocokan_wanita[wanita] = pria

    return pencocokan_pria


# Contoh pemanggilan fungsi
pilihan_pria = [[1, 0], [0, 1]]
pilihan_wanita = [[0, 1], [1, 0]]
hasil_pencocokan = stableMarriageProblem(pilihan_pria, pilihan_wanita)
print("Hasil Pencocokan:")
for i, pasangan in enumerate(hasil_pencocokan):
    print("Pria", i, "dengan Wanita", pasangan)
