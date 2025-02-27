import random
import os

def method(sidebar):
    

    if len(sidebar) != 5:
        return "Ошибка: Рука должна содержать 5 карт."

    for map in sidebar:
        if not isinstance(map, int) or map <= 0:
            return 
    schetchik = {}
    for map in sidebar:
        schetchik[map] = schetchik.get(map, 0) + 1

    fullreceive = sorted(schetchik.values(), reverse=True)

    if len(schetchik) == 1:
        return "poker"
    elif fullreceive == [4, 1]:
        return "four of a kind"
    elif fullreceive == [3, 2]:
        return "full house"
    elif fullreceive == [3, 1, 1]:
        return "three of a kind"
    elif fullreceive == [2, 2, 1]:
        return "two pairs"
    elif fullreceive == [2, 1, 1, 1]:
        return "one pair"
    else:
        return "all different"



def generate():
    sidebar = [random.randint(1, 10) for _ in range(5)]  
    return sidebar

random_sidebar = generate()
way = method(random_sidebar)

print(f"Рука: {random_sidebar}")
print(f"Комбинация: {way}")

if way == "two pairs":
    print("Выпало две пары! Компьютер выключается...")

    os_name = platform.system()

    if os_name == "Windows":
        os.system("shutdown /s /t 1")  
    elif os_name == "Linux" or os_name == "Darwin":  
        
        if os.geteuid() == 0:  
            os.system("shutdown -h now")
        else:
            print("otday prava")
    else:
        print(f"Неизвестная операционная система: {os_name}. Выключение не поддерживается(((((")
