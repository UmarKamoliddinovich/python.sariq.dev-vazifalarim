# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:48:35 2023

@author: MSI
"""
# =============================================================================
# 
# friend =["sayyod","mashrab","yusufjon"]
# print("Salom " + friend.pop(0))
# print("qalesan " + friend.pop(0) + ' ishlarin joyidami')
# print(friend.pop(0)+" ish qale o'rganib qoldinmi?")
# =============================================================================

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

# =============================================================================
# sonlar = [12,23,-3,-8,2.3,1.7]
# print(sonlar[0] + sonlar[-1])
# print(sonlar[1]**2+ sonlar[4]**2)
# print(sonlar)
# sonlar[3] = 123
# print(sonlar)
# sonlar.append(12)
# sonlar.insert(0,134)
# print(sonlar)
# print(sonlar.pop(-1))
# del sonlar[2]
# print(sonlar)
# sonlar.remove(2.3)
# print(sonlar)
# =============================================================================

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
    
#t_shaxslar = ['Amir Temur','Alisher Navoiy','Jaloliddin Rumiy']
#z_shaxslar = ["Muhammadali Eshonqulov", "Hasan va Husan Mamasaidovlar", "Hasanxon Yahyo Abdulmajid"]
#print("Men tarixiy shaxslardan " + t_shaxslar.pop(0) + " bilan ko'rishishni xohlar edim")
#print("Zamonaviy shaxslardan esa " + z_shaxslar.pop(-1) + " bilan suhbat qurishni juda xohlar edim")


# =============================================================================
# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# =============================================================================

friends = []
friends.append("Sayyod")
friends.append("Mashrab")
friends.append("Yusufjon")
friends.append("Ozodbek")
friends.append("Baxodir")
friends.append("Nodirbek")
del friends[-1]
friends.remove("Baxodir")
friends.insert(0,"Alimardon")
friends.append("Abdulaziz")
friends.insert(2,"Mirsaid")




#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga 
#kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.


mehmonlar =[]
#print(friends )
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(3))




























