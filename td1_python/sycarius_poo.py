class sycarius_serie:
    def __init__(self, star_number=0, size=10):
        self.start_number = star_number
        self.size = size

    def conjecture(self):
        list_ = [self.start_number]
        last_index = 0
        while list_[last_index] != 1:
            if list_[last_index] % 2:
                list_.append(list_[last_index] * 3 + 1)
            else:
                list_.append(list_[last_index] // 2)
            last_index = len(list_) - 1
        return list_

class sycarius_serie_file:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_list(self, list_):
        with open(self.file_name, "w") as file_:
            file_.write(', '.join(map(str, list_)))

    def get_list(self):
        with open(self.file_name, "r") as filin:
            list_ = list(map(int, filin.readline().split(", ")))
        return list_


def __main__():
    file_name = input('Nom du ficher: ')
    file_ = sycarius_serie_file(file_name)
    print("*****Menu*****")
    print("\t1. Sauvegarder une suite de Sycarius dans un fichier")
    print("\t2. Lire une suite de Sycarius à partir d'un fichier")
    choice = 0
    while choice < 1 or choice > 2:
        choice = int(input('Faite un choix: '))
    if choice == 1:        
        number = int(input("Enter un nombre: "))
        serie = sycarius_serie(number)            
        file_.save_list(serie.conjecture())
    else:
        print(f'{file_.get_list()}')

if __name__ == "__main__":
    __main__()