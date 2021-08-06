# veri tipi donusumleri

a = input('ilk sayi ')
b = input('ikinci sayi ')

print(type(a))
print(type(b))

toplam = a + b
print(toplam)

toplam2 = int(a) + int(b)
print(toplam2)


#string birlestirme:
x = 1.2
y=4
sonuc = str(x) + str(y)
print(sonuc)

dogruMu = True
print(dogruMu)

dogruMu1 = int(dogruMu)
print('dogruMu1 type: ', type(dogruMu1))
print('dogruMu1: ', dogruMu1)


dogruMu2 = str(dogruMu)
print('dogruMu2 type: ', type(dogruMu2))
print('dogruMu2: ', dogruMu2)

dogruMu3 = bool(dogruMu)
print('dogruMu3 type: ', type(dogruMu3))
print('dogruMu3: ', dogruMu3)

######################

r = float(input('yaricap: '))
pi = 3.14
cevre = 2*pi*r
alan = pi*r*r

# print('cevre: ' + (cevre) + ', ' + 'alan: ' + (alan))
# TypeError: can only concatenate str (not "float") to str

print('cevre: ' + str(cevre) + ', ' + 'alan: ' + str(alan))

