def mult_egyptian(max_, min_):
    list_ = [1]
    list_1 = [max_]
    last_index = 0
    # table de puissance de 2
    while list_[last_index] <= min_:
        list_.append(list_[last_index] + list_[last_index])
        list_1.append(list_1[last_index] + list_1[last_index])
        last_index = len(list_) - 1

    # suppression de l'excédant (1 valeur en plus dans la liste "non voulu")
    list_.pop(last_index)
    list_1.pop(last_index)

    # renverse les listes afin de faciliter le calcul des puissances de 2
    list_.reverse()
    list_1.reverse()
    result = 0

    # addition en fonction des puissances de 2 appartenant au plus petit nombre
    for i in range(len(list_)):
        if min_ - list_[i] >= 0:
            min_ -= list_[i]
            result += list_1[i]
        if min_ == 0:
            break

    return result
    

def main():
    number_1 = int(input('Entrer le premier nombre: '))
    number_2 = int(input('Entrer le deuxième nombre: '))
    max_ = max(number_1, number_2)
    min_ = min(number_1, number_2)
    print(f'--> {number_1} * {number_2} = {mult_egyptian(max_, min_)}')


if __name__ == "__main__":
    main()