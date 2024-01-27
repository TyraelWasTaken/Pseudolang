class Lexer():
    types = {
        "+": "PLUS",
        "-": "SUBTRACT",
        "*": "MUL",
        "/": "FRAC",
        "MOD": "MOD",
        "DIV": "DIV",

        "==": "COMPARE",
        
        "<--": "ARRW",
        ">": "GTHAN",
        "<": "LTHAN",
        
        "OUTPUT": "OUT",
        "USERINPUT": "IN",
        
        "(": "CBO",
        ")": "CBC",
        "]": "SBO",
        "[": "SBC",
        
        "CODE_TO_CHAR": "CODE_TO_CHAR",
        "REAL_TO_STRING": "REAL_TO_STRING",
        "INT_TO_STRING": "INT_TO_STRING",
        "STRING_TO_TREAL": "STRING_TO_TREAL",
        "STRING_TO_INT": "STRING_TO_INT",
        
        "RANDINT": "RAND",
        
        "LEN": "LEN",
        "SUBSTRING": "SUBS",
        "POSITION": "POS",
        
        "DO": "DO",
        "THEN": "THEN",
        "CONSTANT": "CONST",
        "RETURN": "RETURN",
        "WHILE": "WHI",
        "ENDWHILE": "ENDWHI",
        "FOR": "FOR",
        "ENDFOR": "ENDFOR",
        "REPEAT": "REP",
        "UNTIL": "UNTIL",
        "IF": "IF",
        "ENDIF": "ENDIF",
        "ELSE": "ELSE",
        "ELIF": "ELIF",
        "SUBROUTINE": "SUBR",
        "ENDSUBROUTINE": "ENDSUBR",
        "RECORD": "REC",
        "ENDRECORD": "ENDREC",
        "TO": "TO",
        "STEP": "STEP"

    }
    def __init__(self):
        self.tokens = []
        self.currentToken = []
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
        self.currentToken = [str(token_type) + ":" + str(image)]
        self.line.append(self.currentToken)
        self.currentToken = []
        self.tok = ""
        
    def stringything(self):
        if self.stringstart == False:
            self.stringstart = True
            self.tok = ""
        elif self.stringstart == True:
            self.add_token(image=self.tok[:-1], token_type="STRING")
            self.stringstart = False
    def final(self):
        x = self.tokens
        self.tokens = []
        for i in x:
            for j in i:
                self.tokens.append(j[0])
            self.tokens.append("EOL:EOL")
                
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
            
            '''
            if char == '\n':
                self.add_token(image='EOL', token_type='EOL')
            '''

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
            #print(self.line)
            
            if char == "<" or char == "-" and arrow != "":
                arrow += char
                if arrow == "<--":
                    del self.line[-3:]
                    self.add_token(image="<--", token_type="ARRW")
                    arrow = ""
                
        if self.line != []: #checks if a line has been entered with nun on
            if self.tok[0:].isnumeric():
                self.add_token(image=self.tok[0:], token_type="INTEGER")
            elif self.isfloaty(self.tok[0:]) == True:
                self.add_token(image=self.tok[0:], token_type="FLOAT")
            self.tokens.append(self.line)

        self.add_token(image='EOL', token_type='EOL')
        self.final()
        return self.tokens