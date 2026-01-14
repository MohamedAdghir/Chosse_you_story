from Funciones_grupal import *
from  Variables import *
flg_salir = True
flg_00 = True
flg_01 = False
flg_02 = False
fgl_03 = False
fgl_04 = False

while flg_salir:
    while flg_00:
        opc = getOpt("1)Login\n2)Create user\n3)Replay Adventure\n4)Reports\n5)Exit","\nElige tu opción:",[1, 2, 3, 4,5],[],{})
        opc = int(opc)
        if opc == 1:
            print("Login")
            flg_01 = True
            flg_00 = False
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

            flg_01 = True
            flg_00 = False
        elif opc == 3:
            print("Replay Adventure")
        elif opc == 4:
            print("Reports")
            flg_03 = True
            flg_00 = False
        else:
            print("Exit")
            flg_salir = False
            flg_00 = False
    while flg_01:
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
            flg_03 = True
            flg_00 = False
        else:
            print("Exit")
            flg_salir = False
            flg_00 = False
    while flg_03:
        opc = getOpt("\n1)Most used answer\n2)PLayer with more games played\n3)Games played by user\n4)Back", "\nElige tu opción:",
                     [1, 2, 3, 4, 5], [], {})
        if opc == 1:
            print("Most used answer")
        elif opc == 2:
            print("PLayer with more games played")
        elif opc == 3:
            print("Games played by user")
        else:
            print("B")
            flg_salir = False
            flg_00 = False





