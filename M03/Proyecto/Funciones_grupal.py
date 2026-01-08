
def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[],dictionary={}):
    while True:
        print(textOpts)
        opc = input(inputOptText)
        opc = int(opc)
        if opc in rangeList or opc in exceptions or opc in dictionary.keys():
            return opc
        else:
            print("Invalid Options")

password = "10101**A*"
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
checkPassword(password)
nombre = ("Holaaaa")
def checkUser(user):
    if len(user) not in range(6,10):
        print("Invalid range")
        return False
    elif not user.isalpha():
        print("Only numers and characters")
        return False
    return True

checkUser(nombre)
