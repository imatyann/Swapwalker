import pygame

class Reticle:
    def __init__(self,width,color):
        self.width = width
        self.color = color

    def draw(self,screen,pos_first,pos_end):
        # 照準の描画関数
        pygame.draw.line(screen,self.color,pos_first,pos_end,self.width)