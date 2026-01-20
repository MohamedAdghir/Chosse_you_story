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
    texto = title.center(suma,"=") + "\n"
    for i in range(len(t_name_columns)):
        texto += t_name_columns[i].ljust(t_size_columns[i])
    
    texto += "\n" + "".center(suma,"*") + "\n"
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

#writeText(formatText(texto, 105, "\n"),0.025)

"""
diccionari = {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
'date': datetime.datetime(2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName':
'Beowulf'}, 5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
'date': datetime.datetime(2021, 11, 26, 13, 28, 36), 'idCharacter': 1,
'CharacterName': 'Beowulf'}}
tuple_of_keys = ("Username","Name","CharacterName","date")
weigth_of_columns = (20, 20,30, 20)
"""
def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    lista = list(dict_of_data)
    for i in range(len(lista)):
        texto = str(lista[i]).ljust(weigth_of_columns[0])
        for j in range(len(tuple_of_keys)-1):
            texto = texto +str(dict_of_data[lista[i]][tuple_of_keys[j]]).ljust(weigth_of_columns[j+1])
        texto = texto + str(dict_of_data[lista[i]][tuple_of_keys[len(tuple_of_keys)-1]])
        print(texto)

#getTableFromDict(tuple_of_keys,weigth_of_columns,diccionari)

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


#print(getFormatedAdventures())

def replay(idAdventure,choices):
    adventure_steps = get_id_bystep_adventure(idAdventure)

    for step_id, answer_id in choices:
        limpiar_terminal()

        #mostrar la description del paso
        step_text = adventure_steps[step_id]["Description"]
        print(formatText(step_text, 105, "\n"))
        input("Enter to continue")

        # mostrar la opcion seleccionada y resolution
        answers = get_answers_bystep_adventure(step_id)
        print("\nOption selected")
        resolution = answers[(answer_id, step_id)]["resolution"]
        print(formatText(resolution, 105, "\n"))
        input("Enter to continue")

    limpiar_terminal()
    print(show_fin())
    input("Enter to continue")


def show_relive_adventure():
    limpiar_terminal()
    print("""_/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\_
\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /
/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\_

     ____  _____ _  ________ __ ________ ________
    |  _ \\| ____| |     | |   \\ \\    / / ____|
    | |_) |  _| | |      | |    \\ \\  / /| |___
    |  _ <| |___| |___ __| |____ \\ \\/ / | |____
    |_| \\_\\_____|_____|__|____  \\___/  |______|

                YOUR ADVENTURE

_/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\_
\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /\\  /
/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\__/_/\\_
""")
    input("Enter to continue")

#replayAdventures = getReplayAdventures()
#getTableFromDict(("Username", "Name", "CharacterName", "date"),(6, 15, 35, 20, 25),replayAdventures)

def show_fin():
    print("""
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



