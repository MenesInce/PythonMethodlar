x = -2
 #! abs -> mutlak değer

print(x.__abs__())
print(abs(x)) 

 #! pow -> üs alır 

print(x.__pow__(3))
print(pow(x,3)) #x in 3. kuvveti

#! divmod -> bir bölme işleminde bölüm ve kalan kısmını demet olarak gösterir

y = 15
print(y.__divmod__(2)) # (7,1)

#! as_integer_ratio() -> girdiğimiz sayının(y) hangi iki sayının bölümünün sonucu olduğunu gösterir

print(y.as_integer_ratio())
