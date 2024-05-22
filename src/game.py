import pygame
pygame.init()

clock = pygame.time.Clock()

from src.variables import WHITE, BLACK, BLUE, GREEN, RED
from src.button import Button

class Game:
    def __init__(self) -> None:
        self.w = 1200
        self.h = 1200
        self.window = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("jeu de la vie")
        self.running = True
        self.n_cols = 60
        self.n_rows = 60
        self.cols = self.h // self.n_cols
        self.rows = self.w // self.n_rows
        self.rect_group = [[ 0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        self.init()
        self.menu_open = True
        self.button_menu = Button(self.w // 2 - 100, self.h // 2 - 50, 200, 50, "Run")
        self.pause = True

    def init(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                rect = pygame.Rect(i*self.rows, j*self.cols, self.rows, self.cols)
                self.rect_group[i][j] = [rect, False]

    def draw_grid(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                pygame.draw.rect(self.window, BLACK, self.rect_group[i][j][0], not self.rect_group[i][j][1])

    def menu(self):
        rect = pygame.Rect(0, 0, self.w, self.h)
        pygame.draw.rect(self.window, WHITE, rect)

    
    def delay(time = 1) ->None:
        pass
    
    def update(self):
        change = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                
                if self.rect_bordure(i, j) == 3:
                    change.append([[i, j], True])
                elif self.rect_bordure(i, j) == 2:
                    change.append([[i, j], self.rect_group[i][j][1]])
                else:
                    change.append([[i, j], False])
        
        for rec in change:
            x = rec[0][0]
            y = rec[0][1]
            b = rec[1]
            self.rect_group[x][y][1] = b 
        
        
                
                    
    def is_possible(self, a):
        r = True
        if a[0] == 0 or a[0] == self.n_cols:
            r = False
        elif a[1] == 0 or a[1] == self.n_rows:
            r = False
        
        return r    
    
    def rect_bordure(self, i, j):
        
        all_bord = [[i, j-1], [i, j+1], [i-1, j], [i+1, j],[i+1, j+1], [i+1, j-1], [i-1, j+1], [i-1, j-1]]
        c = 0
        for a in all_bord:
            if self.is_possible(a):
                if(self.rect_group[a[0]] [a[1]] [1]):
                    c += 1
        return c

    def clear_board(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self.rect_group[i][j][1] = False

    def run(self):
        while(self.running):
            if self.menu_open:
                self.menu()
                self.button_menu.draw(self.window)
            else:
                self.window.fill(WHITE)
                if not self.pause: 
                    pygame.display.set_caption(f"jeu de la vie : {clock.get_fps()}")
                    self.update()
                else:
                    pygame.display.set_caption(f"jeu de la vie (pause) : {clock.get_fps()}")
                self.draw_grid()
            pygame.display.update()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not self.menu_open:
                        self.menu_open = True
                    elif event.key == pygame.K_SPACE:
                        self.pause = not self.pause
                    elif event.key == 127:
                        self.clear_board()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button_menu.check_click(event.pos) and self.menu_open:
                            self.menu_open = False
                        elif not self.menu_open:
                            for i in range(self.n_rows):
                                for j in range(self.n_cols):
                                    if self.rect_group[i][j][0].collidepoint(event.pos):
                                        self.rect_group[i][j][1] = not self.rect_group[i][j][1]