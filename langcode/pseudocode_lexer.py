types = {
    "+": "AO",
    "-": "AO",
    "*": "AO",
    "/": "AO",
    "MOD": "AO",
    "DIV": "AO",
    
    "OUTPUT": "OUT"
}

'''
AO = Arithematic Operator
OUT = Output
'''
def is_float(value):
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False


def lex(data):
    
    content = list(data)
    
    tokens = []
    currentToken = {}
    stringstart = False
    tok = ""
    
    for char in content:
        if (char == " " or char == ";") and stringstart == False: # we will need to put a ";" at the end of each line unless we use the \n when a new line starts :p
            if tok.isnumeric():
                    
                currentToken = {
                    "image": tok,
                    "type": "integer"
                }
                tokens.append(currentToken)
                currentToken = {}
                
                tok = ""
                
            if is_float(tok) == True:
                    
                currentToken = {
                    "image": tok,
                    "type": "float"
                }
                tokens.append(currentToken)
                currentToken = {}
                
                tok = ""
                
            if tok in types:
                    
                if types[tok] == "AO":
                    
                    currentToken = {
                        "image": tok,
                        "type": "AO"
                    }
                    
                elif types[tok] == "OUT":
                    currentToken = {
                        "type": "OUT"
                    }
                    
                tokens.append(currentToken) 
                currentToken = {}
                tok = ""
                
            if tok == " " or tok == ";":
                tok = ""
                
        elif char == "\"":
            if stringstart == False:
                stringstart = True
                
            elif stringstart == True:
                currentToken = {
                        "image": tok,
                        "type": "STRING"
                    }
                tokens.append(currentToken) 
                currentToken = {}
                stringstart = False
            tok = ""
            
        else: 
            tok += char
        
            
    return tokens # this is epic fr (totally not dying inside making this)