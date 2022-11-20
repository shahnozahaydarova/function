try:
    while True:
        a = input("Karta raqamingizni kiriting: ")
        if len(a) == 16:
            if a[0:4] == 8600:
                print("Uzcard karta raqamini kiritdingiz.Davom etishingiz mumkin.Qaysi xizmat turidan foydalanishni xoxlaysiz.")
                break
            elif a[0:4] == '9860':
                print("Humo karta raqamini kiritdingiz.Davom etishingiz mumkin.Qaysi xizmat turidan foydalanishni xoxlaysiz.")
                break
            else:
                print("Siz kiritgan ma'lumot bo'yicha plastik karta topilmadi qayta urinib ko'ring.")
        else:
            print("Karta raqami 16ta raqamdan iborat bo'lishi kerak qayta urinib ko'ring.")
except ValueError:
    print("Siz karta raqamini kiritish o'rniga harf kiritdingiz,qayta urinib ko'ring.")
        