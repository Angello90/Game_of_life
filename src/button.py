import pygame

from src.variables import WHITE, BLACK, BLUE, GREEN, RED

class Button:
    def __init__(self, x, y, w, h, text) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.button = pygame.Rect(self.x, self.y, self.w, self.h)
        self.font = pygame.font.SysFont('Arial', 25)
    
    def check_click(self, pos):
        if self.button.collidepoint(pos): 
            return True
        else:
            return False

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.button, border_radius=20)
        text = self.font.render(self.text, True, (WHITE))
        text_rect = text.get_rect(center=(self.x + self.w / 2, self.y + self.h / 2))
        surface.blit(text, text_rect)
    