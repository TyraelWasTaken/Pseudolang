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

    def arithmatic(self):
        if types[self.tok] == "AO":
            
            currentToken = {
                "image": self.tok,
                "type": "AO"
            }
            
        elif types[self.tok] == "OUT":
            currentToken = {
                "type": "OUT"
            }
            
        self.tokens.append(currentToken) 
        currentToken = {}
        self.tok = ""

    def string(self):
        if stringstart == False:
            stringstart = True
        elif stringstart == True:
            currentToken = {
                    "image": self.tok,
                    "type": "STRING"
                }
            self.tokens.append(currentToken) 
            currentToken = {}
            stringstart = False
        self.tok = ""
                           
        