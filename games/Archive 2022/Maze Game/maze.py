import random

class Maze:
    def __init__(self, dim) -> None:
        self.dim = dim
        self.generate_new()

    def __check_link(self, cell, links):
        #print(cell)
        if self.vis[cell[0]][cell[1]]:
            return
        self.vis[cell[0]][cell[1]] = True
        for l in links[cell[0]][cell[1]]:
            self.__check_link(l,links)

    def __are_linked(self, cells, links):
        x1,y1,x2,y2 = cells
        self.vis = []
        for i in range(self.dim[0]):
            self.vis.append([])
            for j in range(self.dim[1]):
                self.vis[i].append(False)

        self.__check_link((x1,y1), links)
        if self.vis[x2][y2]:
            return True
        return False



    def generate_new(self):
        #done = []
        todo = []
        doors = []
        links = []
        for i in range(self.dim[0]):
            links.append([])
            for j in range(self.dim[1]):
                links[i].append([])
                todo.append((i,j))

        while len(todo) > 0:
            x,y = random.choice(todo)
            
            w = []
            if x-1>=0:
                if not (x-1, y, x, y) in doors:
                    w.append((x-1, y, x, y))
            if x+1<self.dim[0]:
                if not (x,y,x+1,y) in doors:
                    w.append((x, y, x+1, y))
            if y-1>=0:
                if not (x,y-1,x,y) in doors:
                    w.append((x, y-1, x, y))
            if y+1<self.dim[1]:
                if not (x,y,x,y+1) in doors:
                    w.append((x, y, x, y+1))
            

            random.shuffle(w)

            n_linked = 0
            for p in w:
                if not self.__are_linked(p, links):
                    n_linked +=1
                    if n_linked == 1:
                        x1,y1,x2,y2 = p
                        doors.append(p)
                        links[x1][y1].append((x2,y2))
                        links[x2][y2].append((x1,y1))
                    

            if n_linked <= 1:
                todo.remove((x,y))

        self.doors = doors

            


