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

# Приоритет операций
OP_PRIORITY = {
    "+": 1, "-": 1, "*": 2, "/": 2, "%": 2
}

# Обратный словарь для чисел
NUMBERS_REVERSE = {v: k for k, v in NUMBERS.items()}

# Преобразование текста в число
def text_to_number(text):
    is_negative = text.startswith("минус")
    if is_negative:
        text = text[6:]  # Убираем "минус"
    words = text.split()
    number = 0
    for word in words:
        number += NUMBERS.get(word, 0)
    return -number if is_negative else number

# Преобразование числа в текст
def number_to_text(number):
    if number < 0:
        return "минус " + number_to_text(-number)
    elif number in NUMBERS_REVERSE:
        return NUMBERS_REVERSE[number]
    elif number < 100:
        tens = (number // 10) * 10
        units = number % 10
        return f"{NUMBERS_REVERSE[tens]} {NUMBERS_REVERSE[units]}" if units > 0 else NUMBERS_REVERSE[tens]
    elif number == 100:
        return "сто"
    else:
        return str(number)

# Преобразование дробного числа в текст
def fractional_to_text(value):
    integer_part = int(value)
    fractional_part = value - integer_part
    
    integer_text = number_to_text(integer_part)
    if fractional_part == 0:
        return integer_text
    else:
        repeating_fraction = round(fractional_part, 1)
        if repeating_fraction == 0.3333:
            return f"{integer_text} целых и три в периоде"
        elif repeating_fraction == 0.6666:
            return f"{integer_text} целых и шесть в периоде"
        else:
            fractional_text = str(round(fractional_part * 10))
            return f"{integer_text} целых и {fractional_text}"

# Преобразование выражения в ОПН
def to_rpn(expression):
    output = []
    operators = []
    
    for token in expression:
        if isinstance(token, int):
            output.append(token)
        elif token in OP_PRIORITY:
            while (operators and operators[-1] in OP_PRIORITY and
                   OP_PRIORITY[operators[-1]] >= OP_PRIORITY[token]):
                output.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()  # Удалить "("

    while operators:
        output.append(operators.pop())
    return output

# Выполнение операций
def eval_rpn(rpn_expression):
    stack = []
    for token in rpn_expression:
        if isinstance(token, int):
            stack.append(token)
        elif token in OPERATIONS.values():
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b if b != 0 else "Ошибка: деление на ноль")
            elif token == "%":
                stack.append(a % b if b != 0 else "Ошибка: остаток от деления на ноль")
    return stack[0]

# Основная функция калькулятора
def calculator(text):
    words = text.split()
    expression = []
    i = 0

    while i < len(words):
        word = words[i]
        if word == "минус" and (i == 0 or words[i - 1] in OPERATIONS or words[i - 1] == "("):
            # Обработка отрицательного числа
            number = text_to_number(" ".join(words[i:i+2]))
            expression.append(number)
            i += 2
        elif word in NUMBERS:
            number_text = [word]
            i += 1
            while i < len(words) and words[i] in NUMBERS:
                number_text.append(words[i])
                i += 1
            number = text_to_number(" ".join(number_text))
            expression.append(number)
        elif word in OPERATIONS:
            operation = OPERATIONS[word]
            expression.append(operation)
            i += 1
        elif word == "(":
            expression.append("(")
            i += 1
        elif word == ")":
            expression.append(")")
            i += 1
        else:
            i += 1

    # Перевод выражения в ОПН
    rpn_expression = to_rpn(expression)
    
    # Вычисление выражения
    result = eval_rpn(rpn_expression)

    # Перевод результата в текст
    if isinstance(result, float):
        return fractional_to_text(result)
    elif isinstance(result, int):
        return number_to_text(result)
    else:
        return result

# Тесты
print(calculator("десять плюс пять"))                        
print(calculator("семь плюс семь плюс семь плюс семь умножить семь"))       
print(calculator("пять плюс ноль"))                          
print(calculator("двадцать минус три"))                      
print(calculator("десять минус десять"))                     
print(calculator("сто минус семьдесят"))                     
print(calculator("шесть умножить на четыре"))                
print(calculator("девяносто девять умножить девяносто девять"))  
print(calculator("пять умножить на ноль"))                   
print(calculator("сорок восемь разделить на шесть"))         
print(calculator("пятьдесят разделить на три"))              
print(calculator("тридцать два разделить на один"))          
print(calculator("двадцать разделить на ноль"))              
print(calculator("семь остаток от деления пять"))            
print(calculator("десять остаток от деления ноль"))                   
print(calculator("три минус пять"))                          
print(calculator("девять умножить на десять"))