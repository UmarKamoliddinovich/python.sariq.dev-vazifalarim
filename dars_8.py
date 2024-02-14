


#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi
# harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

# =============================================================================
# 
# cars = ['toyota', 'mazda', 'hyundai', 'gm','kia']
# for car in cars:
#     if car !='gm':
#         print(car.title())
#     else:
#         print(car.upper())
# =============================================================================
        
        
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

# =============================================================================
# login = input("Iltimos login kiriting......\n")
# if login.lower() == "admin" :
#     print(f"Xush kelibsiz {login.title()}.Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {login.title()}")
# =============================================================================
    
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni 
#konsolga chiqaring.

# =============================================================================
# print("Istalgan 2 ta son kiriting....")
# a = float(input("a ="))
# b = float(input("b="))
# if a == b :
#      print("sonlar teng!")
# =============================================================================
     
     
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa 
#"Musbat son" degan xabarni chiqaring.     
# =============================================================================
# 
# x =float(input("Ixtiyoriy son kiriting....\n"))
# 
# if x >=0 :
#     print("Musbat son")
# else:
#     print("Manfiy son")
# =============================================================================
     
     
     
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
#Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.      
     
# =============================================================================
# y = int(input("son kiriting...\n"))
# if y > 0 :
#     print(f"ildiz {y**0.5} ga teng")
# else:
#     print("Musbat son kiriting!")
# =============================================================================
     
     
     
kirish =input()
son = kirish.split()
son1 = int(son[0])
son2 = int(son[1])
print(son1+son2)     
     
     
     
     
     
     
     
     
     
     
     
     
     