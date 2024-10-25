digits = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
}

teens = {
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
}

tens = {
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
}

def translate_to_num(word):
    user_command = word.split()
    current_nums = []
    current_num = 0
    for elem in user_command:
        if elem in teens:
            current_num += teens[elem]
        elif elem in tens:
            current_num += tens[elem]
        elif elem in digits:
            current_num += digits[elem]
        else:
            current_nums.append(current_num)
            current_num = 0
    current_nums.append(current_num)
    return current_nums

def translate_to_word(word):
    return