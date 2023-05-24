from lexer import Lexer
from parser import Parser
from interpret import Interpreter 
  
while True: 
         try: 
                 text = input(">>> ") 
                 lexer = Lexer(text) 
                 tokens = lexer.make_tokens() 
                 parser = Parser(tokens) 
                 tree = parser.parse() 
                 if not tree: continue 
                 interpreter = Interpreter() 
                 value = interpreter.visit(tree) 
                 print(value) 
         except Exception as e: 
                 print(e)