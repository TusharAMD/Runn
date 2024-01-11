from maze import Maze

class Maze_Solver():
    def __init__(self, maze):
        self.maze = maze
        self.solve()

    def solve(self, start=(0,0), end=(-1,-1)):
        if end == (-1,-1):
            end = (self.maze.dim[0]-1, self.maze.dim[1]-1)
        queue = [(start[0],start[1],0)]

        dist = [[-1 for _ in range(self.maze.dim[1])]for _ in range(self.maze.dim[0])]

        while len(queue) > 0:
            x = queue.pop(0)

            if dist[x[0]][x[1]] == -1 or dist[x[0]][x[1]] > x[2]:
                dist[x[0]][x[1]] = x[2]

                if (x[0], x[1], x[0]+1, x[1]) in self.maze.doors and x[0]+1 < self.maze.dim[0]:
                    queue.append((x[0]+1,x[1], x[2]+1))
                if (x[0], x[1], x[0], x[1]+1) in self.maze.doors and x[1]+1 < self.maze.dim[1]:
                    queue.append((x[0],x[1]+1, x[2]+1))
                if (x[0]-1, x[1], x[0], x[1]) in self.maze.doors and x[0]-1 >= 0:
                    queue.append((x[0]-1,x[1], x[2]+1))
                if (x[0], x[1]-1, x[0], x[1]) in self.maze.doors and x[1]-1 >= 0:
                    queue.append((x[0],x[1]-1, x[2]+1))

        self.__solution = [end]
        if end == (0,0) or start == (0,0):
            self.__solution.append((-1,0))
        if end == (self.maze.dim[0]-1, self.maze.dim[1]-1) or start == (self.maze.dim[0]-1, self.maze.dim[1]-1):
            self.__solution.append((self.maze.dim[0]-1, self.maze.dim[1]))

        d = dist[end[0]][end[1]]
        current = (end[0], end[1])
        while d > 0:
            x,y = current
            if x+1 < self.maze.dim[0] and dist[x+1][y] == d-1 and (x,y,x+1,y) in self.maze.doors:
                self.__solution.append((x+1,y))
                current = (x+1,y)
                d-=1
            elif x-1 >= 0 and dist[x-1][y] == d-1 and (x-1,y,x,y) in self.maze.doors: 
                self.__solution.append((x-1,y))
                current = (x-1,y)
                d-=1
            elif y+1 < self.maze.dim[1] and dist[x][y+1] == d-1 and (x,y,x,y+1) in self.maze.doors:
                self.__solution.append((x,y+1))
                current = (x,y+1)
                d-=1
            elif y-1 >= 0 and dist[x][y-1] == d-1 and (x,y-1,x,y) in self.maze.doors:
                self.__solution.append((x,y-1))
                current = (x,y-1)
                d-=1


    def get_solution(self):
        return self.__solution