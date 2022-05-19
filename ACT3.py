#Ferdinand Andhika W / 50421513
print('=================================================')
print('|            PROGRAM FUNCTION BIODATA           |')
print('=================================================')

def biodata():
    nama = str(input('Masukan Nama\t: '))
    kelas = str(input('Masukan Kelas\t: '))
    npm = int(input('Masukan NPM\t: '))
    print('=================================================')
    print('Nama anda adalah  : ',nama)
    print('Kelas anda adalah : ',kelas)
    print('NPM anda adalah   : ',npm)
biodata()

print('\n=================================================')
print('|       PROGRAM MENGHITUNG LUAS SEGITIGA        |')
print('=================================================')

def segitiga():
    alassegitiga = float(input('Masukan alas segitiga\t: '))
    tinggisegitiga = float(input('Masukan tinggi segitiga\t: '))
    luassegitiga = float(alassegitiga * tinggisegitiga) /2
    print('=================================================')
    print('Luas Segitiga adalah\t: ',luassegitiga)
segitiga()


