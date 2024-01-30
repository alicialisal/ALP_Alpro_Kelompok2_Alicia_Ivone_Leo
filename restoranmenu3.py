import mysql.connector
import utils

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "foodwaste"
)
connectsrv = connector.cursor()
    
def lihatpesanan():
    # Melakukan query
    query = f"SELECT pesanandet.NoPesanan, Kode, mmenu.NamaMenu, pesanandet.Jumlah, pesanandet.Harga, pesanan.NoUrutPesan FROM pesanan inner join pesanandet on pesanan.nopesanan = pesanandet.nopesanan inner join mmenu on (pesanandet.Kode = mmenu.kodemenu and pesanan.KodeResto = mmenu.KodeResto) where pesanan.koderesto = '{koderesto}' and status = 0"
    connectsrv.execute(query)

    # Mendapatkan nama kolom
    columns = [col[0] for col in connectsrv.description]

    # Menampilkan judul
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    judultabel = "List Pesanan"
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

def selectsql(kolomselect, kolomwhere, syaratwhere):
    query = f"SELECT {kolomselect} FROM muser where {kolomwhere} = {syaratwhere}"
    connectsrv.execute(query)

    # Mengambil semua baris hasil query
    hasil = connectsrv.fetchall()

    # Menampilkan atau mengembalikan nilai username
    hasilselect = [data[0] for data in hasil]  # Ambil kolom pertama (username)
    return hasilselect

def updatestatus():
    global koderesto
    print("Silahkan update status pesanan restoran anda!")
    while True:
        nourutpsn = int(input("Masukkan no. urut pesanan yang ingin di-update statusnya = "))

        # Pastikan kode menu yang ingin diedit ada dalam database
        adapesanan = utils.selectsql("*", "nourutpesan", nourutpsn, "pesanan")

        if adapesanan:
            connectsrv.execute("UPDATE pesanan SET status = 1 WHERE nourutpesan = %s and koderesto = %s", (nourutpsn, koderesto))
            connector.commit()

            print("Status updated.")
        else:
            print(f"No. Urut {nourutpsn} tidak ada.")
        
        ulang = input("Apakah masih ada pesanan yang ingin di-update statusnya? (Y/N) = ")
        if ulang.lower() == 'n': break

def main():
    global koderesto
    userresto = str(utils.selectsql("nama", "login", "1", "muser")[0])
    koderesto = str(utils.selectsql("koderestoplg", "nama", userresto, "muser")[0])
    while True:
        menu = "\n1. Lihat Pesanan\n2. Update Status Pesanan\n3. Kembali ke Menu Utama"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses (1-3)= "))
        if (pilihanmenu == 1): lihatpesanan()
        elif (pilihanmenu == 2): updatestatus()
        elif (pilihanmenu == 3): 
            import mainrestoran as resto
            resto.utama()

koderesto = ""            
main()
