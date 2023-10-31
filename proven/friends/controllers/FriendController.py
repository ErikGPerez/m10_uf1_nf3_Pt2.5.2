from ..model.FriendModel import FriendModel
#from ..views.FriendView import FriendView

class FriendController:
    
    def FriendController(self, model):
        self.model = FriendModel()
        #self.view = FriendView(self, model)
        #view.display()
        
    def exitApplication(self):
        quit()
        
    def processRequest(self, action):
        pass #TODO

        #TODO Da errores en el import, y no sé porqué. No puedo avanzar hasta que esté

#Test section
f = FriendController(fm = FriendModel())
f.exitApplication()