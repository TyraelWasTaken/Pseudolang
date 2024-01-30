types = {
    "+": "AO",
    "-": "AO",
    "*": "AO",
    "/": "AO",
    "MOD": "AO",
    "DIV": "AO",
    
    "OUTPUT": "OUT"
}

'''
AO = Arithematic Operator
OUT = Output
'''

class lex():
    def __init__(self,data):
        content = list(data)
        
        tokens = []
        currentToken = {}
        stringstart = False
        tok = ""
        self.content = content
        self.tokens = tokens
        self.currentToken = currentToken
        self.stringstart = stringstart
        self.tok = tok
    
    def scan(self):
        for self.char in self.content:
            if (self.char == " " or self.char == ";") and self.stringstart == False: # we will need to put a ";" at the end of each line unless we use the \n when a new line starts :p
                
                if self.tok.isnumeric():
                    self.integer()
                    
                if self.tok in types:
                    self.arithmatic()

                if self.char == "\"":
                    self.string()
                else: 
                    self.tok += self.char
                    
                if self.tok == " " or self.tok == ";":
                    self.tok = ""

                return self.tokens # this is epic fr (totally not dying inside making this)
                           
    def integer (self):  
        currentToken = {
            "image": self.tok,
            "type": "integer"
        }
        self.tokens.append(currentToken)
        currentToken = {}
        
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
        return self.tokens

        
    
#Parsers
#    def Parser(self):
        
