import random
from cell import Cell


class Maze: 

    def __init__(self,size):
        self.size = size
        self.maze = [[Cell() for i in range (size)] for j in range (size)]
        self.start = (0 , 0)
        self.traveler_cell = self.start
        self.end = (size - 1 , size - 1)
        self.stack = []

        

    def print_maze(self):
        maze_display = [["#" for _ in range(2 * self.size +1)] for _ in range(2 * self.size + 1)]
        for row in range(self.size):
            for col in range(self.size):
                if self.maze[row][col].visited:  
                    maze_display[2 * row + 1][2 * col + 1] = "."
                    if self.maze[row][col].walls['top']:
                        maze_display[2 * row][2 * col + 1] = "#"
                    else:
                        maze_display[2 * row][2 * col + 1] = "."
                    if self.maze[row][col].walls['bottom']:
                        maze_display[2 * row + 2][2 * col + 1] = "#"
                    else:
                        maze_display[2 * row + 2][2 * col + 1] = "."
                    if self.maze[row][col].walls['left']:
                        maze_display[2 * row + 1][2 * col] = "#"
                    else:
                        maze_display[2 * row + 1][2 * col] = "."
                    if self.maze[row][col].walls['right']:
                        maze_display[2 * row + 1][2 * col + 2] = "#"
                    else:
                        maze_display[2 * row + 1][2 * col + 2] = "."
                    if self.maze[row][col].mark == 'O':
                        maze_display[2 * row + 1][2 * col + 1] = "O"
                    elif self.maze[row][col].mark == '*':
                        maze_display[2 * row + 1][2 * col + 1] = "*"
                else:  
                    maze_display[2 * row + 1][2 * col + 1] = "."
        maze_display[1][0] = "."
        maze_display[2*self.size - 1][2*self.size] = "."
        maze_str = ""
        for line in maze_display:
            maze_str += " ".join(line) + "\n"
        print(maze_str)
        self.printotextfile = maze_str
        return maze_str


       
    
    def getcell(self,x,y):
        return self.maze[y][x] 


    def backtracking_gene(self, start):
        x = start[0]
        y = start[1]
        cell = self.getcell(x,y)
        directions = [(0,1),(-1,0),(1,0),(0,-1)]
        random.shuffle(directions)
        cell.visited = True
        for dx, dy in directions:
            n_x, n_y = x + dx, y + dy 
            if 0 <= n_x < self.size and 0 <= n_y < self.size:
                neighbor = self.getcell(n_x,n_y)
                if not neighbor.visited == True:

                    if dx == 1: 
                        cell.break_wall('right', neighbor)
                    elif dx == -1 :
                        cell.break_wall('left', neighbor)
                    elif dy ==  -1:
                        cell.break_wall('top', neighbor)
                    elif dy == 1:
                        cell.break_wall('bottom', neighbor)
                    self.backtracking_gene((n_x,n_y))                    
    #fonction génératrice de labyrinthe avec kruskal
    def kruskal_gene(self):
        allcells = [(x, y) for x in range(self.size) for y in range(self.size)]
        random.shuffle(allcells)
        for x, y in allcells:
            cellule = self.getcell(x, y)
            if not cellule.visited:
                cellule.visited = True
                
                directions = [(0,1),(-1,0),(1,0),(0,-1)]
                random.shuffle(directions)
                for dx, dy in directions:
                    n_x, n_y = x + dx, y + dy 
                    if 0 <= n_x < self.size and 0 <= n_y < self.size:
                        neighbor = self.getcell(n_x,n_y)
                        if not neighbor.visited == True:
                            
                            if cellule.find() != neighbor.find():
                                if dx == 1: 
                                    cellule.break_wall('right', neighbor)
                                elif dx == -1 :
                                    cellule.break_wall('left', neighbor)
                                elif dy ==  -1:
                                    cellule.break_wall('top', neighbor)
                                elif dy == 1:
                                    cellule.break_wall('bottom', neighbor)
                                cellule.union(neighbor)
   
   
    
    def save(self, filename):
        with open(f"{filename}.txt", "w") as f:
            print(self.printotextfile, file=f)
   
   
    def reset_visited(self):
        for row in range(self.size):
            for col in range(self.size):
                self.maze[row][col].visited = False

    def backtracking_solve(self, start, end,filename):
        stack = []
        x, y = start
        end_x, end_y = end
        stack.append((x, y))

        while len(stack) > 0:
            x, y = stack[-1]
            if (x, y) == (end_x, end_y):
                print(stack)
                break  

            cell = self.maze[y][x]
            cell.visited = True 

            found_neighbor = False  

            directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
            random.shuffle(directions)

            for dx, dy in directions:
                n_x, n_y = x + dx, y + dy
                if 0 <= n_x < self.size and 0 <= n_y < self.size:
                    neighbor = self.maze[n_y][n_x]
                    if not neighbor.visited:
                        
                        if dx == 1 and not cell.walls['right']:
                            stack.append((n_x, n_y))
                            found_neighbor = True
                            break
                        elif dx == -1 and not cell.walls['left']:
                            stack.append((n_x, n_y))
                            found_neighbor = True
                            break
                        elif dy == 1 and not cell.walls['bottom']:
                            stack.append((n_x, n_y))
                            found_neighbor = True
                            break
                        elif dy == -1 and not cell.walls['top']:
                            stack.append((n_x, n_y))
                            found_neighbor = True
                            break

            if not found_neighbor:
                self.maze[y][x].mark = '*'
                stack.pop()  

        for x, y in stack:
            self.maze[y][x].mark = 'O'

        if (x, y) == (end_x, end_y):
            print("La fin a été atteinte!")
        else:
            print("La fin n'a pas été atteinte!")

        self.print_maze()


maze = Maze(5)
maze.backtracking_gene((0,0))

maze.print_maze()
filename = input("Veuillez entrer le nom du fichier : ")
maze.save(filename)


maze.reset_visited()

maze.backtracking_solve((0, 0), (maze.size - 1, maze.size - 1),filename)
maze.save(filename)