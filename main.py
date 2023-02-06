print('============= Selamat datang di Konversi Waktu =============')

def opsi():
    print('[1] Jam')
    print('[2] Hari')
    print('[3] Minggu')
    print('[4] Bulan')
    print('[0] Exit')
def opsi1():
    print('[1] Jam ke Hari')
    print('[2] Jam ke Minggu')
    print('[3] Jam ke Bulan')
    print('[0] Back')
def opsi2():
    print('[1] Hari ke Jam')
    print('[2] Hari ke Minggu')
    print('[3] Hari ke Bulan')
    print('[0] Back')
def opsi3():
    print('[1] Minggu ke Jam')
    print('[2] Minggu ke Hari')
    print('[3] Minggu ke Bulan')
    print('[0] Back')
def opsi4():
    print('[1] Bulan ke Jam')
    print('[2] Bulan ke Hari')
    print('[3] Bulan ke Minggu')
    print('[0] Back')

opsi()
choice = int(input('Pilih satuan waktu yang ingin di konversikan: '))
print('')
while choice != 0:
    if choice == 1:
        opsi1()
        pilihan = int(input('Pilih waktu yang ingin dikonversikan: '))
        print('')
        print('Memilih Satuan Jam')
        if pilihan == 1:
            operasi11 = int(input('Berapa Jam?: '))
            hasil11 = operasi11 / 24
            print(hasil11, 'Hari')
            
        elif pilihan == 2:
            operasi12 = int(input('Berapa Jam?: '))
            hasil12 = operasi12 / 168
            print(hasil12, 'Minggu')
            
        elif pilihan == 3:
            operasi13 = int(input('Berapa Jam?: '))
            hasil13 = operasi13 / 720
            print(hasil13, 'Bulan')
            
    elif choice == 2:
        opsi2()
        pilihan = int(input('Pilih waktu yang ingin dikonversikan: '))
        print('')
        print('Memilih Satuan Hari')
        if pilihan == 1:
            operasi21 = int(input('Berapa Hari?: '))
            hasil21 = operasi21 * 24
            print(hasil21, 'Jam')
            
        elif pilihan == 2:
            operasi22 = int(input('Berapa Hari?: '))
            hasil22 = operasi22 / 7
            print(hasil22, 'Minggu')
            
        elif pilihan == 3:
            operasi23 = int(input('Berapa Hari?: '))
            hasil23 = operasi23 / 30
            print(hasil23, 'Bulan')
            
    elif choice == 3:
        opsi3()
        pilihan = int(input('Pilih waktu yang ingin dikonversikan: '))
        print('')
        print('Memilih Satuan Minggu')
        if pilihan == 1:
            operasi31 = int(input('Berapa Minggu?: '))
            hasil31 = operasi31 * 168
            print(hasil31, 'Jam')
            
        elif pilihan == 2:
            operasi32 = int(input('Berapa Minggu?: '))
            hasil32 = operasi32 * 7
            print(hasil32, 'Hari')
            
        elif pilihan == 3:
            operasi33 = int(input('Berapa Minggu?: '))
            hasil33 = operasi33 / 4
            print(hasil33, 'Bulan')

    elif choice == 4:
        opsi4()
        pilihan = int(input('Pilih waktu yang ingin dikonversikan: '))
        print('')
        print('Memilih Satuan Bulan')
        if pilihan == 1:
            operasi41 = int(input('Berapa Bulan?: '))
            hasil41 = operasi41 * 720
            print(hasil41, 'Jam')
            
        elif pilihan == 2:
            operasi42 = int(input('Berapa Bulan?: '))
            hasil42 = operasi42 * 30
            print(hasil42, 'Hari')
        elif pilihan == 3:
            operasi43 = int(input('Berapa Bulan?: '))
            hasil43 = operasi43 * 4
            print(hasil43, 'Minggu')
    else:
        print('Pilihlah salah satu!')
    print('')
    opsi()
    choice = int(input('Pilih satuan waktu yang ingin di konversikan: '))
print('Sampai jumpa lagi!')
print('============= By Hardjuno Indracahya =============')