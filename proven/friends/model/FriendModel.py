class FriendModel:
    
    def FriendModel(self):
        pass
    
    def find(self, entity):
        """Finds a friend in data source 
        

        Args:
            entity (Friend): Entity to find

        Returns:
            Friend:  Return the friend found or null if not found
        """
        
        
        return None
    
    def add(self, entity):
        """ Adds a new friend to the data source

        Args:
            entity (Friend): Entity to add

        Returns:
            Int: Return 1 if successfully added, 0 otherwise
        """
        
        
        return 0
    
    def modify(self, oldEntity, newEntity):
        """ Modifies the Friend entity

        Args:
            oldEntity (Friend): Old Entity to find
            newEntity (Friend): New entity to replace

        Returns:
            int: Retruns 1 if successfully modified, 0 otherwise
        """
        
        
        return 0
    
    def remove(self, entity):
        """ Removes a friend entity choosen of the data source

        Args:
            entity (Friend): Entity friend

        Returns:
            Int: 1 if succesfully removed, 0 otherwise
        """
        
        
        return 0
    
    def findAll(self):
        """ Gets all friends from the data source

        Returns:
            List<Friend>: A list with all data or an empty list if none is found
        """
        
        return []
    
    def findFriendsNyName(self, name):
        """ Gets a friend from data source by its name

        Args:
            name (String): The name to find on the friend data source

        Returns:
            List<Friend>: A list of friends by its name, an empty list otherwise
        """
        
        
        return []
    
    def __str__(self):
        return None