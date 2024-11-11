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

# Функция для преобразования чисел в текстовый формат, включая числа больше 1000
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
    elif number < 1000000:
        thousands = number // 1000
        remainder = number % 1000
        thousands_text = f"{number_to_text(thousands)} тысяч" if thousands != 1 else "тысяча"
        if remainder > 0:
            return f"{thousands_text} {number_to_text(remainder)}"
        return thousands_text
    else:
        return str(number)  # Вывод для чисел больше миллиона в числовом виде

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
    i = 0
    while i < len(words):
        word = words[i]
        # Проверка на составные операции, как "остаток от деления"
        if word == "остаток" and i + 2 < len(words) and words[i + 1] == "от" and words[i + 2] == "деления":
            operation = "%"
            i += 3  # Пропустить слова "остаток от деления"
        elif word in OPERATIONS:
            operation = OPERATIONS[word]
            i += 1
        elif operation is None:
            num1_words.append(word)
            i += 1
        else:
            num2_words.append(word)
            i += 1
    
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
        result = num1 % num2 if num2 != 0 else "Ошибка: остаток от деления на ноль"
    
    # Переводим результат в текст
    if isinstance(result, float):
        return fractional_to_text(result)
    elif isinstance(result, int) and result >= 0:
        return number_to_text(result)
    else:
        return "Отрицательный результат не поддерживается"

# Примеры тестов для проверки
print("1) " + calculator("десять плюс пять"))                        
print("2) " + calculator("сто тридцать плюс двадцать пять"))         
print("3) " + calculator("пять плюс ноль"))                          
print("4) " + calculator("двадцать минус три"))                      
print("5) " + calculator("десять минус десять"))                     
print("6) " + calculator("сто минус семьдесят"))                     
print("7) " + calculator("шесть умножить на четыре"))                
print("8) " + calculator("девяносто девять умножить девяносто девять"))  
print("9) " + calculator("пять умножить на ноль"))                   
print("10) " + calculator("сорок восемь разделить на шесть"))         
print("11) " + calculator("пятьдесят разделить на три"))              
print("12) " + calculator("тридцать два разделить на один"))          
print("13) " + calculator("двадцать разделить на ноль"))              
print("14) " + calculator("семь остаток от деления пять"))            
print("15) " + calculator("десять остаток от деления ноль"))          
print("16) " + calculator("двести пятьдесят плюс триста"))            
print("17) " + calculator("три минус пять"))                          
print("18) " + calculator("девять умножить на десять"))               
print("19) " + calculator("сто двадцать умножить на семьдесят"))      
print("20) " + calculator("двести пятьдесят умножить на пять"))       
