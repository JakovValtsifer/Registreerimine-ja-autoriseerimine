import Mymodule

logins = []
passwords = []

while True:
    choice = input("Sisestage 1 registreerimiseks, 2 loa saamiseks või 3 väljumiseks: ")
    if choice == "1":
        login, password = Mymodule.register_user(logins, passwords)
        if login is not None and password is not None:
            logins.append(login)
            passwords.append(password)
    elif choice == "2":
        Mymodule.authorize_user(logins, passwords)
    elif choice == "3":
        break
    else:
        print("Vale valik.")

