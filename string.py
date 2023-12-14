x = "Anlaşılır Ekonomi"

#! lower() -> bütün karakterleri küçük harfe çevirir
y = x.lower()
print(y)

#! upper() -> bütün karakterleri büyük harfe çevirir
y = x.upper()
print(y)

#! capitalize() -> Cümlenin ilk kelimesinin ilk harfini büyük harfe çevirir
z = "Anlaşılır ekonomi"
a = z.capitalize()
print(a)

#! title() -> bütün kelimlerin ilk harflerini büyük harfe çevirir
a = z.title()
print(a)

#! swapcasse() -> büyük karakterleri küçük,küçük karakterleri büyük harfe çevirir
a = z.swapcase()
print(a)

#! count() -> sayım yapar
a = z.count("ı") # anlaşılır ekonomi içinde 2 tane ı vardır
print(a)

#! strip() -> soldan ve sondan sayım yapar. verdiğimiz değerleri siler
b = "   Anlaşılır ekonomi  "
c = b.strip(" ") # baştan ve sondan tarayarak bulduğu boşlukları siler
print(c)

#! split() -> yapıyı parçalar ve liste olarak döndürür
c = b.split(" ")
print(c)

#! split() -> parçalanmış değişkeni birleştirir
c = "**".join(c)
print(c)

#! find() -> arattığımız karakteri,kelimeyi bulur ve index numarasını getirir
cumle = "Merhaba ben python öğreniyorum"
d = cumle.find("ben")
print(d)

#! replace() -> değişim yapar
d = cumle.replace("Merhaba","Selam") # merhaba selam olarak değiştirildi
print(d)


ad = "Ahmet"
soyad = "Tan"
yas = 54

bilgiler = [ad,soyad,yas]
print("Adı : {}, Soyadı : {}, Yaş : {}"
      .format(bilgiler[0],bilgiler[1],bilgiler[2]))
