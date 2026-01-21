from Funciones_grupal import *
from  db_manager import *
from Variables import *
flg_salir = True

menu_general = "principal"
current_user = 0
userList = get_user_ids()
textVel = 0.05
while flg_salir:
    while menu_general == "principal":
        opc = getOpt("1)Login\n2)Create user\n3)Replay Adventure\n4)Reports\n5)Exit","\nElige tu opción:",[1, 2, 3, 4,5],[],{})
        opc = int(opc)
        if opc == 1:
            for i in range(3,0,-1):
                print(userList)
                login_name = input("Username:\n")
                login_passw = input("Password:\n")
                opc = checkUserbdd(login_name, login_passw)
                if opc == 0:
                    print("The user does not exist. You have {} more attempts.".format(i))
                elif opc == -1:
                    print("The password is incorrect, please try again.You have {} more attempts.".format(i))
                else:
                    menu_general = "Play"
                    current_user = userList[1][userList[0].index(login_name)]
                    userList = get_user_ids()
                    break
        elif opc == 2:
            print("Create User")
            name = input("Usename:\n")
            while True:
                if not checkUser(name):
                    name = input("Usename:\n")
                elif user_exist(get_users(), name):
                    print("User already in use")
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
            userList = get_user_ids()
            current_user = userList[1][userList[0].index(name)]
        elif opc == 3:
            menu_general = "Replay"
        elif opc == 4:
            print("Reports")
            menu_general = "Reports"
        else:
            print("Exit")
            flg_salir = False

            menu_general = ""

    while menu_general == "Play":
        opc = getOpt("\n1)Logout\n2)Play\n3)Replay Adventure\n4)Reports\n5)Configuración\n6)Exit", "\nElige tu opción:",
                     [1, 2, 3, 4, 5, 6], [], {})
        opc = int(opc)

        if opc == 1:
            menu_general = "principal"
        elif opc == 2:
            menu_general = "game_loop"
        elif opc == 3:
            menu_general = "Replay"
        elif opc == 4:
            menu_general = "Reports"
        elif opc == 5:
            menu_general = "config"
        else:
            print("Exit")
            flg_salir = False
            menu_general = ""

    while menu_general == "Reports":
        opc = getOpt("\n1)Most used answer\n2)PLayer with more games played\n3)Games played by user\n4)Back", "\nElige tu opción:",
                     [1, 2, 3, 4], [], {})
        opc = int(opc)
        if opc == 1:
            reporte = GetMostUsedAnswersReport()

            if reporte:

                print(getHeadeForTableFromTuples(
                    ("ID AVENTURA - NOMBRE", "ID PASO-DESCRIPCION", "ID RESPUESTA - DESCRIPCION",
                     "NUMERO VECES SELECCIONADA"),
                    (30, 30, 30, 30),
                    title="Most used answer"
                ))
                for fila in reporte:
                    datos_fila = (
                        str(fila["ID AVENTURA - NOMBRE"]),
                        str(fila["ID PASO - DESCRIPCION"]),
                        str(fila["ID RESPUESTA - DESCRIPCION"]),
                        str(fila["NUMERO VECES SELECCIONADA"])
                    )
                    print(getFormatedBodyColumns(datos_fila, (28, 28, 28, 28)))
            else:
                print("No hay datos para mostrar.")
            input("Continue")
            limpiar_terminal()
        elif opc == 2:
            usuario,partidas = most_played_player()
            print(getHeadeForTableFromTuples(("NOMBRE USUARIO", "PARTIDAS JUGADAS"), (60, 60),
                                             title="Player with more games played"))
            if usuario is not None:
                print("{:<60}{:<60}".format(str(usuario), str(partidas)))
            else:
                print("No se encontraron datos")
            input("Continue")
            limpiar_terminal()
        elif opc == 3:
            name = input("What user do you want to see?")
            if checkUserbdd(name,"hola") == -1:
                aventuras = GetPlayerAdventureLog(name)

                if aventuras:
                    print(getHeadeForTableFromTuples(("Id_Adventure", "Name", "Date"), (40, 40, 40),
                                                     title="Games played by "+name))
                    for fila in aventuras:
                        print("{:<40}{:<40}{:<40}".format(
                            str(fila["idadventure"]),
                            str(fila["Name"]),
                            str(fila["date"])))
                else:
                    print("El usuario no ha hecho ninguna aventura")
            else:
                input("Usuario no existe")

        else:
            print("Salir")
        input("Continue")
        limpiar_terminal()
        menu_general = "Play"

    while menu_general == "Replay":
        replayAdventures = getReplayAdventures()
        if not replayAdventures:
            print("No adventures to replay.")
            input("Enter to continue")
            menu_general = "principal"
            break
        show_relive_adventure()
        start = 0
        page_size = 5
        total = len(replayAdventures)
        keys = getReplayKeysSortedByDate(replayAdventures)
        while True:
            page_dict = getReplayPage(replayAdventures, keys, start, page_size)
            header = getHeadeForTableFromTuples(
            ("Id", "Username", "Name", "CharacterName", "date"),
            (6, 15, 40, 20, 24),"")
            datos = header + "\n"
            datos += getTableFromDict(("Username", "Name", "CharacterName", "date"),(6, 15, 40, 20, 24),page_dict) + "\n"
            datos += "Which adventure do you want to replay?(+ next | - prev | 0 Go back): \n" 
            opc = input(datos).strip()
            if opc == "0":
                menu_general = "principal"
                break
            elif opc == "+" or opc == "-":
                start = ReplayStart(start, page_size, total, opc)
            elif opc.isdigit() and int(opc) in page_dict:
                idGame = int(opc)
                game = replayAdventures[idGame]
                print("You selected the game", idGame)
                print("\n")
                id_adventure = game["idAdventure"]
                choices = getChoices(idGame)
                characterName = game["CharacterName"]
                replay(id_adventure,choices,characterName,game["Name"])
                menu_general = "principal"
                start = 0
                continue
            else:
                print("Invalid option")
                input("Enter to continue")

    while menu_general == "config":
        opc = getOpt("Velocidad de escritura de los textos:\n1)Instantaneo\n2)Rápido\n3)Normal\n4)Lento\n5)Back", "\nElige tu opción:",
                     [1, 2, 3, 4, 5], [], {})
        if opc == 1: # Instantaneo
            textVel = 0
        elif opc == 2: # Rapido
            textVel = 0.025
        elif opc == 3: # Normal
            textVel = 0.05
        elif opc == 4: # Lento
            textVel = 0.065
        else:
            menu_general = "Play"

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
        characterID = opc
        characterSelected = characters[opc]
        print("Has seleccionado al personaje {}!\n".format(characterSelected))
        input("Enter para continuar")

        # Obtener los pasos de la aventura
        adventure_steps = get_id_bystep_adventure(selectedAdventure)
        final_steps = []
        for step in adventure_steps:
            if adventure_steps[step]["Final_Step"] == 1:
                final_steps.append(step)

        first_step = get_first_step_adventure(selectedAdventure)
        current_step = first_step

        selectedOptions = []

        game_finished = False
        while not game_finished:
            limpiar_terminal()
            stepDisplay = getHeader(adventures[selectedAdventure]["Name"]) + "\n"
            answers = get_answers_bystep_adventure(current_step)
            if current_step in final_steps: # Es un final?
                stepDisplay += formatText(adventure_steps[current_step]["Description"].replace("$NAME",characterSelected),105,"\n")
                print(stepDisplay)
                print("Se acabo\n")
                selectedOptions.append((current_step,None))
                game_finished = True
                menu_general = "Play"
            # ----------------------------------------------------
            elif answers: # Tiene opciones?
                stepDisplay += formatText(adventure_steps[current_step]["Description"].replace("$NAME",characterSelected),105,"\n") + "\n"
                possibleAnswers = []
                for answer in answers:
                    possibleAnswers.append(answer[0])
                    stepDisplay += getFormatedAnswers(len(possibleAnswers), answers[answer]["Description"], 99, 3) + "\n"
                opc = getOpt(stepDisplay, "Selecciona una opción: ", range(1,len(possibleAnswers)+1))
                opc = possibleAnswers[int(opc)-1]
                if formatText(answers[(int(opc), current_step)]["Resolution_Answer"].replace("$NAME",characterSelected),105,"\n") != "":
                    resolution = "\n" + formatText(answers[(int(opc), current_step)]["Resolution_Answer"].replace("$NAME",characterSelected),105,"\n")
                    print(resolution)
                selectedOptions.append((current_step,int(opc)))
                current_step = answers[(int(opc), current_step)]["NextStep_Adventure"]
            # ----------------------------------------------------
            else: # No es final ni tiene opciones, un paso intermedio
                stepDisplay += formatText(adventure_steps[current_step]["Description"].replace("$NAME",characterSelected),105,"\n")
                print(stepDisplay)
                selectedOptions.append((current_step,None))
                current_step = adventure_steps[current_step]["Next_Step"]
            input("Enter para continuar")
        insertGame(current_user,characterID,selectedAdventure)
        gameList = getIdGames()
        lastGame = gameList[len(gameList)-1]
        for choice in selectedOptions:
            insertChoice(lastGame,choice[0],choice[1])
