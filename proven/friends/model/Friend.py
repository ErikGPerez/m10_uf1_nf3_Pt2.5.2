class Friend:
    
    def __init__(self, *args):
        if len(args) == 0: #Empty object
            self.phone 
            self.name
            self.age
        elif len(args) == 1: #Only name
            self.phone
            self.name == args[0]
            self.age
        else: #Default constructor
            self.phone == args[0]
            self.name == args[1]
            self.age == args[2]
            
        #Getters/Setters
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name
    def setPhone(self, phone):
        self.phone = phone
    def setAge(self, age):
        self.age = age
           
    def __hash__(self):
        hashCode = 0
        for char in self:
            hashCode = hashCode * 31 + ord(char)
            return hashCode
        
    def __eq__(self, __value: object) -> bool:
        pass
	
    def __str__(self) -> str:
        pass
    
    #TODO: Revisar que esté correctamente
    
    