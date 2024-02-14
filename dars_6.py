# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:33:05 2023

@author: MSI
"""


# =============================================================================
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# Ro'yxatning uzunligini konsolga chiqaring
# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# Asl ro'yxatni qaytadan konsolga chiqaring
# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# =============================================================================

davlatlar =['Germaniya' ,'Amerika', 'Shvetsariya', 'Ispaniya' ]
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))
#print(davlatlar.reverse())
# =============================================================================
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# =============================================================================
         
# =============================================================================
# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# Ro'yxatdagi elementlar sonini hisoblang
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# =============================================================================

juft_sonlar = list(range(120,1200,2))
print(juft_sonlar)
print("Uzunligi:" ,len(juft_sonlar))
print("Yeg'indisi:", sum(juft_sonlar))




























