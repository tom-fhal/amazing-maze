class Cell: 
    def __init__(self):
        self.walls = {'left':True,'right':True,'top':True,'bottom':True }
        self.opposite = {'left':'right','right':'left','top':'bottom','bottom':'top' }
        self.visited = False
        self.parent = self  # Au début, chaque cellule est son propre parent
        self.mark = ''


    def getwalls(self):
        return self.walls
    
    def break_wall(self,wall,neighbor):
        if wall in self.walls :
            self.walls[wall] = False
            neighbor.walls[self.opposite[wall]] = False
        return self.walls
    
    def find(self):
        if self.parent != self:
            self.parent = self.parent.find()  # Compression de chemin
        return self.parent

    def union(self, other):
        root1 = self.find()
        root2 = other.find()
        if root1 != root2:
            root1.parent = root2  # Fusionne les ensembles
    
    def setisvisited(self):
        self.visited =  True