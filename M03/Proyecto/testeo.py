
import time

text1 = "Narrador: Este no era el camino correcto hacia la sala de reuniones, y $NAME lo sabía perfectamente. Quizás quería hacer una parada en la sala de descanso de empleados primero, solo para admirarla."
text2 = "Ah, sí. Sin duda, una habitación digna de admiración. Al fin y al cabo, había merecido la pena el desvío, solo por pasar unos momentos aquí, en esta sala inmaculada y bellamente construida. $NAME se quedó allí de pie, absorbiéndolo todo."
text3 = "Narrador: Pero, ansioso por volver al trabajo, $NAME tomó la primera puerta abierta a su izquierda."

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

texto = formatText(text2,50,"\n")
escribir_con_efectos(texto, 0.05)
