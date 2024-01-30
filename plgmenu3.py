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
    
def lihatlistpesanan(kodeplg, tglawal, tglakhir, filterkode):
    query = f"SELECT pesanan.NoPesanan, pesanan.Tgl, pesanan.KodeResto, pesanandet.Kode, mmenu.NamaMenu, pesanandet.Jumlah, pesanandet.Harga, pesanandet.Harga*pesanandet.Jumlah as SubTotal FROM pesanan inner join pesanandet on pesanan.nopesanan = pesanandet.nopesanan inner join mmenu on pesanandet.kode = mmenu.kodemenu and pesanan.koderesto = mmenu.koderesto where pesanan.plg = '{kodeplg}' and pesanan.tgl >= '{tglawal}' and pesanan.tgl <= '{tglakhir}' and pesanandet.kode like '{filterkode}' order by pesanan.tgl"
    connectsrv.execute(query)

    # Mendapatkan nama kolom
    columns = [col[0] for col in connectsrv.description]

    # Mendapatkan hasil query
    result = connectsrv.fetchall()

    # Menampilkan judul
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    judultabel = "Histori Pesanan Anda"
    print(judultabel.center(7 + 15 * len(columns) + 3 * len(columns) - 1))  # Menampilkan judul yang terpusat
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan header kolom
    for col in columns:
        print(f"{col:15}", end=" | ")  # Menampilkan nama kolom dengan lebar 15 karakter
    print("\n" + "-" * (15 * len(columns) + 3 * len(columns) - 1))  # Garis pemisah antara header dan data

    # Menampilkan isi tabel
    for row in result:
        for col in row:
            print(f"{str(col):15}", end=" | ")  # Menampilkan data dengan lebar 15 karakter
        print()
    
    # Menghitung total belanja
    total_belanja = sum(row[7] for row in result)

    # Menampilkan garis bawah setelah data
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))

    # Menampilkan informasi total belanja
    print(f"Total Pesanan: {total_belanja:15}")

    # Menampilkan garis bawah akhir
    print("-" * (15 * len(columns) + 3 * len(columns) - 1))
    
    return total_belanja, result

def main():
    #lihatlistpesanan()
    tglhariini = datetime.date.today()
    userplg = str(utils.selectsql("nama", "login", "1", "muser")[0])
    while True:
        menu = "\nPilihan menu: \n1. Lihat semua histori pesanan\n2. Lihat histori berdasarkan tanggal\n3. Kembali Ke Menu Utama"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses (1-3) = "))
        if (pilihanmenu == 1): 
            lihatlistpesanan(userplg, "1900-01-01", tglhariini, '%%%%')
        elif (pilihanmenu == 2): 
            tglawal = input("Masukkan tanggal awal dengan format yyyy-MM-dd = ")
            tglakhir = input("Masukkan tanggal akhir dengan format yyyy-MM-dd = ")
            lihatlistpesanan(userplg, tglawal, tglakhir, '%%%%')
        elif (pilihanmenu == 3):    
            import mainplg
            mainplg.main()

main()

