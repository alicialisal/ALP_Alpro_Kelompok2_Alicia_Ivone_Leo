def utama():
    print("=" * 50 + "\n")
    print("MENU UTAMA RESTORAN".center(50) + "\n")
    print("=" * 50)
    while True:
        menu = "\n1. Tambahkan menu makanan\n2. Tambahkan stok makanan sisa\n3. Pesanan Pelanggan\n4. Log Out"
        print(menu)
        pilihanmenu = int(input("\nMasukkan nomor menu yang ingin kamu akses (1/2/3/4) = "))
        if (pilihanmenu == 1): 
            import restoranmenu1 as rmmenu1
            rmmenu1.main()
        elif (pilihanmenu == 2): 
            import restoranmenu2 as rmmenu2
            rmmenu2.main()
        elif (pilihanmenu == 3) : 
            import restoranmenu3 as rmmenu3
            rmmenu3.main()
        else :
            import login
            login.main()

utama()