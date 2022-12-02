import time
a = 0
while True:
    a += 1
    parol = input("Parolni kiriting: ")
    if parol == '123':
        print("Kirishingiz mumkin.")
        break
    elif a == 3:
        print("Siz parolni 3 marta noto'g'ri kiritdingiz kuting va qayta urinib ko'ring: ")
        for x in range(15):
            time.sleep(1)
            print(x)
    elif a== 5:
        print("Siz parolni 5 marta noto'g'ri kiritdingiz kuting va qayta urinib ko'ring: ")
        for x in range(30):
            time.sleep(1)
            print(x)
        a = 0