class Lexer():
    types = {
        "+": "AO",
        "-": "AO",
        "*": "AO",
        "/": "AO",
        "MOD": "AO",
        "DIV": "AO",
        
        "OUTPUT": "OUT",
        "USERINPUT": "IN",
        
        "(": "CB",
        ")": "CB",
        "]": "SB",
        "[": "SB",
        
        "CODE_TO_CHAR": "CONVERTOR",
        "CODE_TO_CHAR": "CONVERTOR",
        "REAL_TO_STRING": "CONVERTOR",
        "INT_TO_STRING": "CONVERTOR",
        "STRING_TO_TREAL": "CONVERTOR",
        "STRING_TO_INT": "CONVERTOR",
        
        "RANDINT": "RAND",
        
        "LEN": "MANIPULATOR",
        "SUBSTRING": "MANIPULATOR",
        "POSITION": "MANIPULATOR",
    }

    def __init__(self):
        self.tokens = []
        self.currentToken = {}
        self.stringstart = False
        self.tok = ""

    @staticmethod
    def is_float(value):
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
        self.tokens.append(self.currentToken)
        self.currentToken = {}

    def lex(self, data):
        content = list(data)

        for char in content:
            if (char == " " or char == ";") and not self.stringstart:
                if self.tok.isnumeric():
                    self.add_token(self.tok, "integer")
                    self.tok = ""

                elif self.is_float(self.tok):
                    self.add_token(self.tok, "float")
                    self.tok = ""

                elif self.tok in self.types:
                    if self.types[self.tok] == "AO" or self.types[self.tok] == "CB" or self.types[self.tok] == "SB":
                        self.add_token(self.tok, self.types[self.tok])
                        self.currentToken = {}
                    elif self.types[self.tok] == "OUT" or self.types[self.tok] == "IN":
                        self.currentToken = {"type": self.types[self.tok]}
                        self.tokens.append(self.currentToken)
                        self.currentToken = {}
                    self.tok = ""

                if char == " " or char == ";":
                    self.tok = ""

            elif char == "\"":
                if not self.stringstart:
                    self.stringstart = True
                elif self.stringstart:
                    self.add_token(self.tok, "STRING")
                    self.tok = ""
                    self.stringstart = False

            else:
                self.tok += char

        return self.tokens
