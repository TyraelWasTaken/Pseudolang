import langcode.pseudocode_lexer

def openfile(filename):
    data = open(filename, "r").read()
    return data

def lex(data):
    content = list(data)
    
    
    tokens = {}
    currentToken = {}
    state = 0   #will be 1 if a string has started
    tok = ""
    
    for char in content:
        if char == " " and state == 0:
            print(list(tok))
            tok = ""
        else:
            tok += char
            
        
    return tokens

if __name__ == "__main__":
    data = openfile("test.aqa")
    
    tokens = lex(data)
    print(tokens)