from Funciones_grupal import *
from db_manager import *
flg_salir = True # Bucle principal

menu_general = "principal" # Manejo de los menús por estados (un string)
current_user = 0 # Constancia del usuario que está utilizando el programa
userList = get_user_ids() # Obtención de los usuarios existentes

while flg_salir:
    while menu_general == "principal": # Menú principal del programa
        opc = getOpt(show_project_title()+"1) Login\n2) Crear usuario\n3) Repeticiones de aventura\n4) Reportes\n5) Salir","\nElige tu opción: ",[1, 2, 3, 4,5],[],{})
        opc = int(opc)
        
        if opc == 1: # Login
            for i in range(3,0,-1):
                login_name = input("Nombre de usuario: ")
                login_passw = input("Contraseña: ")
                opc = checkUserbdd(login_name, login_passw)
                if opc == 0:
                    print("El usuario no existe. Te quedan {} intentos.".format(i))
                elif opc == -1:
                    print("La contraseña es incorrecta, intentalo de nuevo. Te quedan {} intentos.".format(i))
                else:
                    menu_general = "Play"
                    current_user = userList[1][userList[0].index(login_name)]
                    userList = get_user_ids()
                    break

        elif opc == 2: # Create User
            print("Creación de usuario")
            name = input("Nombre de usuario: ")
            while True:
                if not checkUser(name):
                    name = input("Nombre de usuario: ")
                elif user_exist(get_users(), name):
                    print("Este usuario ya existe.")
                    name = input("Nombre de usuario: ")
                else:
                    break
            passw = input("Contraseña: ")
            while True:
                if not checkPassword(passw):
                    passw = input("Contraseña: ")
                break
            insertUser(name,passw)
            menu_general = "Play"
            userList = get_user_ids()
            current_user = userList[1][userList[0].index(name)]

        elif opc == 3: # Replay
            menu_general = "Replay"

        elif opc == 4: # Reports
            print("Reportes")
            menu_general = "Reports"

        else:
            print("Hasta la próxima!")
            flg_salir = False

            menu_general = ""

    while menu_general == "Play": # Menú después de logearse
        opc = getOpt(show_project_title()+"\n1) Cerrar sesión\n2) Jugar\n3) Repeticiones de aventura\n4) Reportes\n5) Salir", "\nElige tu opción: ",
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
        else:
            print("Hasta la próxima!")
            flg_salir = False
            menu_general = ""

    while menu_general == "Reports":
        opc = getOpt(show_project_title()+"\n1) Respuestas más usadas\n2) Jugadores con mas partidas jugadas\n3) Partidas jugadas por usuario\n4) Volver", "\nElige tu opción: ",
                     [1, 2, 3, 4], [], {})
        opc = int(opc)

        if opc == 1: # Most used answer
            reporte = GetMostUsedAnswersReport()
            if reporte:
                print(getHeadeForTableFromTuples(
                    ("ID AVENTURA - NOMBRE", "ID PASO-DESCRIPCION", "ID RESPUESTA - DESCRIPCION",
                     "NUMERO VECES SELECCIONADA"),
                    (30, 30, 30, 30),
                    title="Respuestas más usadas"
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
            input("Continuar")
            limpiar_terminal()

        elif opc == 2:
            usuario,partidas = most_played_player()
            print(getHeadeForTableFromTuples(("NOMBRE USUARIO", "PARTIDAS JUGADAS"), (60, 60),
                                             title="Jugadores con mas partidas jugadas"))
            if usuario is not None:
                print("{:<60}{:<60}".format(str(usuario), str(partidas)))
            else:
                print("No se encontraron datos")
            input("Continuar")
            limpiar_terminal()
        elif opc == 3:
            name = input("Que usuario quieres ver? ")
            if checkUserbdd(name,"hola") == -1:
                aventuras = GetPlayerAdventureLog(name)
                if aventuras:
                    print(getHeadeForTableFromTuples(("Id_Adventure", "Name", "Date"), (40, 40, 40),
                                                     title="Partidas jugadas por"+name))
                    for fila in aventuras:
                        print("{:<40}{:<40}{:<40}".format(
                            str(fila["idadventure"]),
                            str(fila["Name"]),
                            str(fila["date"])))
                else:
                    print("El usuario no ha hecho ninguna aventura")
                input("Continuar")
            else:
                input("Usuario no existe")
        else:
            print("Salir")
            if current_user == 0:
                menu_general = "principal"

            else:
                menu_general = "Play"
        limpiar_terminal()

    while menu_general == "Replay":
        replayAdventures = getReplayAdventures()
        if not replayAdventures:
            print("No hay aventuras para reproducir.")
            input("Enter para continuar")
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
            datos += "Que aventura quieres visualizar?(+ siguiente | - anterior | 0 Volver): " 
            opc = input(datos).strip()
            if opc == "0":
                menu_general = "principal"
                break
            elif opc == "+" or opc == "-":
                start = ReplayStart(start, page_size, total, opc)
            elif opc.isdigit() and int(opc) in page_dict:
                idGame = int(opc)
                game = replayAdventures[idGame]
                print("Has seleccionado la partida", idGame)
                print("\n")
                id_adventure = game["idAdventure"]
                choices = getChoices(idGame)
                characterName = game["CharacterName"]
                replay(id_adventure,choices,characterName,game["Name"])
                menu_general = "principal"
                start = 0
                continue
            else:
                print("Opción inválida")
                input("Enter para continuar")

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
                show_fin()
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
