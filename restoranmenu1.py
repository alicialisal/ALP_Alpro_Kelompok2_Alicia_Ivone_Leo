import mysql.connector
import utils

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "foodwaste"
)
connectsrv = connector.cursor()

def tambahmenu():
    arraymenu = []
    jummenu = 0
    print("Silahkan masukkan menu baru!")
    ulang = int(input("Berapa menu yang ingin ditambahkan = "))
    while len(arraymenu) < ulang:
        # Edit data dengan kode menu sebagai syarat where
        kodemenu = input("Masukkan kode menu makanan yang ingin ditambahkan = ")

        # Cek apakah kode menu ada dalam database
        adamenu = utils.selectsql1("*", "kodemenu = '" + kodemenu + "' and koderesto = '" + koderesto + "'", "mmenu")

        row = []
        if (adamenu is None or adamenu == ""):
            for j in range (4):
                if (j == 0):
                    row.append(kodemenu)
                elif (j == 1):
                    row.append(input(f"Masukkan nama menu makanan = "))
                elif (j == 2):
                    row.append(int(input(f"Masukkan harga menu makanan = ")))
                else : row.append(koderesto)
            arraymenu.append(row)
            jummenu += 1
        else:
            print(f"Kode {kodemenu} sudah ada.")

    columns = ['Kode Menu', 'Nama Menu', 'Harga Menu', 'Kode Resto']
    utils.lihatlist(columns, arraymenu, "List penambahan menu")

    konfirmasi = input(f"Anda yakin ingin menyimpan {jummenu} menu ini? (Y/N) ")
    if konfirmasi.lower() == "y":
        for i in arraymenu:
            connectsrv.execute('''INSERT INTO mmenu (kodemenu, namamenu, hargamenu, koderesto) VALUES (%s, %s, %s, %s)''', i)

    connector.commit()

    print(connectsrv.rowcount, "menu inserted.")

def editmenu():
    print("Silahkan edit menu yang sudah ada!")
    ulang = int(input("Berapa menu yang ingin diedit = "))
    for i in range (ulang):
        # Misalkan Anda ingin mengedit harga dari suatu menu berdasarkan kode menu
        kodemenu = input("Masukkan kode menu makanan yang ingin diedit = ")

        # Pastikan kode menu yang ingin diedit ada dalam database
        adamenu = utils.selectsql("*", "kodemenu", kodemenu, "mmenu")

        if adamenu:
            edithrg = int(input("Masukkan harga menu makanan yang baru = "))

            # Update harga menu untuk kode menu tertentu
            connectsrv.execute("UPDATE mmenu SET hargamenu = %s WHERE kodemenu = %s", (edithrg, kodemenu))
            connector.commit()

            print(connectsrv.rowcount, "menu updated.")
        else:
            print(f"Kode menu {kodemenu} tidak ada.")


def hapusmenu():
    print("Silahkan hapus menu yang ada!")
    ulang = int(input("Berapa menu yang ingin dihapus = "))
    for i in range (ulang):
        # Misalkan Anda ingin menghapus entri menu berdasarkan kode menu
        kodemenu = input("Masukkan kode menu makanan yang ingin dihapus = ")

        # Pastikan kode menu yang ingin dihapus ada dalam database
        adamenu = utils.selectsql("*", "kodemenu", kodemenu, "mmenu")

        if adamenu:
            # Hapus entri menu berdasarkan kode menu tertentu
            connectsrv.execute("DELETE FROM mmenu WHERE kodemenu = %s", (kodemenu,))
            connector.commit()

            print(connectsrv.rowcount, "menu deleted.")
        else:
            print(f"Kode menu {kodemenu} tidak ada.")

def main():
    global koderesto
    username = str(utils.selectsql("nama", "login", "1", "muser")[0])
    koderesto = str(utils.selectsql("koderestoplg", "nama", username, "muser")[0])
    while True:
        menu = "\nPilihan Menu:\n1. Tambahkan menu makanan\n2. Edit Menu Makanan\n3. Hapus Menu Makanan\n4. Lihat Daftar Menu\n5. Kembali ke menu utama"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses = "))
        if (pilihanmenu == 1): tambahmenu()
        elif (pilihanmenu == 2): editmenu()
        elif (pilihanmenu == 3): hapusmenu()
        elif (pilihanmenu == 4): 
            utils.lihatmenu(koderesto, "KodeMenu, NamaMenu, Stok, HargaMenu")
        else : 
            import mainrestoran as resto
            resto.utama()

koderesto = ""
main()