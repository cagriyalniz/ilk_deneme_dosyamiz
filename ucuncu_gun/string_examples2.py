cumle1 = ' merhaba dünya '

cumle2 = cumle1.rstrip()
print(cumle2)

cumle3 = 'bu bir deneme mesajıdır'
cumle4 = cumle3.strip('br')
print(cumle4)

cumle5 = 'kimileri için kötümserlik, hayatın bir anlamının olmadığı anlamına gelir.'
syc1 = cumle5.count('a')
print(syc1)

syc2 = cumle5.count('kimileri')
print(syc2)

syc3 = cumle5.count('i', 3,13)
print(syc3) 


a = 'deneme'
print(a.isalpha())

b = 'D3N3M3'
print(b.isdigit())

cumle6 = 'bugün ülke geneli yer yer yağışlı'
print(cumle6.center(60, '*'))
print(cumle6.rjust(60, '-'))

cumle7 = 'beni darmadağın eden ve bunalımlara sürükleyen, olabileceğim o öteki kişiye duyduğum bu özlem işte! - fernando pessoa.'
cumle8 = cumle7.replace('b' ,'d').replace('d', 'b')
print(cumle7)
print(cumle8)