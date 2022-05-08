from operator import truediv
from statistics import median
import statistics

#num1 = float(input("Pierwsza Ocena: "))
#num2 = float(input("Druga Ocena: "))
#num3 = float(input("Trzecia Ocena: "))
Oceny = []

while (1): 
 print ("1-wpisz ocene 2-skoncz wpisywać")
 spis = float(input("wybierz: "))
 if (spis == 1):
     num4 = float(input("Ocena: "))
     Oceny.append(num4)
 else:
  break

 
    
#srednia =(num1+num2+num3)/3
srednia = statistics.mean(Oceny)
print("srednia:", srednia)

mediana = statistics.median(Oceny)
print("mediana:", mediana)

#dane = [num1,num2,num3]
os=statistics.stdev(Oceny)

print("Odchylenie standardowe: ", os)
                