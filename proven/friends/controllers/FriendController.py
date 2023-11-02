from model.FriendModel import FriendModel
#from ..views.FriendView import FriendView

class FriendController:
    
    def __init__(self, model):
        self.model = model
        #self.view = FriendView(model)
        #view.display()
        
    def exitApplication(self):
        quit()
        
    def processRequest(self, action):
        pass #TODO

        #TODO Da errores en el import, y no sé porqué. No puedo avanzar hasta que esté

#Test section

#f = FriendController(FriendModel())
#f.exitApplication()
print("hola")