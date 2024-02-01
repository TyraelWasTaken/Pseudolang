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
        self.count = 2
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

#  def expect(self): 