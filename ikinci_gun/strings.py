ad = 'cagri'
soyAd = 'yalniz'
yas = 26

kisi = ad + soyAd + str(yas)

print(kisi)
print('uzunluk: ' + str(len(kisi)))
print(kisi[1])
print('sıfırıncı, birinci, ikinci, ucuncu indexler:' + kisi[0:4])
print('ustteki ile ayni degerler ' + kisi[:4])
print(kisi[-12])
print(kisi)
print('2. indexten basla, 8. indexe kadar git, 2şer 2şer atla: ' "\n" + kisi[2:8:2])
# tırnak içinde \n alt satıra gönderir 

print('my name is:  {}'.format(ad))
print('i am {} {}'.format(ad,soyAd))

print('adim: {a}, yasim: {y}'.format(a=ad, y=yas))

print(f'ben {ad}, {yas} yaşındayım')
print(kisi[-5: -1])
print(kisi[1:len(kisi)])