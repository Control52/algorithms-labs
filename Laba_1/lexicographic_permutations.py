def next_permutation(array):
    """Меняет array на следующую перестановку. Возвращает True/False."""
    n = len(array)
    
    if n <= 1:                 
        return False
    
    i = n - 2
    while i >= 0 and array[i] >= array[i + 1]:
        i -= 1
        
    if i == -1:
        return False

    j = n - 1
    while array[j] <= array[i]:
        j -= 1

    array[i], array[j] = array[j], array[i]

    # Переворачиваем хвост
    left, right = i + 1, n - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
        
    return True


def generate_all_permutations_lex(items):
    """
    Записывает все перестановки в файл permutations.txt
    Выводит первые 5 в консоль
    """
    # Сортируем и копируем — чтобы не менять оригинал
    array = sorted(items)
    count = 0

    with open("permutations.txt", "w", encoding="utf-8") as f:
        print("Первые 5 перестановок:")
        
        
        if not array:
            print("Всего перестановок: 0")
            print("Готово! Все перестановки сохранены в permutations.txt")
            return
        
        while True:
            # Записываем текущую перестановку
            line = ' '.join(array)
            f.write(line + '\n')

            # Вывод первых пяти
            if count < 5:
                print(f"{count + 1:2d}. {line}")

            count += 1

            # Генерируем следующую
            if not next_permutation(array):
                break
            
    print(f"Всего перестановок: {count}")
    print("Все перестановки сохранены в permutations.txt")
    

arrays = [
    "Б12123-19.03.04ту", "Б12123-27.03.02ук", "Б12123-38.03.07тэ",
    "Б12124-19.03.01пб", "Б12124-19.03.01пби", "Б12124-19.03.01зб",
    "Б12124-19.03.04ту", "Б12124-27.03.02ммк", "Б12124-27.03.03тим",
]
# Запуск
generate_all_permutations_lex(arrays)

