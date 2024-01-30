import langcode.pseudocode_lexer
<<<<<<< Updated upstream
=======
import json
>>>>>>> Stashed changes

def openfile(filename):
    data = open(filename, "r").read()
    return data

if __name__ == "__main__":
<<<<<<< Updated upstream
    data = openfile("C:/Users/samue/OneDrive/Documents/code/Psuedolang/Pseudolang/Pseudolang/Testing/test.aqa")
    
    tokens = langcode.pseudocode_lexer.lex(data)
    print(tokens) 
    
    # there has gotta be a better way to do the lexer stuff lmao
=======
    lexer = langcode.pseudocode_lexer.Lexer()
    data = openfile("test.aqa")
    tokens = lexer.lex(data)
    print(tokens)

    with open("x.json", "w") as a:
        json.dump(tokens, a, indent=4) #easyer to read
>>>>>>> Stashed changes
