import  datetime
import time
import os
from db_manager import *

# Funciones chidas
def limpiar_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y macOS
        os.system('clear')

# Funcion para formatear texto
def formatText(text, lenLine, split):
    formatedText = ""
    start = 0
    end = 0

    while end < len(text):
        if text[end] == " ":
            start = end + 1
            end += lenLine + 1
        else:
            start = end
            end += lenLine

        if end >= len(text):
            slicedText = text[start:]
            formatedText += slicedText + "\n"
        else:
            if text[end] != " ":
                space = text[start:end].rfind(" ")
                if space != -1:
                    end = start + space

            slicedText = text[start:end]
            formatedText += slicedText + split

    return formatedText

# Funcion para formatear textos en columnas
def getFormatedBodyColumns(texts,lenLines,margin=2):
    formatedColumns = []
    finalText = ""
    for i in range(len(texts)):
        formatedColumns.append([])
        formatedText = formatText(texts[i],lenLines[i],"\n")
        start = 0
        end = 0
        for j in range(formatedText.count("\n")):
            end = formatedText.find("\n", start)
            formatedColumns[i].append(formatedText[start:end])
            start = end + 1

    maxLine = 0
    for text in formatedColumns:
        if len(text) > maxLine:
            maxLine = len(text)
            
    for i in range(len(formatedColumns)):
        while len(formatedColumns[i]) != maxLine:
            formatedColumns[i].append("")

    for i in range(maxLine):
        for j in range(len(formatedColumns)):
            finalText += formatedColumns[j][i].ljust(lenLines[j]," ")
            if j != len(formatedColumns)-1:
                finalText += "".ljust(margin," ")
        finalText += "\n"

    return finalText

#Funcion de las opciones del menu
def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[], dictionary={}):
    opciones_validas = []
    for a in rangeList:
        opciones_validas.append(str(a))
    for a in exceptions:
        opciones_validas.append(str(a))
    for a in dictionary.keys():
        opciones_validas.append(str(a))
    while True:
        limpiar_terminal()
        print(textOpts)
        opc = input(inputOptText).strip()
        if opc in opciones_validas:
            return opc
        print("Opción inválida. Intenta de nuevo.\n")
        input("Enter para continuar")

#Funcion de comprobar que la contraseña cumpla con los parametros
def checkPassword(password):
    if not 8 <= len(password) <= 12:
        print("La contraseña debe tener entre 8 y 12 caracteres.")
        return False
    if " " in password:
        print("La contraseña no puede contener espacios.")
        return False
    carac_upper = False
    carac_lower = False
    carac_digit = False
    carac_special = False
    for c in password:
        if c.isupper():
            carac_upper = True
        elif c.islower():
            carac_lower = True
        elif c.isdigit():
            carac_digit = True
        elif not c.isalnum():
            carac_special = True
    if not carac_upper:
        print("Falta al menos una letra mayúscula.")
        return False
    if not carac_lower:
        print("Falta al menos una letra minúscula.")
        return False
    if not carac_digit:
        print("Falta al menos un número.")
        return False
    if not carac_special:
        print("Falta al menos un carácter especial.")
        return False
    return True

#Funcion de comprobar que el usuario cumpla con los parametros
def checkUser(user):
    if len(user) not in range(6,11):
        print("Invalid range")
        return False
    elif not user.isalnum():
        print("Only numbers and characters")
        return False
    return True

#Funcion para los encabezados
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    suma = 0
    texto = ""
    for a in t_size_columns:
        suma = suma + a
    texto = title.center(suma,"*") + "\n"
    for i in range(len(t_name_columns)):
        texto += t_name_columns[i].ljust(t_size_columns[i])
    
    texto += "\n" + "".center(suma,"*")
    return texto

#print(getHeadeForTableFromTuples(("Id", "Username", "Name", "CharacterName", "date"),(6, 15, 35, 20, 25),"")))

# Funcion que crea un header
def getHeader(text):
    texto = "".center(105,"*") + "\n" + text.center(105,"=") + "\n" + "".center(105,"*")
    return texto

texto = "Narrador: Y entonces, un día, ocurrió algo muy peculiar. Algo que cambiaría para siempre a $NAME. Algo que nunca olvidaría. Llevaba casi una hora sentado en su escritorio cuando se dio cuenta de que no había llegado ni una sola orden al monitor para que él la siguiese. Nadie había aparecido para darle instrucciones, convocar una reunión o siquiera saludarle. En todos sus años en la empresa nunca había ocurrido algo así, ese aislamiento total. Era evidente que algo iba muy mal. Conmocionado, paralizado, $NAME se encontró incapaz de moverse durante un buen rato. Pero cuando recuperó el juicio y los sentidos, se levantó de su escritorio y salió de su oficina."
def getFormatedAnswers(id_respuesta, texto, longitud_linea, margen_derecho):
    prefijo = margen_derecho * " " + "{}) ".format(id_respuesta)
    sangria = " " * len(prefijo)

    resultado = prefijo
    linea_actual = prefijo
    palabra = ""

    for caracter in texto:
        if caracter != " ":
            palabra += caracter
        else:
            if len(linea_actual) + len(palabra) + 1 > longitud_linea:
                resultado += "\n{}{} ".format(sangria, palabra)
                linea_actual = "{}{} ".format(sangria, palabra)
            else:
                resultado += "{} ".format(palabra)
                linea_actual += "{} ".format(palabra)

            palabra = ""

    if palabra:
        if len(linea_actual) + len(palabra) > longitud_linea:
            resultado += "\n{}{}".format(sangria, palabra)
        else:
            resultado += "{}".format(palabra)

    return resultado

#print(getFormatedAnswers(1, texto, 99, 3))

def writeText(texto, retraso_base=0.05):
    for caracter in texto:
        print(caracter, end='', flush=True)
        
        if caracter in ',;':
            time.sleep(retraso_base * 8)  # pausa corta
        elif caracter in '.!?':
            time.sleep(retraso_base * 12)  # pausa larga
        else:
            time.sleep(retraso_base)  # retraso normal
    print()  # salto de línea al final

def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    lista = list(dict_of_data)
    resultText = ""
    for pasada in range(len(lista) - 1):
        cambios = False
        for i in range(len(lista) - 1 - pasada):
             if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                cambios = True
        if not cambios:
            break
    for i in range(len(lista)):
        texto = str(lista[i]).ljust(weigth_of_columns[0])
        for j in range(len(tuple_of_keys)-1):
            texto = texto +str(dict_of_data[lista[i]][tuple_of_keys[j]]).ljust(weigth_of_columns[j+1])
        texto = texto + str(dict_of_data[lista[i]][tuple_of_keys[len(tuple_of_keys)-1]])
        resultText += texto + "\n"
    return resultText


#lista = get_users()
#usario = "Tester"
#print(lista)

def user_exist(lista,usuario):
    lista = list(lista)
    if usuario in lista:
        return True
    else:
        return False

#print(user_exist(lista,usario))

def getFormatedAdventures():
    adventures = get_adventures_with_chars()
    body = getHeadeForTableFromTuples(("Id Adventure", "Adventure", "Description"), (15, 22, 68), "Adventures")
    for idAdventure in adventures:
        texts = [
            str(idAdventure),
            adventures[idAdventure]["Name"],
            adventures[idAdventure]["Description"]]
        lenLines = [13, 20, 66]

        body += getFormatedBodyColumns(texts, lenLines) + "\n"
    return body


def replay(idAdventure,choices,characterName,adventureName):
    adventure_steps = get_id_bystep_adventure(idAdventure)
    
    for step_id, answer_id in choices:
        #limpiar_terminal()
        print(getHeader(adventureName))
        #mostrar la description del paso
        step_text = adventure_steps[step_id]["Description"]
        step_text = step_text.replace("$NAME",characterName)
        print(formatText(step_text, 105, "\n"))
        input("Enter to continue")

        # mostrar la opcion seleccionada y resolution
        answers = get_answers_bystep_adventure(step_id)
        if not answers:
            print("\n(No decision was required in this step)")
            continue
        print("\nOptions:")
        for (ans_id, _), data in answers.items():
            option_text = data["Description"].replace("$NAME", characterName)
            print(getFormatedAnswers(ans_id, option_text, 105, 3))
        input("Enter to see what you chose")
        chosen_text = answers[(answer_id, step_id)]["Description"]
        chosen_text = chosen_text.replace("$NAME", characterName)
        print("\nYou chose option", answer_id)
        print(getFormatedAnswers(answer_id, chosen_text, 105, 3))
        input("Enter to see the result")
        #print(getHeader(adventureName))
        resolution = answers[(answer_id, step_id)]["Resolution_Answer"]
        resolution = resolution.replace("$NAME",characterName)
        print(formatText(resolution, 105, "\n"))
        input("Enter to continue")
    show_fin()

#print(getFormatedAdventures())

def ReplayStart(start, page_size, total, option):
    if option == "+":
        if start + page_size < total:
            start = start + page_size
    elif option == "-":
        if start - page_size >= 0:
            start = start - page_size
    return start

def getReplayPage(replayAdventures, keys, start, page_size):
    page_dict = {}
    end = start + page_size

    for i in range(start, end):
        if i >= len(keys):
            break
        page_dict[keys[i]] = replayAdventures[keys[i]]

    return page_dict

def getReplayKeysSortedByDate(replayAdventures):
    keys = list(replayAdventures.keys())

    for pasada in range(len(keys) - 1):
        cambios = False
        for i in range(len(keys) - 1 - pasada):
            date1 = replayAdventures[keys[i]]["date"]
            date2 = replayAdventures[keys[i + 1]]["date"]

            if date1 > date2:
                keys[i], keys[i + 1] = keys[i + 1], keys[i]
                cambios = True

        if not cambios:
            break

    return keys


#replayAdventures = getReplayAdventures()
#getTableFromDict(("Username", "Name", "CharacterName", "date"),(6, 15, 35, 20, 25),replayAdventures)
def show_relive_adventure():
    limpiar_terminal()
    print(r"""
_/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\_
\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /
/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\_
          
    ___ ___ _    _____   _______ 
    | _ \ __| |  |_ _\ \ / / __|
    |   / _|| |__ | | \ V /| _| 
    |_|_\___|____|___| \_/ |___|
          
    __   _____  _   _ ___ 
    \ \ / / _ \| | | | _ \
     \ V / (_) | |_| |   /
      |_| \___/ \___/|_|_\

     __   __        ___      ___      __   __ 
     /\  |  \ \  / |__  |\ |  | |  | |__) |__  
    /~~\ |__/  \/  |___ | \|  | \__/ |  \ |__ 

_/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\_
\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /
/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\_
""")
    input("Enter to continue")



def show_fin():
    limpiar_terminal()
    print(r"""
_/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\_
\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /
/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\_

     ______ _____ _   _
    |  ____|_   _| \\ | |
    | |__    | | |  \\| |
    |  __|   | | | . ` |
    | |     _| |_| |\\  |
    |_|    |_____|_| \\_|

_/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\_
\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /
/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\_
""")
    input("Enter to continue")



def show_project_title():
    limpiar_terminal()
    return r"""
****************************************************************************************************                                                                                         
  ____                            _          _____ _ _              _____      
 |  _ \ _ __ ___  _   _  ___  ___| |_ ___   | ____| (_) __ _  ___  |_   _|   _ 
 | |_) | '__/ _ \| | | |/ _ \/ __| __/ _ \  |  _| | | |/ _` |/ _ \   | || | | |
 |  __/| | | (_) | |_| |  __/ (__| || (_) | | |___| | | (_| |  __/   | || |_| |
 |_|   |_|  \___/ \__, |\___|\___|\__\___/  |_____|_|_|\__, |\___|   |_| \__,_|
                  |___/                                |___/                   
  ____                  _            _                  _                   
 |  _ \ _ __ ___  _ __ (_) __ _     / \__   _____ _ __ | |_ _   _ _ __ __ _ 
 | |_) | '__/ _ \| '_ \| |/ _` |   / _ \ \ / / _ \ '_ \| __| | | | '__/ _` |
 |  __/| | | (_) | |_) | | (_| |  / ___ \ V /  __/ | | | |_| |_| | | | (_| |
 |_|   |_|  \___/| .__/|_|\__,_| /_/   \_\_/ \___|_| |_|\__|\__,_|_|  \__,_|
                 |_|                                                        
  _____     _                   _____                       _             _   _ _ _       
 | ____|___| |_ _____   _____  |_   _|__ _ __ _ __ __ _  __| | __ _ ___  (_) (_) | | __ _ 
 |  _| / __| __/ _ \ \ / / _ \   | |/ _ \ '__| '__/ _` |/ _` |/ _` / __| | | | | | |/ _` |
 | |___\__ \ ||  __/\ V /  __/   | |  __/ |  | | | (_| | (_| | (_| \__ \ | | | | | | (_| |
 |_____|___/\__\___| \_/ \___|   |_|\___|_|  |_|  \__,_|\__,_|\__,_|___/ |_| |_|_|_|\__,_|
          
****************************************************************************************************                                                                                         
"""