list = [1,2,5,"Merhaba",2.5,]
print(list)

#! append() Liste sonuna eleman ekler
list.append("Anlaşılır ekonomi")
print(list)

#! insert() Listenin istediğimiz yerine eleman ekler
list.insert(3,"Selam")
print(list)

#! remove() verdiğimiz parametreyi soldan tarayarak ilk bulduğu yerden siler
list.remove(2)
print(list)

#! pop() boş çalıştırılırsa sondaki elemanı siler. İndex girersek index değerine karşılık gelen elemanı siler
list.pop()
print(list)

#! copy() elimizdeki listenin kopyasını değişken olarak tutmak için
list2 = list.copy()
print(list2)

#! extend() iki listeyi birleştirmek için kullanılır
list3 = ["Liste 3",1,36,5]
list4 = ["Liste 4","a","b","c"]
list3.extend(list4)
#* list3 += list4 de aynı işlemi yapar
print(list3)

#! count() liste içindeki elemanlardan sorguladığımız elemandan kaç tane olduğunu getirir
list5 = [1,36,5,5,13,5]
print(list5.count(5))

#! sort() liste içindeki elemanları küçükten büyüğe sıralar
list5.sort(reverse=True) #* reverse true büyükten küçüğe sıralar
print(list5)

#! clear() liste içindeki elemanları temizler ve boş liste("[]") getirir
list5.clear()
print(list5)