# Словари для чисел и операций
NUMBERS = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20,
    "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
    "восемьдесят": 80, "девяносто": 90
}

OPERATIONS = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "разделить": "/"
}

# Обратный словарь для чисел
NUMBERS_REVERSE = {v: k for k, v in NUMBERS.items()}

# Функция для преобразования текстового числа в числовой формат
def text_to_number(text):
    words = text.split()
    number = 0
    for word in words:
        number += NUMBERS.get(word, 0)
    return number

# Функция для преобразования чисел в текстовый формат
def number_to_text(number):
    if number in NUMBERS_REVERSE:
        return NUMBERS_REVERSE[number]
    elif number < 100:
        tens = (number // 10) * 10
        units = number % 10
        return f"{NUMBERS_REVERSE[tens]} {NUMBERS_REVERSE[units]}" if units > 0 else NUMBERS_REVERSE[tens]
    else:
        return str(number)  # Для чисел больше 99 возвращаем просто числом

# Функция для перевода дробного результата в текст
def fractional_to_text(value):
    integer_part = int(value)
    fractional_part = value - integer_part
    
    # Преобразуем целую часть
    integer_text = number_to_text(integer_part)
    
    # Проверяем, является ли дробная часть периодической
    if fractional_part == 0:
        return integer_text
    else:
        repeating_fraction = round(fractional_part, 1)  # Округляем до одного знака
        if repeating_fraction == 0.3333:
            return f"{integer_text} целых и три в периоде"
        elif repeating_fraction == 0.6666:
            return f"{integer_text} целых и шесть в периоде"
        else:
            fractional_text = str(round(fractional_part * 10))  # Вывод первой цифры дробной части
            return f"{integer_text} целых и {fractional_text}"

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
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
    
    # Переводим результат в текст
    if isinstance(result, float):
        return fractional_to_text(result)
    else:
        return number_to_text(result)

# Примеры использования
print(calculator("шесть умножить на три"))  # Вывод: восемнадцать
print(calculator("девяносто умножить девяносто"))  # Вывод: шестнадцать целых и шесть в периоде
