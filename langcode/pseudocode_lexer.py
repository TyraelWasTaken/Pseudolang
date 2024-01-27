#LEXER
class Lexer():
    types = {
        "+": "AO",
        "-": "AO",
        "*": "AO",
        "/": "AO",
        "MOD": "AO",
        "DIV": "AO",

        "==": "COMPARE",
        
        "<--": "ARRW",
        ">": "SIGN",
        "<": "SIGN",
        
        "OUTPUT": "OUT",
        "USERINPUT": "IN",
        
        "(": "CBO",
        ")": "CBC",
        "]": "SBO",
        "[": "SBC",
        
        "CODE_TO_CHAR": "CONVERTOR",
        "REAL_TO_STRING": "CONVERTOR",
        "INT_TO_STRING": "CONVERTOR",
        "STRING_TO_TREAL": "CONVERTOR",
        "STRING_TO_INT": "CONVERTOR",
        
        "RANDINT": "RANDOM",
        
        "LEN": "MANIPULATOR",
        "SUBSTRING": "MANIPULATOR",
        "POSITION": "MANIPULATOR",
        
        "DO": "ToDo",
        "THEN": "ToDo",
        "CONSTANT": "ToDo",
        "RETURN": "ToDo",
        "WHILE": "ToDo",
        "ENDWHILE": "ToDo",
        "FOR": "ToDo",
        "ENDFOR": "ToDo",
        "REPEAT": "ToDo",
        "UNTIL": "ToDo",
        "IF": "ToDo",
        "ENDIF": "ToDo",
        "ELSE": "ToDo",
        "ELIF": "ToDo",
        "SUBROUTINE": "ToDo",
        "ENDSUBROUTINE": "ToDo",
        "RECORD": "ToDo",
        "ENDRECORD": "ToDo",
        "TO": "ToDo",
        "STEP": "ToDo"

    }

    def __init__(self):
        self.tokens = []
        self.currentToken = {}
        self.stringstart = False
        self.tok = ""
        self.line = []

    def isfloaty(self, value):
        try:
            float_value = float(value)
            return True
        except ValueError:
            return False
        
    def add_token(self, image, token_type):
        self.currentToken = {
            "image": image,
            "type": token_type
        }
        self.line.append(self.currentToken)
        self.currentToken = {}
        self.tok = ""
        
    def stringything(self):
        if self.stringstart == False:
            self.stringstart = True
            self.tok = ""
        elif self.stringstart == True:
            self.add_token(image=self.tok[:-1], token_type="STRING")
            self.stringstart = False
        
    def lex(self, data):
        content = list(data)
        arrow = ""
        for char in content:
            self.tok += char
            
            if char == " " and self.stringstart == False:
                if self.tok == " ":
                    self.tok = ""
                elif self.tok[:-1].isnumeric():
                    self.add_token(image=self.tok[:-1], token_type="INTEGER")
                elif self.isfloaty(self.tok[:-1]) == True:
                    self.add_token(image=self.tok[:-1], token_type="FLOAT")
                else:
                    self.add_token(image=self.tok[:-1], token_type="VAR")
                    

            
            if self.tok in self.types:
                self.add_token(image=self.tok, token_type=self.types[self.tok])
                        
            if char == "\"":
                self.stringything()
            
            if char == '\n' and self.line != []:   
                if self.tok[0:-1].isnumeric():
                    self.add_token(image=self.tok[0:-1], token_type="INTEGER")
                elif self.isfloaty(self.tok[0:-1]) == True:
                    self.add_token(image=self.tok[0:-1], token_type="FLOAT")
                    
                self.tokens.append(self.line)
                self.line = []
                self.tok = ""
            if self.tok == '\n':
                self.tok = ""
                
                
        if self.line != []: #checks if a line has been entered with nun on
            if self.tok[0:].isnumeric():
                self.add_token(image=self.tok[0:], token_type="INTEGER")
            elif self.isfloaty(self.tok[0:]) == True:
                self.add_token(image=self.tok[0:], token_type="FLOAT")
            self.tokens.append(self.line)
        return self.tokens