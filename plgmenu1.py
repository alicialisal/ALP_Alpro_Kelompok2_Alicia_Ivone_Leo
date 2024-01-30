import mysql.connector
import utils

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "foodwaste"
)
connectsrv = connector.cursor()

def lihatstokmenu():
    while True:
        # Melakukan query
        query = "SELECT * FROM mmenu"
        connectsrv.execute(query)

        # Mendapatkan nama kolom
        columns = [col[0] for col in connectsrv.description]

        # Mendapatkan hasil query
        result = connectsrv.fetchall()

        # Menampilkan judul
        print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))
        judultabel = "List Menu"
        print(judultabel.center(7 + 15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
        print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))

        # Menampilkan header kolom
        print(f"{'No':<5}", end=" | ")
        for col in columns:
            print(f"{col:15}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
        print("\n" + "-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

        # Menampilkan isi tabel
        for i, row in enumerate(result, start=1):
            print(f"{i:<5}", end=" | ")  # Menampilkan nomor urut
            for col in row:
                print(f"{col:15}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
            print()

        print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))
        konfirmasi = input(f"\nKembali ke Menu Utama? (Y/N) ")
        if (konfirmasi.lower() == 'y'):
            break
    main()
    
def lihatresto(syarat):
    # Melakukan query
    query = f"SELECT * FROM mresto where kategori like '{syarat}'"
    connectsrv.execute(query)

    # Mendapatkan nama kolom
    columns = [col[0] for col in connectsrv.description]

    # Mendapatkan hasil query
    result = connectsrv.fetchall()

    # Menampilkan judul
    print("-" * (7 + 20 * len(columns) + 3 * len(columns) - 1))
    judultabel = "List Restoran"
    print(judultabel.center(7 + 15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
    print("-" * (7 + 20 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan header kolom
    print(f"{'No':<5}", end=" | ")
    for col in columns:
        print(f"{col:20}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
    print("\n" + "-" * (7 + 20 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

    # Menampilkan isi tabel
    for i, row in enumerate(result, start=1):
        print(f"{i:<5}", end=" | ")  # Menampilkan nomor urut
        for col in row:
            print(f"{str(col):20}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
        print()

    print("-" * (7 + 20 * len(columns) + 3 * len(columns) - 1))

def lihatmenu():
    import utils
    konfirmasielse = None
    konfirmasiif = None
    while True:
        filterkoderesto = input("Masukkan kode restoran yang ingin anda lihat menunya = ")
        adaresto = (utils.selectsql("*", "koderesto", filterkoderesto, "mresto"))
        if adaresto:
            # Melakukan query
            query = f"SELECT KodeMenu, NamaMenu, Stok, HargaMenu FROM mmenu where koderesto = '{filterkoderesto}' and stok > 0"
            connectsrv.execute(query)

            # Mendapatkan nama kolom
            columns = [col[0] for col in connectsrv.description]

            # Mendapatkan hasil query
            result = connectsrv.fetchall()

            # Menampilkan judul
            print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))
            judultabel = "List Menu"
            print(judultabel.center(7 + 15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
            print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))

            # Menampilkan header kolom
            print(f"{'No':<5}", end=" | ")
            for col in columns:
                print(f"{col:15}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
            print("\n" + "-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

            # Menampilkan isi tabel
            for i, row in enumerate(result, start=1):
                print(f"{i:<5}", end=" | ")  # Menampilkan nomor urut
                for col in row:
                    print(f"{col:15}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
                print()

            print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))
            konfirmasiif = int(input(f"\nApakah anda ingin membeli dari restoran ini?\n1. Ya\n2. Tidak, saya ingin melihat menu restoran lain\nPilihan anda (1/2) = "))
            if (konfirmasiif == 1):
                break
        else:
            konfirmasielse = int(input(f"\nRestoran {filterkoderesto} tidak ada. Apakah anda ingin melihat menu restoran lain?\n1. Ya\n2. Tidak, saya ingin kembali ke menu sebelumnya\nPilihan anda (1/2) = "))
            if (konfirmasielse == 1):
                continue
            else: break
    if konfirmasiif:
        if konfirmasiif == 1:
            utils.tambahkeranjang(filterkoderesto)
    elif konfirmasielse:
        if konfirmasielse == 2:
            main()

def selectsql(kolomselect, kolomwhere, syaratwhere):
    query = f"SELECT {kolomselect} FROM muser where {kolomwhere} = {syaratwhere}"
    connectsrv.execute(query)

    # Mengambil semua baris hasil query
    hasil = connectsrv.fetchall()

    # Menampilkan atau mengembalikan nilai username
    hasilselect = [data[0] for data in hasil]  # Ambil kolom pertama (username)
    return hasilselect

def filterkat():
    utils.lihatkat()
    kategori = ""
    jumkat = 0
    while True:
        kodekat = input(f"\nMasukkan kode kategori restoran yang ingin dicari (1-19) = ")
        selectkat = str(utils.selectsql("kategori", "kode", kodekat, "mkategori")[0])
        konfirmasi = input(f"\nKategori yang anda pilih = {selectkat}\nAnda yakin ingin mencari kategori tersebut? (Y/N) ")
        if konfirmasi.lower() == 'n': continue
        else :
            kategori += "%%" + selectkat + "%%"
        tambahkat = input(f"\nMasih ingin menambahkan filter untuk kategori lain? (Y/N) ")
        jumkat += 1
        if (tambahkat.lower() == 'y'):
            if jumkat < 3:
                kategori += " and kategori = "
            else: 
                print("! MAKSIMAL 3 KATEGORI !")
                break
        else: break
    return kategori

def main():
    while True:
        menu = "\n1. Lihat Semua Restoran\n2. Lihat Restoran Berdasarkan Kategori\n3. Kembali ke menu utama"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses = "))
        if (pilihanmenu == 1): 
            lihatresto('%%%%')
            lihatmenu()
        elif (pilihanmenu == 2): 
            while True:
                syaratkat = filterkat()
                lihatresto(syaratkat)
                konfirmasi = int(input(f"\nApakah anda ingin mencari lagi?\n1. Ya\n2. Tidak, saya sudah menemukan restoran\nPilihan anda (1/2) = "))
                if (konfirmasi == 2):
                    break
            lihatmenu()
        else : 
            import mainplg as plg
            plg.main()

main()