
class Menu:
    
    def __init__(self, title):
        self.title = title
        self.options = list()
                
    def Menu(self):
        self.title = None
        self.options = list()
        
    def getOption(self, index):
        return options.get(index)
    
    def addOption(self, option) -> bool:
        return options.add(option)
    
    def removeOption(self, option):
        return options.remove(option)
    
    def removeOption(self, index):
        return options.remove(index)
    
    def __str__(self) -> str:
        pass #TODO 
    
    def show(self): #TODO
        print("=============="+title+"================")
        it = options.get
        
    #TODO