import mysql.connector
import os
import bcrypt
import getpass
import sys
import utils

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "foodwaste"
)

connectsrv = connector.cursor()

def enkripsi_password(password_plaintext):
    # Mengenerate salt dan mengenkripsi password
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password_plaintext.encode('utf-8'), salt)
    return password_hashed.decode('utf-8')

def cek_password(password_plaintext, password_hashed):
    # Memeriksa apakah password sesuai dengan yang terenkripsi
    return bcrypt.checkpw(password_plaintext.encode('utf-8'), password_hashed.encode('utf-8'))

def login():
    global passsalah
    print("=" * 30 + "\n" + " "*10 + "MASUK AKUN\n" + "=" * 30)
    username = input("\nSilahkah masukkan username dan password anda.\nUsername: ")
    if (utils.selectsql("nama", "nama", username, "muser") != "" and utils.selectsql("nama", "nama", username, "muser") is not None):
        passuser = getpass.getpass(prompt="Masukkan password: ")
        if(cek_password(passuser, str(utils.selectsql("password", "nama", username, "muser")[0])) == True):
            connectsrv.execute(f"UPDATE muser set login = 1 where nama = '{username}'")
            connector.commit()
            if (str(utils.selectsql("restoran", "nama", username, "muser")[0]) == "1"):
                return "restoran"
            else : 
                return "pelanggan"
        else:
            if (passsalah == 3): 
                print(f"Password yang anda masukkan salah. (PERCOBAAN = {passsalah}/3)")
            else :
                print(f"Password yang anda masukkan salah. Silahkan coba lagi! (PERCOBAAN = {passsalah}/3)")
            return False
    else: 
        buatakun = int(input("\nUsername belum ada. Apakah anda ingin membuat akun baru?\n1. Ya\n2. Tidak\nPilihan anda (1/2) = "))
        if (buatakun == 1): signup()
        else: sys.exit()
        
def pilihkat():
    utils.lihatkat()
    kategori = ""
    jumkat = 0
    while True:
        kodekat = input(f"\nMasukkan kode kategori restoran anda (1-19) = ")
        selectkat = str(utils.selectsql("kategori", "kode", kodekat, "mkategori")[0])
        konfirmasi = input(f"\nKategori yang anda pilih = {selectkat}\nAnda yakin ingin menambahkan kategori tersebut? (Y/N) ")
        if konfirmasi.lower() == 'n': continue
        else :
            kategori += selectkat
            print(f"Kategori Restoran = {kategori}")
        tambahkat = input(f"\nMasih ingin menambahkan kategori lain? (Y/N) ")
        jumkat += 1
        if (tambahkat.lower() == 'y'):
            if jumkat < 3:
                kategori += ", "
            else: 
                print("! MAKSIMAL 3 KATEGORI !")
                break
        else: break
    return kategori

def autonoresto():
    connectsrv.execute(f"SELECT MAX(koderesto) FROM mresto")

    noterakhir = connectsrv.fetchone()[0]  # Get the last stored number

    if noterakhir:  # If there's a last stored number
        noterakhir = int(noterakhir[1:])  # Extract the numeric part, assuming it's at positions 6 to end
        nourut = str(noterakhir + 1).zfill(4)  # Increment the number and pad with zeros to 4 digits
    else:
        nourut = "0001"  # If it's the first entry for the day

    notambah = f"R{nourut}"  # Create the new 'notambah'

    return notambah

def autonoplg():
    connectsrv.execute(f"SELECT MAX(kodeplg) FROM mpelanggan")

    noterakhir = connectsrv.fetchone()[0]  # Get the last stored number

    if noterakhir:  # If there's a last stored number
        noterakhir = int(noterakhir[1:])  # Extract the numeric part, assuming it's at positions 6 to end
        nourut = str(noterakhir + 1).zfill(4)  # Increment the number and pad with zeros to 4 digits
    else:
        nourut = "0001"  # If it's the first entry for the day

    notambah = f"P{nourut}"  # Create the new 'notambah'

    return notambah
        
def isibioresto():
    print("=" * 30 + "\n" + "Silahkan lengkapi data restoran anda.\n" + "=" * 30)
    koderesto = autonoresto()
    namaresto = input("\nNama Restoran: ")
    almresto = input("Alamat Restoran: ")
    jamtutup = input("Jam Tutup Resto (HH:mm:ss) : ")
    katresto = pilihkat()
    konfirmasi = input(f"\nApakah data-data yang anda isikan sudah sesuai? (Y/N) ")
    if konfirmasi.lower() == 'y':
        connectsrv.execute(f"INSERT INTO mresto (koderesto, nama, alamat, kategori, jamtutup) VALUES ('{koderesto}', '{namaresto}', '{almresto}', '{katresto}', '{jamtutup}')")
        connector.commit()
        return koderesto
    
def isibioplg():
    print("=" * 30 + "\n" + "Silahkan lengkapi data akun anda.\n" + "=" * 30)
    kodeplg = autonoplg()
    namaplg = input("\nNama : ")
    emailplg = input("Email : ")
    notelpplg = input("Nomor Telepon : ")
    konfirmasi = input(f"\nApakah data-data yang anda isikan sudah sesuai? (Y/N) ")
    if konfirmasi.lower() == 'y':
        connectsrv.execute(f"INSERT INTO mpelanggan (kodeplg, nama, email, notelp) VALUES ('{kodeplg}', '{namaplg}', '{emailplg}', '{notelpplg}')")
        connector.commit()
        return kodeplg

def signup():
    print("=" * 30 + "\n" + " "*10 + "DAFTAR AKUN\n" + "=" * 30)
    username = input("\nSilahkah masukkan username dan password anda.\nUsername: ")
    if (utils.selectsql("nama", "nama", username, "muser") == "" or utils.selectsql("nama", "nama", username, "muser") is None):
        passuser = getpass.getpass(prompt="Masukkan password: ")
        pilihan = int(input("\nAnda ingin mendaftar sebagai: \n1. Pihak Restoran\n2. Pembeli\nJawab (1/2): "))
        if pilihan == 1: 
            cekrestoran = 1
            koderestoplg = isibioresto()
        else : 
            cekrestoran = 0
            koderestoplg = isibioplg()
        connectsrv.execute(f"INSERT INTO muser (nama, password, restoran, koderestoplg) VALUES ('{username}', '{enkripsi_password(passuser)}', {cekrestoran}, '{koderestoplg}')")
        connector.commit()
    else: 
        pilih = int(input("\nUsername sudah ada. Apakah anda ingin mengulang pembuatan akun dengan username baru?\n1. Ya\n2. Tidak\n3. Pergi ke halaman login\nJawab (1/2/3): "))
        if pilih == 1: signup()
        elif pilih == 2: sys.exit()
        else: login()
    main()
    
def main():
    os.system('cls')
    connectsrv.execute("UPDATE muser set login = 0")
    connector.commit()
    print("=" * 50 + "\n")
    print("SELAMAT DATANG DI MAKANLAGI".center(50))
    print(" " * 6 + "\033[3mKembali ke Meja Anda\033[0m dengan \033[1mHarga Hemat\033[0m\n")
    print("=" * 50)
    adaakun = int(input("\nApakah anda sudah memiliki akun sebelumnya?\n1. Ya\n2. Tidak\nJawab (1/2): "))
    if (adaakun == 1):
        connectsrv.execute("UPDATE mmenu set stok = 0")
        connector.commit()
        utils.updatestok()
        passsalah = 1
        while passsalah <= 3:
            returnlogin = login()
            if returnlogin == "restoran" :
                print("\n | LOGIN SEBAGAI PIHAK RESTORAN BERHASIL |\n")
                import mainrestoran as resto
                resto.utama()
            elif returnlogin == "pelanggan":
                print("\n | LOGIN SEBAGAI PIHAK PEMBELI BERHASIL |\n")
                import mainplg as plg
                plg.main()
            else:
                passsalah += 1
    else : signup()


username = ''
passsalah = 0
main()


