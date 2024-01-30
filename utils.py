import mysql.connector
import datetime

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "foodwaste"
)
connectsrv = connector.cursor()

def selectsql(kolomselect, kolomwhere, syaratwhere, tabel):
    connector = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "",
        database = "foodwaste"
    )
    connectsrv = connector.cursor()
    
    query = f"SELECT {kolomselect} FROM {tabel} where {kolomwhere} = '{syaratwhere}'"
    connectsrv.execute(query)

    # Mengambil semua baris hasil query
    hasil = connectsrv.fetchone()

    # Menampilkan atau mengembalikan nilai username
    return hasil

def selectsql1(kolomselect, syaratwhere, tabel):
    query = f"SELECT {kolomselect} FROM {tabel} where {syaratwhere}"
    connectsrv.execute(query)

    # Mengambil semua baris hasil query
    hasil = connectsrv.fetchone()

    # Menampilkan atau mengembalikan nilai username
    return hasil

def simpanuser(ambiluser):
    if ambiluser == "":
        return useraktif
    else :
        useraktif = ambiluser
        
def lihatmenu(koderesto, selectkolom):
    connector = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "",
        database = "foodwaste"
    )
    connectsrv = connector.cursor()
    # Melakukan query
    query = f"SELECT {selectkolom} FROM mmenu where koderesto = '{koderesto}'"
    connectsrv.execute(query)

    # Mendapatkan nama kolom
    columns = [col[0] for col in connectsrv.description]

    # Mendapatkan hasil query
    result = connectsrv.fetchall()

    # Menampilkan judul
    print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))
    judultabel = "List Menu Anda"
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
        
def lihatlist(columns, listarray, judultabel):
    # Menampilkan judul
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    print(judultabel.center(15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan header kolom
    for col in columns:
        print(f"{col:15}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
    print("\n" + "-" * (15 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

    # Menampilkan isi tabel
    for row in listarray:
        for col in row:
            print(f"{col:15}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
        print()

    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
        
def tambahkeranjang(koderesto):
    jumkeranjang = 0
    userplg = str(selectsql("nama", "login", "1", "muser")[0])
    kodeplg = str(selectsql("koderestoplg", "nama", userplg, "muser")[0])
    arraykeranjang = []
    print("Silahkan tambahkan menu ke keranjang anda!")
    ulang = True
    while ulang == True:
        # Edit data dengan kode menu sebagai syarat where
        kodemenu = input("Masukkan kode menu makanan yang ingin dimasukkan ke keranjang = ")

        # Cek apakah kode menu ada dalam database
        adakeranjang = selectsql1("*", "kodemenu = '" + kodemenu + "' and koderesto = '" + koderesto + "' and userplg = '" + kodeplg + "'", "keranjangplg")
        
        adamenu = selectsql1("*", "kodemenu = '" + kodemenu + "' and koderesto = '" + koderesto + "' and stok > 0", "mmenu")
        
        row = []
        if (adakeranjang == "" or adakeranjang is None) and (adamenu is not None and adamenu != ""):
            for j in range (5):
                if (j == 0):
                    row.append(userplg)
                elif (j == 1):
                    row.append(koderesto)
                elif (j == 2):
                    row.append(kodemenu)
                elif (j == 3):
                    row.append(int(selectsql1("hargamenu", "kodemenu = '" + kodemenu + "' and koderesto = '" + koderesto + "'",  "mmenu")[0]))
                elif (j == 4):
                    while True:
                        if len(row) == 5:
                            row[4] = int(input(f"Masukkan jumlah menu makanan yang ingin dibeli = "))
                        else:
                            row.append(int(input(f"Masukkan jumlah menu makanan yang ingin dibeli = ")))
                        jumbeli = int(row[4])
                        stokskrg = int(selectsql1("stok", "kodemenu = '" + kodemenu + "' and koderesto = '" + koderesto + "'",  "mmenu")[0])
                        if jumbeli > stokskrg:
                            print(f"Stok tidak cukup. Sisa stok = {stokskrg}")
                            continue
                        else: break
                else: 
                    row.append(kodeplg)
            arraykeranjang.append(row)
        elif (adamenu is None or adamenu == ""): 
            print(f"Kode menu {kodemenu} tidak ada / tidak tersedia.")
        cekulang = input(f"Masih ingin menambah menu lain ke keranjang? (Y/N) ")
        if cekulang.lower() == "n":
            break      

    #print("List penambahan keranjang anda: ")
    columns = ['UserPlg', 'KodeResto', 'KodeMenu', 'Harga', 'Jumlah']
    lihatlist(columns, arraykeranjang, "List penambahan keranjang anda")

    konfirmasi = input(f"Anda yakin ingin menyimpan list diatas ke keranjang anda? (Y/N) ")
    if konfirmasi.lower() == "y":
        for i in arraykeranjang:
            jumkeranjang += 1
            connectsrv.execute('''INSERT INTO keranjangplg (userplg, koderesto, kodemenu, harga, jumlah) VALUES (%s, %s, %s, %s, %s)''', i)
    
    #connectsrv.execute(f"update mmenu t, (select KodeMenu, sum(jumlah) as totjual from  inner join tambahstokdet on tambahstok.NoTambah = tambahstokdet.NoTambah where tambahstok.Tgl = '{tglhariini}' group by tambahstok.Tgl) as s set t.Stok = s.totstok where t.KodeMenu = s.Kodemenu")

    connector.commit()

    print(jumkeranjang, " menu telah ditambahkan ke keranjang anda.")

def lihatkat():
    # Melakukan query
    query = "SELECT * FROM mkategori"
    connectsrv.execute(query)

    # Mendapatkan nama kolom
    columns = [col[0] for col in connectsrv.description]
    
    # Menampilkan judul
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    judultabel = "List Kategori Restoran"
    print(judultabel.center(15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan header kolom
    for col in columns:
        print(f"{col:15}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
    print("\n" + "-" * (15 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

    # Menampilkan isi tabel
    for row in connectsrv.fetchall():
        for col in row:
            print(f"{col:15}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
        print()

    # Menampilkan garis bawah
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    
def updatestok():
    connector = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "",
        database = "foodwaste"
    )
    connectsrv = connector.cursor()
    
    tglhariini = datetime.date.today()
    
    query = f"update mmenu t, (select KodeResto, KodeMenu, sum(jumlah) as totstok from tambahstok inner join tambahstokdet on tambahstok.NoTambah = tambahstokdet.NoTambah where tambahstok.Tgl = '{tglhariini}' group by tambahstok.Tgl, tambahstokdet.KodeMenu, tambahstok.KodeResto) as s set t.Stok = s.totstok where t.KodeMenu = s.Kodemenu and t.KodeResto = s.KodeResto"
    connectsrv.execute(query)
    connector.commit()
    
    # def updatestok():
    # try:
    #     # Assume 'connectsrv' is your MySQL connection object
    #     connectsrv = connectsrv.cursor()

    #     tglhariini = "2024-01-11"  # Replace with the actual date

    #     # Fetch the results before executing another query
    #     connectsrv.execute(f"SELECT KodeMenu, sum(jumlah) as totstok FROM tambahstok INNER JOIN tambahstokdet ON tambahstok.NoTambah = tambahstokdet.NoTambah WHERE tambahstok.Tgl = '{tglhariini}' GROUP BY tambahstok.Tgl")
    #     results = connectsrv.fetchall()  # Fetch all results

    #     # Update 'mmenu' table based on the fetched results
    #     for result in results:
    #         kode_menu = result['KodeMenu']
    #         total_stok = result['totstok']
    #         connectsrv.execute(f"UPDATE mmenu SET Stok = {total_stok} WHERE KodeMenu = '{kode_menu}'")

    #     # Commit the changes
    #     connectsrv.commit()

    # except mysql.connector.Error as err:
    #     print(f"Error: {err}")

    # finally:
    #     # Close the cursor
    #     connectsrv.close()