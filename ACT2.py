#Ferdinand Andhika W / 50421513
print('===========================================================')
print('|                      MENU PROGRAM                       |')
print('===========================================================')
print('1. Program Grade Nilai')
print('2. Program Mengeluarkan Data Array')
    
program = int(input('Silahkan pilih program yang diinginkan (1 atau 2) : '))

#Percabangan / Program Grade
if program == 1:
    print('\n===========================================================')
    print('|                    PROGRAM GRADE NILAI                    |')
    print('===========================================================')
    uts = int(input('Masukkan Nilai UTS anda : '))
    uas = int(input('Masukkan Nilai UAS anda : '))
    
    totaluts = (uts * 70) / 100
    totaluas = (uas * 30) / 100

    rata2 = totaluts + totaluas
    
    if rata2 >= 90:
        print('Anda mendapatkan Grade A dengan total nilai ' + str(rata2))
    elif rata2 >= 80:
        print('Anda mendapatkan Grade B dengan total nilai ' + str(rata2))
    elif rata2 >= 70:
        print('Anda mendapatkan Grade C dengan total nilai ' + str(rata2))
    elif rata2 >= 60:
        print('Anda mendapatkan Grade D dengan total nilai ' + str(rata2))
    elif rata2 < 60:
        print('Anda mendapatkan Grade E dengan total nilai ' + str(rata2))

#Program Array
elif program == 2:
    print('\n===========================================================')
    print('|              PROGRAM MENGELUARKAN DATA ARRAY              |')
    print('===========================================================')

    array = ['Ferdinand', 'Andhika', 'Widhiyan', 'Alexandra', 'Dadario']
    ferdinand = 1

    print('Data Array : ')
    print(str(array))
    print('===========================================================')

    
    while ferdinand <= 5:
        for perulangan in array:
            print('Nama array ke ', str(ferdinand), ' : ',perulangan)
            ferdinand += 1

else:
    print('\n===========================================================')
    print('Angka menu yang anda masukan salah, pilih angka 1 atau 2')
