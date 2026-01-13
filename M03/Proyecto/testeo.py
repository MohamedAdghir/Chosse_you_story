
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

def getFormatedBodyColumns(texts,lenLines,margin=2):
    formatedColumns = []
    for i in range(len(texts)):
        formatedColumns.append([])
        formatedText = formatText(texts[i],lenLines[i],"\n")
        start = 0
        end = 0
        for j in range(formatedText.count("\n")):
            end = formatedText.find("\n", start)
            formatedColumns[i].append(formatedText[start:end])
            start = end + 1
    return formatedColumns

columnas = getFormatedBodyColumns((text1,text1,text1),(20,30,50),margin=2)
for columna in columnas:
    print(columna)
print(formatText(text1,20,"\n"))