from model.Friend import Friend

class FriendModel:

    def __init__(self):
        self.listFriends = list()
    
    def find(self, entity):
        """Finds a friend in data source 
        

        Args:
            entity (Friend): Entity to find

        Returns:
            Friend:  Return the friend found or null if not found
        """
        if entity != None:
            for Friend in self.listFriends:
                if Friend == entity:
                    return Friend
        else:
            return None
    
    def add(self, entity):
        """ Adds a new friend to the data source

        Args:
            entity (Friend): Entity to add

        Returns:
            Int: Return 1 if successfully added, 0 otherwise
        """
        if entity != None:
            self.listFriends.append(entity)
            opt = 1
        else:
            opt = 0
        return opt
    
    def modify(self, oldEntity, newEntity):
        """ Modifies the Friend entity

        Args:
            oldEntity (Friend): Old Entity to find
            newEntity (Friend): New entity to replace

        Returns:
            int: Retruns 1 if successfully modified, 0 otherwise
        """
        opt = 0
        cont = 0
        if oldEntity != None:
            for Friend in self.listFriends:
                if Friend == oldEntity:
                    self.listFriends[cont] = newEntity
                    opt = 1
                cont += 1
        return opt
    
    def remove(self, entity):
        """ Removes a friend entity choosen of the data source

        Args:
            entity (Friend): Entity friend

        Returns:
            Int: 1 if succesfully removed, 0 otherwise
        """
        if entity != None:
            try:
                self.listFriends.remove(entity)
                opt = 1
            except:
                opt = 0
        else:
            opt = 0
        return opt
    
    def findAll(self):
        """ Gets all friends from the data source

        Returns:
            List<Friend>: A list with all data or an empty list if none is found
        """
        
        return self.listFriends
    
    def findFriendsByName(self, name):
        """ Gets a friend from data source by its name

        Args:
            name (String): The name to find on the friend data source

        Returns:
            List<Friend>: A list of friends by its name, an empty list otherwise
        """
        listNameFriends = list()
        if name != None:
            for Friend in self.listFriends:
                if Friend.name == name:
                    listNameFriends.append(Friend)
        return listNameFriends
    
    def __str__(self): 
        return None 
    