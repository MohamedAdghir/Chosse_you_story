
def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[],dictionary={}):
    while True:
        print(textOpts)
        opc = input(inputOptText)
        opc = int(opc)
        if opc in rangeList or opc in exceptions or opc in dictionary.keys():
            return opc
        else:
            print("Invalid Options")

