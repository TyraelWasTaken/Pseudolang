types = {
    "+": "AO",
    "-": "AO",
    "*": "AO",
    "/": "AO",
    "MOD": "AO",
    "DIV": "AO",
}

'''
AO = Arithematic Operator
'''

def lex(data):
    
    content = list(data)
    
    tokens = []
    currentToken = {}
    state = 0   # will be a different sometimes smh
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
            
            if tok in types:
                
                if types[tok] == "AO":
                    
                    currentToken = {
                        "image": tok,
                        "type": "AO"
                    }
                    
                    tokens.append(currentToken) 
                    currentToken = {}
                tok = ""
            if tok == " " or tok == ";":
                tok = ""
        else: 
            tok += char
            
        
            
        
    return tokens # this is epic fr (totally not dying inside making this)