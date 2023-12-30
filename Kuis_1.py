q0TOq0 = ["c"]
q0TOq1 = ["a"]
q1TOq2 = ["b"]
q2TOq1 = ["c"]
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
    print("char")
    if (firstChar in q0TOq0 or firstChar in q0TOq1 or firstChar in q1TOq2 or firstChar in q2TOq1):
        return firstChar
    else : 
        return parseInt(symbol)
    
def trueInput(symbol="") :
    replacedSymbol = symbol.replace(" ", "")
    if len(replacedSymbol) <= 0 :
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
            if (firstChar in q0TOq0) :
                state = "q0"
            elif (firstChar in q0TOq1) :
                state = "q1"
            else :
                state = "qError"
                break
        case "q1" : 	
            if (firstChar in q1TOq2) :
                state = "q2"
            else :
                state = "qError"
                break
        case "q2" : 	
            if (firstChar in q2TOq1) :
                state = "q1"
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
     
if state=="q1" and firstChar in stoppingChar :
    print("STRING DITERIMA") 
else :
    print("STRING TIDAK DITERIMA") 