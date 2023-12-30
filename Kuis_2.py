sTOt = ["a"]
tTOv = ["b"]
vTOv = ["b"]
vTOs = ["c"]
stoppingChar = [""," ",None]
def parseInt(symbol):
    if len(symbol) <= 0 :
        return None
    firstChar = symbol[0]
    try:
        number = int(firstChar)
        return number
    except ValueError:
        return None
    
def parseFirstChar(symbol):
    if len(symbol) <= 0 :
        return None
    firstChar = symbol[0]
    if (firstChar in sTOt or firstChar in tTOv or firstChar in vTOv or firstChar in vTOs):
        return firstChar
    resultInt = parseInt(symbol)
    if resultInt!=None : 
        return resultInt
    else :
        return firstChar
    
def trueInput(symbol="") :
    replacedSymbol = symbol.replace(" ", "")
    if len(replacedSymbol) <= 0 :
        return False
    firstChar = parseFirstChar(symbol)
    if(firstChar==None) :
        return False
    return True

state = "s"
symbol = input("masukan karakter : ")
trueAlfabet = trueInput(symbol)
firstChar = parseFirstChar(symbol)
while ( trueAlfabet ) :
    match state :
        case "s" : 	
            if (firstChar in sTOt) :
                state = "t"
            else :
                state = "qError"
                break
        case "t" : 	
            if (firstChar in tTOv) :
                state = "v"
            else :
                state = "qError"
                break
        case "v" : 	
            if (firstChar in vTOv) :
                state = "v"
            elif (firstChar in vTOs) :
                state = "s"
            else :
                state = "qError"
                break
        case _ :
            break
    symbol = input("masukan karakter : ")
    
    firstChar = parseFirstChar(symbol)
    if firstChar in stoppingChar :
        break

    trueAlfabet = trueInput(symbol)
     
if state=="s" and firstChar in stoppingChar :
    print("STRING DITERIMA") 
else :
    print("STRING TIDAK DITERIMA") 