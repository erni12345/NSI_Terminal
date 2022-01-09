from copy import deepcopy
import pygame
from random import randint


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, el):

        self.head = Node(el, self.head)

    def pop(self):

        el = self.head.val
        self.head = self.head.next
        return el



class Laby:
    
    def __init__(self, laby, h, l):
        self.laby = laby
        self.h = h
        self.l = l
        self.resolve = laby.copy()

        format(self)

    
    def make_best(self, start, end, clock):
        """calls maze solve with queue so BFS, but adds at the end the best path

        Args:
            start (tuple): x and y of where to start
            end (tuple): x and y of end
            clock (py game object): pygame clock

        Returns:
            True to siginify done
        """
        path = self.resoudre_laby_queue(start,end,clock)
        for x in path:
            self.laby[x[0]][x[1]] = -2
        self.draw_board()
        return True




    def resoudre_laby_stack(self, start, end,clock):

        """
        solves the labyrinth with stack so DFS

        Returns:
            True to signify end
        """

        stack = Stack()
        stack.push((start, [start]))
        ended = False
        while not ended:
            clock.tick(35)
            self.draw_board()
            x, visited = stack.pop()
            print(x, visited)
            self.laby[x[0]][x[1]] = -1
            vois_de_x = self.voisins(self.laby,x)
            for y in vois_de_x:
                visited_moment = visited.copy()
                visited_moment.append(y)
                stack.push((y,visited_moment))
            if x == end:
                self.laby[x[0]][x[1]] = -1
                ended = True
        self.resolve = self.laby
        return True
            
        
    def resoudre_laby_queue(self, start, end, clock):

        """
        solves laby with BFS

        Returns:
            list of tuples representing best path
        """
        queue = [(start, [start])]
        found = False
        while not found :
            clock.tick(35)
            x, visited = queue.pop(0) 
            if x == end:
                    self.laby[x[0]][x[1]] = -2
                    found = True
                    return visited
            vois_de_x = self.voisins(self.laby, x)
            for y in vois_de_x:
                visited_moment = visited.copy()
                visited_moment.append(y)
                if self.laby[y[0]][y[1]] == 1:
                    self.laby[y[0]][y[1]] = -1
                queue.append((y, visited_moment))

            self.draw_board()
                
            
        return visited

    def voisins(self, T,v):

        """
        gives available neighboughrs of a node x

        INPUTS:
        x = tuple 
        T = matrix

        Returns:
            list of tuples representing neighbouring nodes that can be visited
        """
        V=[]
        i,j=v[0],v[1]
        for a in (-1,1):
            if 0<=i+a<self.h:
                if T[i+a][j]==1 or T[i+a][j]==-3:
                    V.append((i+a,j))
            if 0<=j+a<self.l:
                if T[i][j+a]==1 or T[i][j+a]==-3:
                    V.append((i,j+a))

        return V

    

    def draw_board(self):

        """
        draws maze in oygame window
        """
        for x in range(self.h):
            for y in range(self.l):
                if self.laby[x][y] == 1:
                    pygame.draw.rect(fenster, (255,255,255), pygame.Rect((32*y),(32*x+1), 30, 30))
                elif self.laby[x][y] == -1:
                    pygame.draw.rect(fenster, (255,0,0), pygame.Rect((32*y),(32*x+1), 30, 30))
                elif self.laby[x][y] == 0:
                    pygame.draw.rect(fenster, (0,0,0), pygame.Rect((32*y), (32*x+1), 30, 30))
                elif self.laby[x][y] == -2:
                    pygame.draw.rect(fenster, (0,255,0), pygame.Rect((32*y), (32*x+1), 30, 30))
                elif self.laby[x][y] == -3:
                    pygame.draw.rect(fenster, (0,0,255), pygame.Rect((32*y), (32*x+1), 30, 30))

        pygame.display.update()


    def add_walls(self, pos):

        """
        when clicked on wall will turn the block into its oposite ex: 1-->0 or 0-->1
        """
        x,y = pos
        if x < 1120 and y < 480:
            x =( x // 32)
            y = (y // 32)
            print(x,y)
            if self.laby[y][x] == 1:
                self.laby[y][x] = 0
            else:
                self.laby[y][x] = 1

    
    def add_start_and_end(self, start, end):
        self.laby[start[0]][start[1]] = -3
        self.laby[end[0]][end[1]] = -3

    def reset(self):
        self.laby = self.resolve
        self.draw_board()
        






fenster = pygame.display.set_mode([1280, 720])
fenster.fill((100,100,100))


def main():

    

    laby_tab = []

    for x in range(22):
        med = []
        for y in range(40):
            if randint(0,1) == 1:
                med.append(0)
            else:
                med.append(1)
        laby_tab.append(med)

    clock = pygame.time.Clock()
    running = True
    tab = Laby(laby_tab, 15,35)
    paused = False
    done = False
    start = False
    select_start_and_end = True
    selected_number = 0
    select_walls = False

    clicked = False

    pygame.draw.rect(fenster, (0,255,0), pygame.Rect(500,500, 60, 60))
    pygame.draw.rect(fenster, (0,155,234), pygame.Rect(600,500, 60, 60))
    pygame.draw.rect(fenster, (0,0,0), pygame.Rect(400,500, 60, 60))

    while running:

        if not paused:
            tab.add_start_and_end((3,3),(10,18))
            tab.draw_board()
            if start and not done:
                done = tab.make_best((3,3), (10,18), clock)
            tab.draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.display.set_caption("Paused")
                    paused = not paused

            if event.type == pygame.MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()
                x,y = pos

                clicked = not clicked

                if 600<x<660 and 500<y<560:
                    tab.reset()

                if 400<x<460 and 500<y<560:
                    select_walls = not select_walls
                    
                if 500<x<560 and 500<y<560:
                    start = not start

                if select_walls:
                    tab.add_walls(pos)
                tab.draw_board()



main()