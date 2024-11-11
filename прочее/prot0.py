# Словари для чисел и операций
NUMBERS = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20,
    "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
    "восемьдесят": 80, "девяносто": 90, "сто": 100
}

OPERATIONS = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "разделить": "/",
    "остаток от деления": "%"
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

# Функция для преобразования чисел в текстовый формат, включая числа больше 100
def number_to_text(number):
    if number in NUMBERS_REVERSE:
        return NUMBERS_REVERSE[number]
    elif number < 100:
        tens = (number // 10) * 10
        units = number % 10
        return f"{NUMBERS_REVERSE[tens]} {NUMBERS_REVERSE[units]}" if units > 0 else NUMBERS_REVERSE[tens]
    elif number < 1000:
        hundreds = (number // 100) * 100
        remainder = number % 100
        hundreds_text = f"{NUMBERS_REVERSE[hundreds // 100]}сот" if hundreds != 100 else "сто"
        if remainder > 0:
            return f"{hundreds_text} {number_to_text(remainder)}"
        return hundreds_text
    else:
        thousands = number // 1000
        remainder = number % 1000
        thousands_text = f"{number_to_text(thousands)} тысяч" if thousands != 1 else "тысяча"
        if remainder > 0:
            return f"{thousands_text} {number_to_text(remainder)}"
        return thousands_text

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
    elif operation == "%":
        result = num1 % num2
    
    # Переводим результат в текст
    if isinstance(result, float):
        return fractional_to_text(result)
    else:
        return number_to_text(result)

# Примеры использования
print(calculator("десять плюс пять"))                        # Простое сложение
print(calculator("сто тридцать плюс двадцать пять"))         # Сложение чисел больше 100
print(calculator("пять плюс ноль"))                          # Сложение с нулём
print(calculator("двадцать минус три"))                      # Простое вычитание
print(calculator("десять минус десять"))                     # Вычитание с результатом ноль
print(calculator("сто минус семьдесят"))                     # Вычитание с числом больше 100
print(calculator("шесть умножить на четыре"))                # Простое умножение
print(calculator("девяносто девять умножить девяносто девять"))  # Умножение с числом больше 100
print(calculator("пять умножить на ноль"))                   # Умножение на ноль
print(calculator("сорок восемь разделить на шесть"))         # Простое деление с целым результатом
print(calculator("пятьдесят разделить на три"))              # Деление с дробным результатом
print(calculator("тридцать два разделить на один"))          # Деление на 1
# print(calculator("двадцать разделить на ноль"))              # Попытка деления на ноль
print(calculator("семь остаток от деления пять"))            # Нахождение остатка
print(calculator("десять остаток от деления ноль"))          # Остаток от деления на ноль
print(calculator("двести пятьдесят плюс триста"))            # Сложение трёхзначных чисел
print(calculator("три минус пять"))                          # Вычитание с отрицательным результатом
print(calculator("девять умножить на десять"))               # Умножение на 10
print(calculator("сто двадцать умножить на семьдесят"))      # Комбинация операций с большими числами
print(calculator("двести пятьдесят умножить на пять"))       # Сложное число, превышающее тысячу
