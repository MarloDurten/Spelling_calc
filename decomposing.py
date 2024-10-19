vocabulary = {'один':"1",'два':"2",'три':"3",
             'четыре':"4",'пять':"5",'шесть':"6",
             'семь':"7",'восемь':"8",'девять':"9",
             'ноль':"0",}



verb_form_num = vocabulary.keys()

verb_form_signs = ('плюс', 'минус')

input_massege = input('Введите запрос: ')
input_massege = input_massege.lower()
input_massege_splited = input_massege.split()



def resolve(input):
    expr= ''
    global verb_form_num
    global verb_form_signs

    for word in input: # проверка на число
        if word in verb_form_num:
            expr += vocabulary.get(word)

        elif word in verb_form_signs: # проверка на знак, если да то какой
            if word == 'плюс':
                expr += '+'

            else:
                expr +='-'

        else:                       # Пропуск если гойда 
            pass

    return expr

print(resolve(input_massege_splited))


