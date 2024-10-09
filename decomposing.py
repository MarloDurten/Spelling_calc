
vocabulary = {'один':"1",'два':"2",'три':"3",
             'четыре':"4",'пять':"5",'шесть':"6",
             'семь':"7",'восемь':"8",'девять':"9",
             'ноль':"0",}

verb_form_num = vocabulary.keys()

verb_form_signs = ('плюс', 'минус')

input_massege = input('Введите запрос: ')
input_massege = input_massege.lower()
input_massege_splited = input_massege.split()


expr = ''

for word in input_massege_splited:
    if word in verb_form_num:
        expr += vocabulary.get(word)
    elif word in verb_form_signs:
        if word == 'плюс':
            expr += '+'
        else:
            expr +='-'
    else:
        pass

result = eval(expr)
print(result)

# result=0
# q = 0
# stete = None
# for word in input_massege_splited:
#     if word in verb_form_num:
#         q = vocabulary.get(word)
#     elif word in verb_form_signs:
#         if word == 'плюс':
#             result += q
#             q = 0
#         elif word == 'минус':
#             result -= q
#     else:
#         pass




