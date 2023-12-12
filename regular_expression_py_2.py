num = [0,1,2,3,4,5,6,7,8,9]
ekspressions = ["/","*","+","-"]
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
    if (firstChar in ekspressions or firstChar in num or firstChar==" "):
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

# def trueInput(symbol=None) :
    # valueInt = parseFirstChar(symbol)
    # if valueInt==None : 
    #     return False
    # return True
    # trueAlfabet = False
    # text = ""
    # if len(symbol) > 0 :
    #     text = symbol[0]
    # if (text in num):
    #     trueAlfabet = True
    # else :
    #     try:
    #         number = int(text)
    #         print(number in num)
    #         if (number in num):
    #             trueAlfabet = True
    #     except ValueError:
    #         pass
    # return trueAlfabet

state = "q0"
symbol = input("masukan karakter atau num : ")
trueAlfabet = trueInput(symbol)

firstChar = parseFirstChar(symbol)
while ( trueAlfabet ) :
    print(firstChar)
    print(state)
    if(firstChar in num) :
        print("is num",firstChar in num)
    else:
        print("is symbol",firstChar in ekspressions)
    match state :
        case "q0" : 	
            if (firstChar in num) :
                state = "q1"
            else :
                state = "qError"
                break
        case "q1" :
            if (firstChar in num) :
                state = "q1"
            elif (firstChar in ekspressions) :
                state = "q2"
            else :
                state = "qError"
                break
        case "q2" :
            if (firstChar in num) :
                state = "q3"
            else :
                state = "qError"
                break
        case "q3" :
            if (firstChar in num) :
                state = "q3"
            else :
                state = "qError"
                break
    symbol = input("masukan karakter atau num : ")
    
    firstChar = parseFirstChar(symbol)
    
    if firstChar==" " :
        state = "q4"
        break
    trueAlfabet = trueInput(symbol)
    
if state=="q4" and firstChar==" " :
    print("STRING DITERIMA") 
else :
    print("STRING TIDAK DITERIMA") 