import random

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


# Пример использования с генерацией случайных карт:
def generate():
    """Генерирует случайную покерную руку из 5 карт (числа от 1 до 13)."""
    sidebar = [random.randint(1, 10) for _ in range(5)]  # Диапазон от 1 до 13
    return sidebar

random_sidebar = generate()
way = method(random_sidebar)

print(f"Рука: {random_sidebar}")
print(f"Комбинация: {way}")