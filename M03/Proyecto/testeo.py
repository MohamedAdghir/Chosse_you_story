
# Funcion para formatear texto
def formatText(text,lenLine,split):
    formatedText = ""
    start = 0
    end = 0
    while not end > len(text):
        if text[end] == " ":
            start = end + 1
            end += lenLine + 1
        else:
            start = end
            end += lenLine
        if end > len(text):
            slicedText = text[start:]
            formatedText += slicedText
        else:
            if text[end] != " ":
                space = text[start:end].rfind(" ")
                if space != -1:
                    end = start + space
            print(start,end)
            slicedText = text[start:end]
            formatedText += slicedText + split
            print(formatedText)
    return formatedText


print(formatText("12345 abcdf 09876 ppppp", 5, "\n"))