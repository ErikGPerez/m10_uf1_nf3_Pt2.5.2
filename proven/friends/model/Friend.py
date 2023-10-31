class Friend:
    
    def __init__(self, *args):
        if len(args) == 0: #Empty object
            self.phone = None
            self.name = None
            self.age = None
        elif len(args) == 1: #Only phone
            self.phone = args[0]
            self.name = None
            self.age = None
        else: #Default constructor
            self.phone = args[0]
            self.name = args[1]
            self.age = args[2]
           
    def __hash__(self):
        hashCode = 0
        for char in self:
            hashCode = hashCode * 31 + ord(char)
            return hashCode
        
    def __eq__(self, __value) -> bool:
        if(isinstance(__value, Friend)):
            if(self.phone == __value.phone):
                return True
            else:
                return False
        else:
            return False
                    
	
    def __str__(self) -> str:
        return ("Phone = " + str(self.phone) + ", Name = " + str(self.name) + ", Age = " + str(self.age))
    
    #Constructor ended
    
#Test sector
