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

    with open("x.json", "w") as a:
        json.dump(tokens, a, indent=4) #easyer to read