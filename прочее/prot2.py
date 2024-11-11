NUMBERS = {"ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20,
    "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
    "восемьдесят": 80, "девяносто": 90}

OPERATIONS = {"плюс": "+", "минус": "-",
    "умножить": "*", "разделить": "/"}

# Функция для преобразования текста числа в числовой формат
def text_to_number(text):
    words = text.split()
    number = 0
    for word in words:
        number += NUMBERS.get(word, 0)
    return number

# Основная функция калькулятора
def calculator(text):
    words = text.split()
    num1_words = []
    operation = None
    num2_words = []
    
    # Разделяем текст на числа и операцию
    for word in words:
        if word in OPERATIONS:
            operation = OPERATIONS[word]
        elif operation is None:
            num1_words.append(word)
        else:
            num2_words.append(word)
    
    # Преобразуем текстовые числа в числовые
    num1 = text_to_number(" ".join(num1_words))
    num2 = text_to_number(" ".join(num2_words))
    
    # Выполняем операцию
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"

# Пример использования
print(calculator("семьдесят пять разделить три"))  