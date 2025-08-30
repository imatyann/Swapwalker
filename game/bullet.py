import pygame

class Bullet:
    def __init__(self,color,radius,speed,x,y,is_alive):
        self.color = color
        self.radius = radius
        self.speed = speed
        self.x = x
        self.y = y
        self.is_alive = is_alive

    def draw(self,screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )

    def summon(self,pos_fiest):
        self.x = pos_fiest[0]
        self.y = pos_fiest[1]
    
    def is_out_screen(self,screen_width,screen_height):
        return (self.x < 0) and (self.x > screen_width) and (self.y < 0) and (self.y > screen_height)
    
    def plus_xy(self,dx,dy):
        self.x += dx * self.speed
        self.y += dy * self.speed