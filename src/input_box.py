import pygame


class InputBox:
    def __init__(self, w, h, x, y, text, color_box = (255, 255, 255), color_text = (0, 0, 0)) -> None:
        self.x = x
        self.h = h
        self.text = text
        self.color_box = color_box
        self.color_text = color_text
        self.text_container = pygame.Rect(self.x, self.y, self.w, self.h)
        
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color_box, self.text_container)