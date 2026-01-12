import  datetime

#Funcion de las opciones del menu
def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[],dictionary={}):
    while True:
        print(textOpts)
        opc = input(inputOptText)
        opc = int(opc)
        if opc in rangeList or opc in exceptions or opc in dictionary.keys():
            return opc
        else:
            print("Invalid Options")

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
    if len(user) not in range(6,10):
        print("Invalid range")
        return False
    elif not user.isalpha():
        print("Only numers and characters")
        return False
    return True

#Funcion para los encabezados
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    suma = 0
    texto = ""
    for a in t_size_columns:
        suma = suma + a
    print(title.center(suma,"="))
    for i in range(len(t_name_columns)):
        texto = texto + t_name_columns[i].ljust(t_size_columns[i])
    print(texto+ "\n" + "".center(suma,"*"))

# Funcion que crea un header
def getHeader(text):
    texto = "".center(120,"*") + "\n" + text.center(120,"=") + "\n" + "".center(120,"*")
    print(texto)

texto = "Escoge el camino mas seguro para poder escapar del hombre lobo y luego poder ir a la  casa de abuela a cuidarla"
def getFormatedAnswers(id_respuesta, texto, longitud_linea, margen_derecho):
    prefijo = "{} ) ".format(id_respuesta)
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


#print(getFormatedAnswers("1",texto,0,120))

diccionari = {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
'date': datetime.datetime(2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName':
'Beowulf'}, 5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
'date': datetime.datetime(2021, 11, 26, 13, 28, 36), 'idCharacter': 1,
'CharacterName': 'Beowulf'}}
tuple_of_keys = ("Username","Name","CharacterName","date")
weigth_of_columns = (20, 20,30, 20)
def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    lista = list(dict_of_data)
    for i in range(len(lista)):
        texto = str(lista[i]).ljust(weigth_of_columns[0])
        for j in range(len(tuple_of_keys)-1):
            texto = texto +str(dict_of_data[lista[i]][tuple_of_keys[j]]).ljust(weigth_of_columns[j+1])
        texto = texto + str(dict_of_data[lista[i]][tuple_of_keys[len(tuple_of_keys)-1]])
        print(texto)

#getTableFromDict(tuple_of_keys,weigth_of_columns,diccionari)
text1 = "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo\
seguir con la aventura que estabas viviendo simplemente aleshores el resultat de fer la següent crida:"
