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
        
        "RANDINT": "RAND",
        
        "LEN": "MANIPULATOR",
        "SUBSTRING": "MANIPULATOR",
        "POSITION": "MANIPULATOR",
        
        "DO": "CONLOOP",                #DO is not necessary
        "THEN": "CONDITION",
        "CONSTANT": "DECLARATION",
        "RETURN": "FUNCTION",
        "WHILE": "CONLOOP",
        "ENDWHILE": "CONLOOP",
        "FOR": "RANGE",
        "ENDFOR": "RANGE",
        "REPEAT": "CONLOOP",
        "UNTIL": "CONLOOP",
        "IF": "CONDITION",
        "ENDIF": "CONDITION",
        "ELSE": "CONDITION",
        "ELIF": "CONDITION",
        "SUBROUTINE": "THREAD",
        "ENDSUBROUTINE": "THREAD",
        "RECORD": "RECORD",
        "ENDRECORD": "RECORD",
        "TO": "RANGE",
        "STEP": "RANGE"

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
        self.spacecount = 0
        for char in content:
            self.tok += char
            
            if char == " " and self.stringstart == False:
                if self.tok == " ":
                    self.tok = ""
                    self.spacecount = self.spacecount + 1
                    if self.spacecount == 4:
                        self.add_token(image="  ", token_type="TAB")
                        self.spacecount = 0
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
            
            
            if char == '\n':
                self.add_token(image='EOL', token_type='EOL')
            

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

        self.add_token(image='EOF', token_type='EOF')
        return self.tokens

        
#Parsers
class ASTNode:
    pass

class Node(ASTNode):
    def __init__(self, value):
        self.value = value

class Parser:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.count = 0
        self.all_tokens = []
        for items in self.tokens:
            for sublists in items:
                self.all_tokens.append(sublists)
        self.next_token()
        print(self.current_token.values())
        for items in self.current_token.values():
            print(items)

    def next_token(self):
        if self.count+1 < len(self.all_tokens):
            self.current_token = self.all_tokens[self.count]
            self.count += 1
        return self.current_token
        
        

    def parse(self):
        trees = []
        while self.current_token != "EOF":
            nodes = []
            while self.current_token['type'] != None or self.current_token['type'] != "EOL":
                if self.current_token['type'] == 'INTEGER':
                    return
                elif self.current_token['type'] == 'FLOAT':
                    return
                elif self.current_token['type'] == 'ARRW':
                    return
                self.next_token()
            if self.current_token['type'] == 'EOL':
                trees.append(nodes)
        return trees
