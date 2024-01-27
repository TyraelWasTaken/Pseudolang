types = {
    "+": "AO",
    "-": "AO",
    "*": "AO",
    "/": "AO",
    "MOD": "AO",
    "DIV": "AO"
}

'''
AO = Arithmatic Operator
'''


def lex(data):
    content = list(data)
    
    tokens = []
    currentToken = {}
    state = 0   # will be 1 if a string has started or something smh
    tok = ""
    
    for char in content:
        
        if char == " " or char == ";" and state == 0: # we will need to put a ";" at the end of each line unless we use the \n when a new line starts :p
            
            if tok.isnumeric():
                
                currentToken = {
                    "image": tok,
                    "type": "integer"
                }
                tokens.append(currentToken)
                currentToken = {}
            
            tok = ""
            
        elif char in types and types[char]  == "AO" and state == 0:
            currentToken = {
                "image": char,
                "type": "AO"
            }
            tokens.append(currentToken)
            tok = ""
        else:
            tok += char
            
        
    return tokens