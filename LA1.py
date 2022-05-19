#Ferdinand Andhika W / 50421513

print('========================================')
print('|     PROGRAM KONVERSI TEMPERATURE     |')
print('========================================')

celcius = input('Masukan suhu dalam celcius : ')
print('========================================\n')

print('Suhu adalah ' + celcius + ' Celcius')

reamur = ((4 / 5) * float(celcius))
print('Suhu dalam reamur adalah ' + str(reamur) + ' Reamur')

fahrenheit = (9 / 5) * float(celcius) + 32
print('Suhu dalam fahrenheit adalah ' + str(fahrenheit) + ' Fahrenheit')

kelvin = float(celcius) + 273
print('Suhu dalam kelvin adalah ' + str(kelvin) + ' Kelvin')
print('\n========================================')