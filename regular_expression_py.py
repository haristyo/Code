kar = ["a","b","c"]
num = [0,1,2,3,4]

def benarAlfabet(symbol) :
    trueAlfabet = False
    text = ""
    if len(symbol) > 0 :
        text = symbol[0]
    if (text in kar):
        trueAlfabet = True
    else :
        try:
            number = int(text)
            if (number in num):
                trueAlfabet = True
        except ValueError:
            pass
    return trueAlfabet

state = "q0"
firstChar = ""
symbol = input("masukan karakter atau num : ")

trueAlfabet = benarAlfabet(symbol)

if len(symbol) > 0 :
    firstChar = symbol[0]
while ( trueAlfabet ) :
    match state :
        case "q0" : 	
            if (firstChar in kar) :
                state = "q1"
            else :
                state = "q2"
                break
        case "q1" :
            state = "q1"
        case "q2" :
            state = "q2"
    firstChar = ""
    symbol = input("masukan karakter atau num : ")
    if len(symbol) > 0 :
        firstChar = symbol[0]
    if firstChar==" " :
        state = "q2"
    trueAlfabet = benarAlfabet(symbol)
if state=="q2" and firstChar==" " :
    print("STRING DITERIMA") 
else :
    print("STRING TIDAK DITERIMA") 