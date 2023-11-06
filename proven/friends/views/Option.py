
class Option:
    def __init__(self, text, actionCommand):
        self.text = text
        self.actionCommand = actionCommand
        
    def __hash__(self):
        prime = 31
        result = 1
        result = prime * result + (0 if self.actionCommand is None else hash(self.actionCommand))
        result = prime * result + (0 if self.text is None else hash(self.text))
        return result
    
    def __eq__(self, __value: object) -> bool:
        pass #TODO
    
    def __str__(self) -> str:
        pass #TODO
    
    #TODO