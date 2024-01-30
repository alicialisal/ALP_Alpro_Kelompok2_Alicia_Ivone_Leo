def main():
    print("=" * 50 + "\n")
    print("MENU UTAMA PEMBELI".center(50) + "\n")
    print("=" * 50)
    while True:
        menu = "\n1. Lihat Menu Restoran\n2. Lihat Keranjang\n3. Lihat Histori Pesanan\n4. Log Out"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses = "))
        if (pilihanmenu == 1): 
            import plgmenu1
            plgmenu1.main()
        elif (pilihanmenu == 2): 
            import plgmenu2
            plgmenu2.main()
        elif (pilihanmenu == 3): 
            import plgmenu3
            plgmenu3.main()
        else:
            import login
            login.main()
            
main()