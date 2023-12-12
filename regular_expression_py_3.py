stringIn = ["b"]
stringEnd = ["a"]
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
    if (firstChar in stringEnd or firstChar in stringIn or firstChar==" "):
        return firstChar
    else : 
        return parseInt(symbol)
    
def trueInput(symbol="") :
    if len(symbol) <= 0 :
        return False
    
    firstChar = parseFirstChar(symbol)
    if(firstChar==None) :
        return False
    return True

state = "q0"
symbol = input("masukan karakter : ")
trueAlfabet = trueInput(symbol)

firstChar = parseFirstChar(symbol)
while ( trueAlfabet ) :
    match state :
        case "q0" : 	
            if (firstChar in stringIn) :
                state = "q0"
            elif (firstChar in stringEnd) :
                state = "q1"
            else :
                state = "qError"
                break
        case _ :
            break
            
    symbol = input("masukan karakter : ")
    
    firstChar = parseFirstChar(symbol)
    
    if firstChar==" " :
        break
    
    trueAlfabet = trueInput(symbol)
    
if state=="q1" and firstChar==" " :
    print("STRING DITERIMA") 
else :
    print("STRING TIDAK DITERIMA") 