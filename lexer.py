from tokens import Token, TokenType

EXCEPTIONS = " \n\t"
DIGITS = "0123456789"
class Lexer:
    
    def __init__(self, expression):
        self.expression = iter(expression)
        self.advanced()
    
    def advanced(self):
        try:
            self.current_char = next(self.expression)
        except StopIteration:
             self.current_char = None
             
    def make_tokens(self):
        while self.current_char != None:
            if self.current_char in EXCEPTIONS:
                self.advanced()
            elif self.current_char == "." or self.current_char in DIGITS:
                yield self.get_number()
            elif self.current_char == "+":
                self.advanced()
                yield Token(TokenType.PLUS)
            elif self.current_char == "-":
                self.advanced()
                yield Token(TokenType.MINUS)
            elif self.current_char == "*":
                self.advanced()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == "/":
                self.advanced()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == "(":
                self.advanced()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ")":
                self.advanced()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Это чё такое {self.current_char}?")
        
    def get_number(self):
        point_count = 0
        number = self.current_char
        self.advanced()
        while self.current_char != None and (self.current_char == "." or self.current_char in DIGITS):
            if self.current_char == ".":
                point_count += 1
                if point_count > 1:
                    break
                
            number += self.current_char
            self.advanced()
        
        if number.startswith("."):
            number = "0" + number
        if number.endswith("."):
            number += "0"
            
        return Token(TokenType.NUMBER, float(number))