
def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[],dictionary={}):
    while True:
        print(textOpts)
        opc = input(inputOptText)
        opc = int(opc)
        if opc in rangeList or opc in exceptions or opc in dictionary.keys():
            return opc
        else:
            print("Invalid Options")

password = "Alolb8*"
def checkPassword(password):
    if len(password) not in range(8,12):
        print("Invalid range")
    elif not password:
        print("hola")

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
