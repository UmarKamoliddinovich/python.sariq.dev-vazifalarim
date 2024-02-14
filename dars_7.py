# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:29:59 2023

@author: MSI
"""

#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta 
#takrorlanganini yozing)

# =============================================================================
# ismlar =['Yusufjon','Asror aka', 'Shovkat aka', 'Abdukarim aka', 'Shag\'zod aka' ]
# for ism in ismlar:
#     print(f"{ism} bugun o'qishga borasizmi?")
# 
# print(f"Kod {len(ismlar)} marta takrorlandi")
# 
# =============================================================================



#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan
# konsolga chiqaring.

# =============================================================================
# toq_sonlar = list(range(11,100,2))
# for n in toq_sonlar:
#     print(f"{n} ning kubi {n**3} ga teng.")
# =============================================================================
    

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling.
#Natijani konsolga chiqaring.

# =============================================================================
# print("5 ta sevimli kinolaringizni kiriting:")
# sevimli_kino =[]
# for n in range(5):
#     sevimli_kino.append(input(f"{n+1} - kinoni kiriting:"))
# print(sevimli_kino)    
#     
# =============================================================================
    

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
#va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
    

x = int(input("Bugun nechta odam bilan suhbat qurdingzi?"))
odam =[]
for n in range(x):
     odam.append(input((f"{n+1} - odamning ismi: ")))
print(odam)    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    