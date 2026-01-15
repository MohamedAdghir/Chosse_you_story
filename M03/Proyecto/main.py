from Funciones_grupal import *
from  Variables import *
flg_salir = True


menu_general = "principal"
while flg_salir:
    while menu_general == "principal":
        opc = getOpt("1)Login\n2)Create user\n3)Replay Adventure\n4)Reports\n5)Exit","\nElige tu opción:",[1, 2, 3, 4,5],[],{})
        opc = int(opc)
        if opc == 1:
            print("Login")
            menu_general = "play"
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
            menu_general = "play"
        elif opc == 3:
            print("Replay Adventure")
        elif opc == 4:
            print("Reports")
            menu_general = "reports"
        else:
            print("Exit")
            flg_salir = False
            menu_general = ""
    while menu_general == "play":
        opc = getOpt("\n1)Logout\n2)Play\n3)Replay Adventure\n4)Reports\n5)Exit", "\nElige tu opción:",
                     [1, 2, 3, 4, 5], [], {})
        if opc == 1:
            print("Logout")
            flg_00= True
            flg_01 = False
        elif opc == 2:
            print("Play")
        elif opc == 3:
            print("Replay Adventure")
        elif opc == 4:
            print("Reports")
            menu_general = "reports"
        else:
            print("Exit")
            flg_salir = False
            menu_general = ""
    while menu_general == "reports":
        opc = getOpt("\n1)Most used answer\n2)PLayer with more games played\n3)Games played by user\n4)Back", "\nElige tu opción:",
                     [1, 2, 3, 4, 5], [], {})
        if opc == 1:
            print("Most used answer")
        elif opc == 2:
            print("PLayer with more games played")
        elif opc == 3:
            print("Games played by user")
        else:
            flg_salir = False
            menu_general = ""





