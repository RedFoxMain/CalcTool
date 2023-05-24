from nodes import * 
from dataclasses import dataclass

@dataclass
class Number:
    value: any
    def __repr__(self):
        return f"{self.value}"
        
class Interpreter: 
         def __init__(self): 
                 pass 
  
         def visit(self, node): 
                 method_name = f'visit_{type(node).__name__}' 
                 method = getattr(self, method_name) 
                 return method(node) 
                  
         def visit_Number(self, node): 
                 return Number(node.value) 
  
         def visit_AddNode(self, node): 
                 return Number(self.visit(node.first_num).value + self.visit(node.second_num).value) 
  
         def visit_SubNode(self, node): 
                 return Number(self.visit(node.first_num).value - self.visit(node.second_num).value) 
  
         def visit_MulNode(self, node): 
                 return Number(self.visit(node.first_num).value * self.visit(node.second_num).value) 
  
         def visit_DivNode(self, node): 
                 try: 
                         return Number(self.visit(node.first_num).value / self.visit(node.second_num).value) 
                 except: 
                         raise Exception("Runtime math error")
         def visit_UAddNode(self, node):
             return self.visit(node.node)
         def visit_USubNode(self, node):
             return Number(-self.visit(node.node).value)