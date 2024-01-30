import mysql.connector
import datetime
import utils

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "foodwaste"
)
connectsrv = connector.cursor()

def autono(formattgl):
    connectsrv.execute(f"SELECT MAX(notambah) FROM tambahstok WHERE LEFT(notambah, 6) = '{formattgl}'")

    noterakhir = connectsrv.fetchone()[0]  # Get the last stored number

    if noterakhir:  # If there's a last stored number
        noterakhir = int(noterakhir[6:])  # Extract the numeric part, assuming it's at positions 6 to end
        nourut = str(noterakhir + 1).zfill(4)  # Increment the number and pad with zeros to 4 digits
    else:
        nourut = "0001"  # If it's the first entry for the day

    notambah = f"{formattgl}{nourut}"  # Create the new 'notambah'

    return notambah

def lihatlisttambahstok(keranjangplg):
    # Mendapatkan nama kolom
    columns = ['NoTambah', 'KodeMenu', 'Stok Hari Ini']

    # Menampilkan judul
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    judultabel = "List Penambahan Stok Anda"
    print(judultabel.center(15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan header kolom
    for col in columns:
        print(f"{col:15}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
    print("\n" + "-" * (15 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

    # Menampilkan isi tabel
    for row in keranjangplg:
        for col in row:
            print(f"{col:15}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
        print()

    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

def tambahstok():
    userresto = str(utils.selectsql("nama", "login", "1", "muser")[0])
    koderesto = str(utils.selectsql("koderestoplg", "nama", userresto, "muser")[0])
    arraymenu = []
    jummenu = 0
    tglhariini = datetime.date.today()
    formattgl = (tglhariini).strftime("%d%m%y")

    notambah = autono(formattgl)

    connectsrv.execute(f"INSERT INTO tambahstok (notambah, tgl, opr, koderesto) VALUES ('{notambah}', '{tglhariini}', '{userresto}', '{koderesto}')")

    print("Silahkan tambahkan stok pada menu anda!")
    ulang = True
    while ulang == True:
        # Edit data dengan kode menu sebagai syarat where
        kodemenu = input("Masukkan kode menu makanan yang ingin ditambahkan stoknya = ")

        # Cek apakah kode menu ada dalam database
        adamenu = utils.selectsql("*", "kodemenu", kodemenu, "mmenu")
        
        row = []
        if adamenu:
            for j in range (3):
                if (j == 0):
                    row.append(f"{notambah}")
                elif (j == 1):
                    row.append(kodemenu)
                elif (j == 2):
                    row.append(input(f"Masukkan stok menu makanan hari ini = "))
            arraymenu.append(row)
            jummenu += 1
        else : 
            print(f"Kode menu {kodemenu} tidak ada.")
        cekulang = input(f"Masih ingin menambah stok menu lain? (Y/N) ")
        if cekulang.lower() == "n":
            break      
    
    if len(arraymenu) > 0:
        print("List penambahan stok anda: ")
        lihatlisttambahstok(arraymenu)

        konfirmasi = input(f"Anda yakin ingin menambah stok untuk {jummenu} menu ini? (Y/N) ")
        if konfirmasi.lower() == "y":
            for i in arraymenu:
                connectsrv.execute('''INSERT INTO tambahstokdet (notambah, kodemenu, jumlah) VALUES (%s, %s, %s)''', i)

        connector.commit()
        
        utils.updatestok()

        print(connectsrv.rowcount, "menu telah ditambahkan stoknya.")

def main():
    global koderesto
    username = str(utils.selectsql("nama", "login", "1", "muser")[0])
    koderesto = str(utils.selectsql("koderestoplg", "nama", username, "muser")[0])
    while True:
        utils.lihatmenu(koderesto, "KodeMenu, NamaMenu, Stok")
        menu = "\n1. Tambahkan stok makanan sisa\n2. Kembali ke Menu Utama"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses (1/2) = "))
        if (pilihanmenu == 1): 
            tambahstok()
            utils.updatestok()
        elif (pilihanmenu == 2): 
            import mainrestoran as resto
            resto.utama()

main()