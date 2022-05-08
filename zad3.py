import random
l=0
num=0
losowanie = []
gracz = []
while l != 6:
 los= random.randint(1, 49)
 #print ("los:", los)
 losowanie.append(los)
 
 liczba = int(input("Podaj liczbe (nie może być mniejsza od 1 i wieksza od 49): "))
 if (liczba < 1 or liczba > 49):
     print ("wprowadziłś złą wartość przepadł los")
 else:
    gracz.append(liczba) 
 
      
      
 
 l+=1
print ("liczby gracza :", gracz)
print ("Wylosowane liczby:", losowanie)

porownanie = set(gracz) & set(losowanie)

print ("trafiłeś: ", porownanie)