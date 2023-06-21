import os.path
from prettytable import PrettyTable


print("""
                    __________ .__                    __        __________                __________         
                    \______   \|  |  _____     ____  |  | __    \____    /  ____    ____  \______   \   ____  
                     |    |  _/|  |  \__  \  _/ ___\ |  |/ /      /     / _/ __ \ _/ __ \  |       _/ _/ __ \ 
                     |    |   \|  |__ / __ \_\  \___ |    <      /     /_ \  ___/ \  ___/  |    |   \ \  ___/ 
                     |______  /|____/(____  / \___  >|__|_ \    /_______ \ \___  > \___  > |____|_  /  \___  >
                            \/            \/      \/      \/            \/     \/      \/         \/       \/

                                                                                     repertoire telephonique V-0-0-1
 06/21/2023-11:32                                                                                    
""")

table = PrettyTable(["NAME", "NUMBER CALL", "E-MAIL"])
print()
"""
        REPERTOIRE TELEPHONIQUE

        1- Nom
        2- Prenom
        3- Numero telephone
        4- Adresse mail

        STOCKER DANS UN FICHIER

        On demander a user son nom et autre on stock et on load

"""
file_name = "repertoire"


def get_three_information(who: bool):
    if who:
        name = input("Name : ")
        number_call = input("Cell : ")
        mail = input("Mail : ")
        return name, number_call, mail
    else:
        name = input("Name : ")
        return name


def ajouter_donner_file(file, data):
    data_chaine = ", ".join(data)
    if os.path.exists(file):
        with open(file, 'a') as f:
            f.write(data_chaine)
            f.write("\n")
    else:
        with open(file, 'w') as f:
            f.write(data_chaine)
            f.write("\n")


def data_corre_word(file):
    word = get_three_information(False)
    with open(file, 'r') as f:
        for element in f:
            element2 = element[0:len(element) - 1]
            for ele in element2.split(", "):
                if ele.lower() == word.lower():
                    data2 = element2.split(", ")
                    return data2
    print("")
    print("Le nom specifier n'est pas présent veuillez l'enregistrer ")
    input("Ok")
    exit(0)


def toute_les_data(file):
    name = []
    nb_call = []
    e_mail = []
    with open(file, 'r') as f:
        for element in f:
            element2 = element[0:len(element) - 1]
            x = element2.split(", ")
            a, b, c = x
            name.append(a)
            nb_call.append(b)
            e_mail.append(c)
    collect = list(zip(name, nb_call, e_mail))
    return collect


def put_data_in_the_table(the_table, file):
    collect_data = toute_les_data(file)
    for element in collect_data:
        the_table.add_row([*element])
    return the_table


print()
print("""REPERTOIRE TELEPHONIQUE
       vous souhaitez:
           1- consulter un contact
           2- ajouter un contact
           3- afficher tous les contacts
""")
while True:
    choix_str = input("Option : ")
    try:
        choix_int = int(choix_str)
    except:
        print("Saisie incorrect !!!!!!")
    else:
        break


match choix_int:
    case 1:
        data = data_corre_word(file_name)
        table.add_row([*data])
        print(table)
    case 2:
        ajouter_donner_file(file_name, get_three_information(True))
    case 3:
        to_print = put_data_in_the_table(table, file_name)
        print(to_print)
    case _:
        print("Error: option not available")


input("press 'enter' to close")