import langcode.pseudocode_lexer
import json 
def openfile(filename):
    data = open(filename, "r").read()
    return data

if __name__ == "__main__":
    lexer = langcode.pseudocode_lexer.Lexer()
    data = openfile("test.aqa")
    tokens = lexer.lex(data)
    print(tokens)
    #print(list(data))
    # there has gotta be a better way to do the lexer stuff lmao
    with open("x.json", "w") as a:
        json.dump(tokens, a, indent=4)