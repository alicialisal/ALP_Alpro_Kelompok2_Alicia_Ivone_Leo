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

def editkeranjang():
    print("Silahkan edit isi keranjang anda!")
    while True:
        nokeranjang = input("Masukkan no. keranjang yang ingin diedit = ")

        # Pastikan nomor keranjang yang ingin diedit ada dalam database
        adamenu = utils.selectsql("kodemenu", "noauto", nokeranjang, "keranjangplg")[0]
        koderesto = utils.selectsql("koderesto", "noauto", nokeranjang, "keranjangplg")[0]

        if adamenu:
            editjum = int(input(f"Masukkan jumlah baru untuk menu {adamenu} = "))
            
            stokskrg = int(utils.selectsql1("stok", "kodemenu = '" + adamenu + "' and koderesto = '" + koderesto + "'",  "mmenu")[0])
            if editjum > stokskrg:
                print(f"Stok tidak cukup. Sisa stok = {stokskrg}")
                continue
            
            jumsblm = int(utils.selectsql("jumlah", "noauto", nokeranjang, "keranjangplg")[0])
            
            if jumsblm - editjum < 0:
                konfirubah = input(f"Anda yakin menambahkan sebanyak {editjum - jumsblm} pcs untuk menu {adamenu} (Y/N) = ")
            else:
                konfirubah = input(f"Anda yakin mengurangi sebanyak {jumsblm - editjum} pcs untuk menu {adamenu} (Y/N) = ")
            
            if konfirubah.lower() == 'y':
            # Update harga menu untuk kode menu tertentu
                connectsrv.execute("UPDATE keranjangplg SET jumlah = %s WHERE noauto = %s", (editjum, nokeranjang))
                connector.commit()

                print("Successfully updated.")
            else:
                print("Update cancelled.")
        else:
            print(f"No. Keranjang {nokeranjang} tidak ada.")
        
        ulang = input(f"Masih ingin mengedit keranjang anda? (Y/N) = ")
        if ulang.lower() == 'n':
            break

def hapuskeranjang(noauto):
    if (noauto == ""):
        print("Silahkan hapus item dari keranjang anda!")
        while True:
            nokeranjang = input("Masukkan no. keranjang yang ingin diedit = ")

            # Pastikan nomor keranjang yang ingin diedit ada dalam database
            adamenu = utils.selectsql("kodemenu", "noauto", nokeranjang, "keranjangplg")[0]

            if adamenu:
                konfirhapus = input(f"Anda yakin ingin menghapus No. Keranjang {nokeranjang} - Menu {adamenu} (Y/N) = ")
                    # Hapus entri menu berdasarkan kode menu tertentu
                if konfirhapus.lower() == 'y':
                    connectsrv.execute("DELETE FROM keranjangplg WHERE noauto = %s", (nokeranjang,))
                    connector.commit()
                    print("Successfully deleted.")
                else:
                    print("Cancelled.")
            else:
                print(f"No. Keranjang {nokeranjang} tidak ada.")
            
            ulang = input(f"Masih ingin menghapus item dari keranjang anda? (Y/N) = ")
            if ulang.lower() == 'n':
                break
    else:
        # Kueri untuk menghapus pesanan berdasarkan nomor auto
        query = f"DELETE FROM keranjangplg WHERE noauto = {noauto}"
        connectsrv.execute(query)

        # Commit perubahan ke database
        connector.commit()

def autono(formattgl):
    connectsrv.execute(f"SELECT MAX(nokeranjang) FROM tambahstok WHERE LEFT(notambah, 6) = '{formattgl}'")

    noterakhir = connectsrv.fetchone()[0]  # Get the last stored number

    if noterakhir:  # If there's a last stored number
        noterakhir = int(noterakhir[6:])  # Extract the numeric part, assuming it's at positions 6 to end
        nourut = str(noterakhir + 1).zfill(4)  # Increment the number and pad with zeros to 4 digits
    else:
        nourut = "0001"  # If it's the first entry for the day

    notambah = f"{formattgl}{nourut}"  # Create the new 'notambah'

    return notambah

def lihatkeranjang():
    userplg = str(utils.selectsql("nama", "login", "1", "muser")[0])
    # Melakukan query
    query = f"SELECT keranjangplg.KodeResto, KodeMenu, Harga, Jumlah, harga*jumlah as SubTotal, NoAuto as NoKeranjang FROM keranjangplg inner join mresto on keranjangplg.koderesto = mresto.koderesto where userplg = '{userplg}'"
    connectsrv.execute(query)

    # Mendapatkan nama kolom
    columns = [col[0] for col in connectsrv.description]

    # Menampilkan judul
    print("-" * (7 + 15 * len(columns) + 3 * len(columns) - 1))
    judultabel = "List Keranjang Anda"
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

    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    
def lihatlistco(wherenoauto):
    query = f"SELECT UserPlg, KodeResto, KodeMenu, Harga, Jumlah, Harga*Jumlah as SubTotal FROM keranjangplg where {wherenoauto}"
    connectsrv.execute(query)

    # Mendapatkan nama kolom
    columns = [col[0] for col in connectsrv.description]

    # Mendapatkan hasil query
    result = connectsrv.fetchall()

    # Menampilkan judul
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    judultabel = "List Checkout Anda"
    print(judultabel.center(7 + 15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan header kolom
    for col in columns:
        print(f"{col:15}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
    print("\n" + "-" * (15 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

    # Menampilkan isi tabel
    for row in result:
        for col in row:
            print(f"{col:15}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
        print()
    
    # Menghitung total belanja
    total_belanja = sum(row[5] for row in result)

    # Menampilkan garis bawah setelah data
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan informasi total belanja
    print(f"Total Belanja: {total_belanja:15}")

    # Menampilkan garis bawah akhir
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    
    return total_belanja, result
    
def autono(formattgl):
    connectsrv.execute(f"SELECT MAX(nopesanan) FROM pesanan WHERE LEFT(nopesanan, 9) = 'PSN{formattgl}'")

    noterakhir = connectsrv.fetchone()[0]  # Get the last stored number

    if noterakhir:  # If there's a last stored number
        noterakhir = int(noterakhir[6:])  # Extract the numeric part, assuming it's at positions 6 to end
        nourut = str(noterakhir + 1).zfill(4)  # Increment the number and pad with zeros to 4 digits
    else:
        nourut = "0001"  # If it's the first entry for the day

    notambah = f"PSN{formattgl}{nourut}"  # Create the new 'notambah'

    return notambah, int(nourut)
    
def checkout():
    jummenu = 0
    tglhariini = datetime.date.today()
    formattgl = (tglhariini).strftime("%d%m%y")
    listco = []
    while True:
        noauto = int(input("Masukkan No. Keranjang yang ingin di-checkout = "))
        adanoauto = utils.selectsql("noauto", "noauto", noauto, "keranjangplg")
        if adanoauto:
            listco.append(noauto)
            ulang = input("Apakah masih ada menu ingin di-checkout dari keranjang? (Y/N) = ")
            if ulang.lower() == 'n': break
        else: print(f"No. Keranjang {noauto} tidak ada.")
    
    txtwhere = ""
    for i in listco :
        if txtwhere != "":
            txtwhere += f" or noauto = {i}"
        else: txtwhere += f"noauto = {i}"
        
    totalco, keranjangplg = lihatlistco(txtwhere)
        
    konfirmasi = input(f"Anda yakin ingin checkout {len(keranjangplg)} menu ini dengan total Rp. {totalco} ? (Y/N) ")
    
    if konfirmasi.lower() == "y":    
        nopesan, nourutpesan = autono(formattgl)
        for pesanan in keranjangplg:
            query = f"INSERT INTO pesanandet (nopesanan, kode, jumlah, harga) VALUES ('{nopesan}', '{pesanan[2]}', {pesanan[4]}, {pesanan[3]})"
            connectsrv.execute(query)
        
        connectsrv.execute(f"INSERT INTO pesanan (nopesanan, tgl, plg, koderesto, nourutpesan) VALUES ('{nopesan}', '{tglhariini}', '{pesanan[0]}', '{pesanan[1]}', {nourutpesan})")
        connector.commit()
        
        for noauto in listco:
            hapuskeranjang(noauto)
        
        jamtutupresto = str(utils.selectsql("jamtutup", "koderesto", pesanan[1], "mresto")[0])
        print(f"Pesanan dengan nomor pesanan = {nopesan} berhasil dibuat.\nNomor urut anda = {nourutpesan}.\nSilahkan datang ke restoran untuk mengambil pesanan anda sebelum jam {jamtutupresto}.")

        connectsrv.execute(f"update mmenu t, (select pesanan.KodeResto, KodeMenu, jumlah as totjual from pesanandet inner join pesanan on pesanan.NoPesanan = pesanandet.NoPesanan inner join mmenu on pesanandet.Kode = mmenu.KodeMenu where pesanan.NoPesanan = '{nopesan}' group by pesanan.NoPesanan, pesanandet.Kode) as s set t.Stok = t.Stok - s.totjual where t.KodeMenu = s.Kodemenu and t.KodeResto = s.KodeResto")
        connector.commit()
    else:
        print(f"Checkout dibatalkan. Anda akan diarahkan kembali ke menu utama.")

def main():
    lihatkeranjang()
    while True:
        menu = "\nPilihan menu: \n1. Edit Isi Keranjang\n2. Hapus Menu dari Keranjang\n3. Lihat isi keranjang\n4. Kembali Ke Menu Utama"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses (1-4) = "))
        if (pilihanmenu == 1): 
            editkeranjang()
        elif (pilihanmenu == 2): 
            hapuskeranjang("")
        elif (pilihanmenu == 3): 
            lihatkeranjang()
            pilihanco = input("\nApakah anda ingin checkout keranjang? (Y/N) = ")
            if pilihanco.lower() == 'y':
                checkout()
        elif (pilihanmenu == 4): 
            import mainplg
            mainplg.main()

main()

