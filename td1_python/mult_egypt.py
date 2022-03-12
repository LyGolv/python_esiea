def lower_exponent(number):
    exp_ = 0
    while(2 ** exp_ < number):
        exp_ += 1
    return exp_ - 1 if 2 ** exp_ > number else exp_


def exponent_list(number):
    list_ = []
    while(number > 0):
        exp_ = lower_exponent(number)
        list_.append(2 ** exp_ if exp_ > 0 else 1)
        number = number - 2 ** exp_
    return list_


def __main__():
    number_1 = int(input("Entrer le premier nombre: "))
    number_2 = int(input("Entre le deuxieme nombre: "))
    min_ = min(number_1, number_2)
    max_ = max(number_1, number_2)
    sum_exponent = sum(exponent_list(min_))
    result = 0
    for i in range(sum_exponent):
        result += max_
    print("Resultat:", result)


__main__()  