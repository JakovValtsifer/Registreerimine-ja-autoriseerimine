import random

def auto_generate_password():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    password = "".join([random.choice(ls) for x in range(12)])
    return password

def register_user(logins, passwords):
    login = input("Login: ")
    while login in logins:
        login = input("See sisselogimine on juba võetud. Sisestage teine sisselogimine: ")
    password_choice = input("Sisestage 1 parooli automaatseks genereerimiseks või 2 isegenereeriva parooli loomiseks: ")
    if password_choice == "1":
        password = auto_generate_password()
        print("Teie parool: " + password)
    elif password_choice == "2":
        password =  input("Sisestage oma parool: ")
        while not any(char.isdigit() for char in password) or not any(char.islower() for char in password) or not any(char.isupper() for char in password) or not any(char in ".,:;!_*-+()/#¤%&" for char in password):
            password = input("Parool peab sisaldama numbreid, väike- ja suurtähti ning eritähti. Märki. Sisestage parool uuesti: ")
    else:
        print("Vale valik.")
        return None, None
    logins.append(login)
    passwords.append(password)
    print("Registreerimine on edukas!")
    return login, password

def authorize_user(logins, passwords):
    login = input("Login: ")
    password = input("Sisestage oma parool: ")
    if login in logins and passwords[logins.index(login)] == password:
        print("Autoriseerimine oli edukas!")
    else:
        print("Vale kasutajanimi või parool.")
