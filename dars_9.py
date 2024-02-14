# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:20:22 2024

@author: MSI
"""

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa 
#"Bu son juft emas" degan xabarni chiqaring.

# =============================================================================
# son = int(input("Juft son kiriting:\t"))
# if son % 2 == 0 :
#     print("Rahmat")
# else:
#     print(f"{son} juft son emas")
# =============================================================================



#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm


# =============================================================================
# yosh = int(input("Yoshingizni kiriting:\t"))
# if yosh <=4 or yosh>=60 :
#     print("Sizga kirish bepul!")
# elif yosh < 18 :
#     print("Sizga kirish 10 000  so'm")
# elif yosh > 18 :
#     print("Sizga kirish 20 000  so'm")
#     
# =============================================================================
    
    
#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi
#haqida xabarni chiqaring    

# =============================================================================
# print("Ikkita son kiriting>>>\n")
# b_son = float(input("Birinchi soni kiriting:\t"))
# ik_son = float(input("Ikkinchi soni kiriting:\t"))
# if b_son > ik_son :
#     print(f"{b_son} > {ik_son}")
# elif b_son < ik_son :
#     print(f"{b_son} < {ik_son}")
# else:
#     print(f"{b_son} = {ik_son}")
# =============================================================================
    
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating
#va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan 
#solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan 
#xabarlarni chiqaring.

# =============================================================================
# mahsulotlar = ['olcha', ' xurmo', 'anor', 'zaytun', 'kartoshka', 'qalampir', 'gilos', 'behi', 'o\'rik']
# savat = []
# print("5 ta mahsulot nomini kiriting:")
# for i in range(5) :
#     savat.append(input(f"Savatga {i+1} - mahsulotni qo'shing: "))
# 
# for x in savat :
#    if  x in mahsulotlar :
#        print(f"Do'konda {x} bor")
#    else:
#        print(f"Do'konda {x} yo'q")
#     
# =============================================================================
    

#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan 
#va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan 
#ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan 
#xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.  
    
    
# =============================================================================
# mahsulotlar = ['olcha', 'xurmo', 'anor', 'zaytun', 'kartoshka', 'qalampir', 'gilos', 'behi', 'o\'rik']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# print("5 ta mahsulot nomini kiriting:")
# for i in range(5) :
#     savat.append(input(f"Savatga {i+1} - mahsulotni qo'shing: "))
# for x in savat:
#     if  x in mahsulotlar :
#         bor_mahsulotlar.append(x)
#     else:
#         mavjud_emas.append(x)
# if mavjud_emas :
#     print(f"Quyidagi mahsulotlat yo'q\n {mavjud_emas}")
# else:
#     print("Siz so'ragan barcha narsa do'konimizda bor..")
# =============================================================================
    
    
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang 
#va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday 
#login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.    
    
    
# =============================================================================
# foydalanuvchilar = ['umar', 'anvar', 'yusuf', 'sayyod', 'mashrab']
# new_login =input("Yangi login kiriting:\t")
# 
# if new_login in foydalanuvchilar :
#     print("Login band. Yangi login tanlang >>")
# else:
#     print(f"Xush kelibsiz, {new_login}")
# =============================================================================
    
#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi 
#kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz 
#bo'linishini konsolga chiqaring.    
 
son =  int(input('Istalgan butun son kiriting:'))
for n in range(2,11):
    if not (son%n) :
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
    
    
    
    
    
    
    