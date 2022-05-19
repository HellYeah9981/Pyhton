#Ferdinand Andhika W / 50421513
#Array Return
def program_biodata():
            print('\n===========================================================')
            print('|                     PROGRAM BIODATA                     |')
            print('===========================================================')
            nama = str(input('Masukan Nama\t: '))
            kelas = str(input('Masukan Kelas\t: '))
            npm = int(input('Masukan NPM\t: '))
            print('=================================================')
            print('Nama anda adalah  : ',nama)
            print('Kelas anda adalah : ',kelas)
            print('NPM anda adalah   : ',npm)
            return 0

while True: #Menu Program
    print('\n===========================================================')
    print('|                      MENU PROGRAM                       |')
    print('===========================================================')
    print('1. Program Biodata')
    print('2. Program Konversi Temperatur')
    print('3. Program Membuat Bangun Persegi')
    print('4. Keluar Dari Program')
    program = input('Silahkan pilih program yang diinginkan : ')

#Program Biodata
    if program == '1':
          program_biodata()

#Program Konversi Temperatur
    elif program == '2':
        print('\n===========================================================')
        print('|              PROGRAM KONVERSI TEMPERATURE               |')
        print('===========================================================')

        celcius = input('Masukan suhu dalam celcius : ')
        print('========================================\n')

        print('Suhu adalah ' + celcius + ' Celcius')

        reamur = ((4 / 5) * float(celcius))
        print('Suhu dalam reamur adalah ' + str(reamur) + ' Reamur')

        fahrenheit = (9 / 5) * float(celcius) + 32
        print('Suhu dalam fahrenheit adalah ' + str(fahrenheit) + ' Fahrenheit')

        kelvin = float(celcius) + 273
        print('Suhu dalam kelvin adalah ' + str(kelvin) + ' Kelvin')

#Program Bangun Persegi
    elif program == '3':
        print('\n===========================================================')
        print('|             PROGRAM MEMBUAT BANGUN PERSEGI              |')
        print('===========================================================')
        persegi = int(input("Masukkan Ukuran Persegi yang anda inginkan : "))
        for fer in range (persegi):
            for di in range (persegi):
                if (fer == 0 or di == 0 or fer == persegi - 1 or di == persegi - 1):
                    print( "*" , end = "  ") 
                else:
                    print( " " , end = "  ")
            print() 

    elif program == '4':
        print('\n===========================================================')
        print("Program telah keluar\n")      
        exit()
        