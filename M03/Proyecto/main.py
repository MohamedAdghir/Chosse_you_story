from Funciones_grupal import *
from  Variables import *
from  db_manager import *
flg_salir = True

menu_general = "Principal"

while flg_salir:
    while menu_general == "Principal":
        opc = getOpt("1)Login\n2)Create user\n3)Replay Adventure\n4)Reports\n5)Exit","\nElige tu opción:\n",[1, 2, 3, 4,5],[],{})
        opc = int(opc)
        print(get_users())
        if opc == 1:
            for i in range(3,0,-1):
                login_name = input("Username:\n")
                login_passw = input("Password:\n")
                opc = checkUserbdd(login_name, login_passw)
                if opc == 0:
                    print("The user does not exist. You have {} more attempts.".format(i))
                elif opc == -1:
                    print("The password is incorrect, please try again.You have {} more attempts.".format(i))
                else:
                    menu_general = "Play"
                    break
        elif opc == 2:
            print("Create User")
            name = input("Usename:\n")
            while True:
                if not checkUser(name):
                    name = input("Usename:\n")
                elif user_exist(get_users(), name):
                    print("User alredy in use")
                    name = input("Usename:\n")
                else:
                    break
            passw = input("Password:\n")
            while True:
                if not checkPassword(passw):
                    passw = input("Password:\n")
                break
            insertUser(name,passw)
            menu_general = "Play"
        elif opc == 3:
            print("Replay Adventure")
        elif opc == 4:
            print("Reports")
            menu_general = "Reports"
        else:
            print("Exit")
            flg_salir = False

            menu_general = ""
    while menu_general == "Play":
        opc = getOpt("\n1)Logout\n2)Play\n3)Replay Adventure\n4)Reports\n5)Exit", "\nElige tu opción:",
                     [1, 2, 3, 4, 5], [], {})
        opc = int(opc)

        if opc == 1:
            print("Logout")
            menu_general = "Principal"
        elif opc == 2:
            print("Play")
        elif opc == 3:
            print("Replay Adventure")
        elif opc == 4:
            print("Reports")
            menu_general = "Reports"
        else:
            print("Exit")
            flg_salir = False
            menu_general = ""
    while menu_general == "Reports":
        opc = getOpt("\n1)Most used answer\n2)PLayer with more games played\n3)Games played by user\n4)Back", "\nElige tu opción:",
                     [1, 2, 3, 4], [], {})
        opc = int(opc)

        if opc == 1:
            print("Most used answer")
        elif opc == 2:
            print("PLayer with more games played")
        elif opc == 3:
            print("Games played by user")
        else:
            print("Salir")
            flg_salir = False
            menu_general = ""





