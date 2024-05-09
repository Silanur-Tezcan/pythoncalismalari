"""#Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini gösteren python kodunu yazınız. 
#(50’den büyükse geçti değilse kaldı yazdıran örnek python kodu)

ders=float(input("ders notunuzu giriniz:"))

if ders>=50:
    print("geçtiniz")

else:
    print("kaldınız")

#Klavyeden girilen sayının tek mi çift mi olduğunu yazdıran python kod örneğini yapınız.
s1=float(input("sayı giriniz:"))
if s1%2==0:
    print("çift sayı.")
else:
    print("tek sayı.")
#1-100'e kadar olan sayıların çift olanlarını ekrana yazdıran kodu yapınız.
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
 #Klavyeden girilen sayıya kadar olan sayıları alt alta yazdıran python kodunu yazınız.
baslangic=int(input("baslangıc sayısını giriniz:")) 
bitiş=int(input("bitiş sayısını giriniz:"))

for i in range(baslangic,bitiş):
   print(i)

#Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen dikdörtgenin alan ve çevresini hesaplayan python kodunu yazınız.
kısaK=float(input("kısa kenar uzunluğunu giriniz:"))
uzunK=float(input("uzun kenar uzunluğunu giriniz:"))
alan=kısaK*uzunK
print("dikdörtgenin alanı:",alan)
cevre=(kısaK+uzunK)*2
print("dikdörtgenin çevresi:",cevre)

# Klavyeden girilen bir metnin harflerini alt alta yazdıran python kodunu yazınız.
metin=input("metin giriniz:")
sayac=0
while sayac<len(metin):
 print(metin[sayac])
 sayac+=1
#Klavyeden girilen iki sayı arasındaki sayıları toplayan python kodunu yazınız.
toplam=0
s1=int(input("sayi giriniz:"))
s2=int(input("ikinci sayıyı giriniz:"))

for i in range(s1+1,s2):
    toplam+=i

print(f"{s1} ile {s2} arasındaki sayıların toplamı:",toplam)"""









