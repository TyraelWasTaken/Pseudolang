import langcode.pseudocode_lexer

def openfile(filename):
    data = open(filename, "r").read()
    return data

if __name__ == "__main__":
    data = openfile("C:/Users/samue/OneDrive/Documents/code/Psuedolang/Pseudolang/Pseudolang/Testing/test.aqa")
    
    tokens = langcode.pseudocode_lexer.lex(data)
    print(tokens) 
    
    # there has gotta be a better way to do the lexer stuff lmao