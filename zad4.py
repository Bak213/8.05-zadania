liczby =[]
liczby2=[]
while 1:
    wybor=int(input("1-podaj kojną liczbę 2-przerwij: "))
    if wybor == 1:
    
        
        liczba = int(input("Podaj liczbe: "))
        liczby.append(liczba) 
        liczby2.append(liczba)
    else:
        break
    
print ("wartosci listy z indexami: ")
for i in range(len(liczby)):
    print ("[",i,"]: ", end = " ")
    print (liczby[i])
    

   
print ("posortowana wartosci tablicy w odwrotnejj kolejnosci: ")
liczby2.sort(reverse=True)
print(liczby2)

print("Posortowane wartosic listy: ")
liczby2.sort()
print (liczby2)

print("Usunięcie pierwszej wartości z listy")
liczby.pop(0)
print(liczby)

licz=int(input("Podaj wartość której chcesz sprawdzić ilość: "))

l = liczby.count(licz)
index = liczby.index(licz)
print(licz,"wystąpiło:",l,"index pierwszego wystąpienia: [",index,"]")

print ("lista ma długość: ",len(liczby))
i=int(input("od ktorego indexu chcesz wypisac liste: "))
j=int(input("do ktorej wartosci chesz wypisać liste: "))

elementy = liczby[i:j+1]

print("wartosci listy od ",i,"do",j,": ",elementy)


