import number_translator
from number_translator import *




def calc(user_input):
    current_nums = translate_to_num(user_input)
    current_command = ''.join(str(x) for x in current_nums)
    result = eval(current_command)
    return translate_to_word(result)

print(calc("двадцать пять плюс тринадцать"))
print(calc("пять плюс два умножить на три минус один"))
print(calc("скобка открывается пять плюс два скобка закрывается умножить на три минус один"))
print(calc("пять минус минус один"))