def sycarius_conjecture(nb):
    list_ = [nb]
    last_index = 0
    while list_[last_index] != 1:
        if list_[last_index] % 2:
            list_.append(list_[last_index] * 3 + 1)
        else:
            list_.append(list_[last_index] // 2)
        last_index = len(list_) - 1
    return list_

start_number = int(input("Donner la debut de la liste: "))

print(len(sycarius_conjecture(start_number)))