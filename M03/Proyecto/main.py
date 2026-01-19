from Funciones_grupal import *
from  Variables import *
from  db_manager import *
flg_salir = True

menu_general = "game_loop"

while flg_salir:
    while menu_general == "principal":
        opc = getOpt("1)Login\n2)Create user\n3)Replay Adventure\n4)Reports\n5)Exit","\nElige tu opción:",[1, 2, 3, 4,5],[],{})
        opc = int(opc)
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
            menu_general = "Replay"
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
            menu_general = "principal"
        elif opc == 2:
            menu_general = "game_loop"
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
    
    while menu_general == "Replay":
                print("")


    while menu_general == "game_loop":

        # Exportacion de datos que necesitamos para settear la aventura
        adventures = get_adventures_with_chars()
        characters = get_characters()

        # Eleccion de la aventura
        opc = getOpt(getFormatedAdventures(), "Selecciona una aventura (0 para volver atrás): ", adventures,[0])
        if int(opc) == 0:
            menu_general = "Play"
            break
        selectedAdventure = int(opc)

        # ----- Elegir el personaje para la aventura: -----
        characterSelectorDisplay = getHeader(adventures[selectedAdventure]["Name"]) + "\n"
        characterSelectorDisplay += getFormatedBodyColumns(("Aventura:", adventures[selectedAdventure]["Name"]),(20,85),0) + "\n"
        characterSelectorDisplay += getFormatedBodyColumns(("Descripción:", adventures[selectedAdventure]["Description"]),(20,85),0) + "\n"
        characterSelectorDisplay += "Personajes disponibles".center(45,"=") + "\n"
        for character in adventures[selectedAdventure]["Characters"]:
            characterSelectorDisplay += "{:3}) {:50}\n".format(character,characters[character])
        opc = getOpt(characterSelectorDisplay, "Selecciona un personaje (0 para volver atrás): ", adventures[selectedAdventure]["Characters"],[0])
        opc = int(opc)
        if opc == 0:
            break
        characterSelected = characters[opc]
        print("Has seleccionado al personaje {}!\n".format(characterSelected))
        input("Enter para continuar")

        # Obtener los pasos de la aventura
        adventure_steps = get_id_bystep_adventure()
        final_steps = []
        for step in adventure_steps:
            if adventure_steps[step]["Final_Step"] == 1:
                final_steps.append(step)

        first_step = get_first_step_adventure(selectedAdventure)
        current_step = first_step

        game_finished = False
        while not game_finished:
            limpiar_terminal()
            stepDisplay = getHeader(adventures[selectedAdventure]["Name"]) + "\n"
            answers = get_answers_bystep_adventure(current_step)
            if current_step in final_steps: # Es un final?
                stepDisplay += formatText(adventure_steps[current_step]["Description"],105,"\n").replace("$NAME",characterSelected)
                print(stepDisplay)
                print("Se acabo\n")
                game_finished = True
                menu_general = "Play"
            elif answers: # Tiene opciones?
                stepDisplay += formatText(adventure_steps[current_step]["Description"],105,"\n").replace("$NAME",characterSelected) + "\n"
                possibleAnswers = []
                for answer in answers:
                    possibleAnswers.append(answer[0])
                    stepDisplay += getFormatedAnswers(answer[0], answers[answer]["Description"], 99, 3) + "\n"
                opc = getOpt(stepDisplay, "Selecciona una opción: ", possibleAnswers)
                resolution = "\n" + formatText(answers[(int(opc), current_step)]["Resolution_Answer"],105,"\n").replace("$NAME",characterSelected)
                print(resolution)
            else: # No es final ni tiene opciones, un paso intermedio -hector: jejegod
                stepDisplay += formatText(adventure_steps[current_step]["Description"],105,"\n").replace("$NAME",characterSelected)
                print(stepDisplay)
                print("paso intermedio\n")
            input("Enter para continuar")
            current_step = answers[(int(opc), current_step)]["NextStep_Adventure"]