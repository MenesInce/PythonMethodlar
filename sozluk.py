bilgi = {
    "ad"    : "Ahmet",
    "soyad" : "Tan",
    "dYeri" : "Ankara",
    "TcNo"  : 12345678921
}

print(type(bilgi))

#! keys() Sözlük içindeki keyleri döndürür
print(bilgi.keys())

#! values() Sözlük içindeki değerleri döndürür
print(bilgi.values())

#! item() Sözlük içindeki key values değerlerini, eşleştirerek döndürür
print(bilgi.items())

#! get() Sözlük içindeki keyin değerini getirir
print(bilgi.get("ad"))

#! keys() Sözlük güncellemesi yapar
bilgi.update({"Cinsiyet" : "Erkek"}) #* girilen key ve value değerlerini ekler
print(bilgi)

#! __len__() Sözlük içinde kaç tane key value ikilisi olduğunu gösterir
print(bilgi.__len__())

#! pop() verilen keyi silmek için kullanılır
bilgi.pop("TcNo")
print(bilgi)