import number_translator
from number_translator import *


commands = ["плюс", "минус", "умножить на", "делить на"]

def calc(user_input):
    current_nums = translate_to_num(user_input)
    user_command = user_input.split()
    for word in user_command:
        if word in commands:
            if word == "плюс":
                result = current_nums[0] + current_nums[1]
            elif word == "минус":
                result = current_nums[0] - current_nums[1]
            elif word == "умножить на":
                result = current_nums[0] * current_nums[1]
            elif word == "делить на":
                result = current_nums[0] // current_nums[1]
    return result

print(calc("двадцать пять минус пять"))