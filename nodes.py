from dataclasses import dataclass

@dataclass
class Number:
    value: any
    
    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    first_num: any
    second_num: any
    
    def __repr__(self):
        return f"({self.first_num}+{self.second_num})"

@dataclass
class MulNode:
    first_num: any
    second_num: any
    
    def __repr__(self):
        return f"({self.first_num}*{self.second_num})"

@dataclass
class SubNode:
    first_num: any
    second_num: any
    
    def __repr__(self):
        return f"({self.first_num}-{self.second_num})"
        
@dataclass
class DivNode:
    first_num: any
    second_num: any
    
    def __repr__(self):
        return f"({self.first_num}/{self.second_num})"

@dataclass
class UAddNode:
    node: any
    
    def __repr__(self):
        return f"(+{self.node})"

@dataclass
class USubNode:
    node: any
    
    def __repr__(self):
        return f"(-{self.node})"    