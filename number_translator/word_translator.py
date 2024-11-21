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

commands = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "делить": "/",
    "закрывается": ")",
    "открывается": "("
}

def translate_to_num(word):
    """Перевод из слов в символы"""
    user_command = word.split()
    current_nums = []
    current_num = None
    for elem in user_command:
        if elem in teens:
            current_num = (current_num or 0) + teens[elem]
        elif elem in tens:
            current_num = (current_num or 0) + tens[elem]
        elif elem in digits:
            current_num = (current_num or 0) + digits[elem]
        elif elem == "на": # Игнорируем слово "на"
            continue
        elif elem == "скобка": # Игнорируем слово "скобка"
            continue
        else:
            if current_num is not None:
                current_nums.append(current_num)
                current_num = None
            if elem in commands:
                current_nums.append(commands[elem])
    if current_num is not None:
        current_nums.append(current_num)
    return current_nums

def translate_to_word(num):
    """Перевод из символов в слова"""
    answer = []
    if 10 <=num<= 19:
        for key, value in teens.items():
            if value == num:
                answer.append(key)
    elif len(str(num)) == 2:
        for key, value in tens.items():
            if str(value)[0] == str(num)[0]:
                answer.append(key)
        for key, value in digits.items():
            if str(value)[0] == "0":
                continue
            if str(value)[0] == str(num)[1]:
                answer.append(key)
    elif len(str(num)) == 1:
        for key, value in digits.items():
            if value == num:
                answer.append(key)
    return " ".join(answer)
