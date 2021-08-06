cumle1 = "Oh my God! ChAndleR bing!"
def string1_func(cumle1):
    print(cumle1.upper())
    print(cumle1.lower())
    print(cumle1.title())
    print(cumle1.capitalize())

string1_func(cumle1)

#printlerin hepsini ayrı ayrı yazmıştım
# fakat vscode fonksiyona çevirmemi önerince tek tuşla çevirdim
# çok da iyi oldu çok da güzel oldu

cumle2 = " düşmüş , delinin yıldızı yüzüyor ayağımın ucunda"
#strip fonk boşluğu siler
print(cumle2.strip())


print(cumle2.split())
cumle3 = cumle2.split()
print(cumle3[1:6])
cumle4 = cumle2.split(',')
print(cumle4)
cumle5 = cumle2.split('d')
print(cumle5)
cumle6 = 'd'.join(cumle5)
print(cumle6)

#istediğimin, kaçıncı indexten başladığını bulur find
bul = cumle6.find('yıldızı')
print(bul)

#alttaki kod çalışmadı çünkü: 
# 'list' object has no attribute 'find'
# bul2 = cumle4.find('delinin')
# print(bul2)

#alltaki kodun çıktısına false verdi, çünkü:
#cümle d ile değil, boşluk ile başlıyor ;)
ilkharf = cumle2.startswith('d')
print(ilkharf)

sonharf = cumle2.endswith('a')
print(sonharf)

cumle7 = cumle2.replace('düşmüş', 'düşüvermiş')
print(cumle7)

cumle8 = cumle2.replace('düşmüş', 'düşmemiş').replace('yıldızı', 'kuyruklu yıldızı')
print(cumle8)

print(cumle8.center(125))
print(cumle8.center(100, '*'))