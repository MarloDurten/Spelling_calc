vocabulary = {'один':"1",'два':"2",'три':"3",
             'четыре':"4",'пять':"5",'шесть':"6",
             'семь':"7",'восемь':"8",'девять':"9",
             'ноль':"0", 'одинадцать':"11", 'двенадцать':"12",
             'тринадцать':"13", 'четырнадцать':"14",'пятьнадцать':"15",
             'шестьнадцать':"16",'семьнадцать':"17",'восемьнадцать':"18",
             'девятьнадцать':"19",'двадцать':"20+",'тридцать':"30+",
             'сорок':"40+",'пятьдеся':"50+",'шестьдесят':"+60",
             'семьдесят':"70+",'восемьдесят':"+80",
             'девяносто':"90+",'сто':"100"}



num_form_num = vocabulary.values()
verb_form_num = vocabulary.keys()

signs = {'плюс':'+', 'минус':'-'}
verb_form_signs = signs.keys() 
sign_form_signs = signs.values()



def conv(input_str:str):

    expr= '' # от слова expresion
    # global verb_form_num
    # global verb_form_signs
    # global num_form_num
    # global sign_form_signs

    input_str = input_str.lower()
    input_str = input_str.split()

    for word in input_str: # проверка на число

        if word in verb_form_num:
            if word in verb_form_num:
                expr += vocabulary.get(word)

        elif word in verb_form_signs: # проверка на знак, если да то какой
            if word == 'плюс':
                expr += '+'

            elif word == 'минус':
                expr +='-'

        else:                       # Пропуск если гойда
            pass
    
    if expr[-1]=='+' or expr[-1]=='-':
        expr = expr[:-1]
    else:
        pass
    
    return expr



def resolve(expr):
    try:
        ans = eval(expr)
        return expr, ans
    except:
        return expr, KeyError



def verb_resolve(ans):
    ans = int(ans)

    hundreds = ans % 100
    tens = (ans // 10) % 10
    ones = (ans // 100) // 10

    print(hundreds,tens,ones)



while True:

    print(resolve(conv(input())))



# TO-DO
# 1. Сделать словестный вывод
# 2. Решить баг с деcяткой на конце (три минус двадцать) +
# 3. Реши костыль с плюсиками (надо доработать алгоритм и разделить его на две ступени)


       
 


























