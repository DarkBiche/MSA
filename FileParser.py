def open_text_file(addr_text):
    file = open(addr_text,"r")
    texte = file.readlines()
    file.close()
    return texte

def parsing_file(addr_text):
    file = open_text_file(addr_text)
    s = []
    buffer = []
    for line in file:
        if line == ".\tSENT\t.\n":
            s.append(buffer)
            #print(buffer)
            buffer = []
        else:
            word = ""
            i=0
            while line[i] != "\t":
                word = word + line[i]
                i = i + 1
            buffer.append(word)
        
    return s
    
 
