class Menu:
    
    def __init__(self, title):
        self.title = title
        self.options = list()
                
    def Menu(self):
        self.title = None
        self.options = list()
        
    def getOption(self, index):
        return self.options.get(index)
    
    def addOption(self, option) -> bool:
        return self.options.add(option)
    
    def removeOption(self, option):
        return self.options.remove(option)
    
    def removeOption(self, index):
        return self.options.remove(index)
    
    def __str__(self) -> str:
        return ("Title = " + str(self.title) + ", Options = " + str(self.options))
    
    def show(self):
        print("=============="+self.title+"================")
        idOption = 0
        for Option in self.options:
            print(Option ": " + idOption)
            idOption = idOption + 1

        
    def getSelecOption() -> int:
        """Gets the selected option. If fails, resturns -1

        Returns:
            int: Option choosen. If not, -1
        """
        opt = -1
        try:
            print("Select an Option: ")
            opt = input()
            if opt < 0 or opt >= Menu.options.len():
                opt = -1
        except :
            opt = -1
    
    def getSelectedOptionActionCommand():
        optionNumber = Menu.getSelectedOption()
        actionCommand = None
        if optionNumber >= 0 and optionNumber < Menu.options.len():
            actionCommand = Menu.options.get(optionNumber).getActionCommand()
        return actionCommand