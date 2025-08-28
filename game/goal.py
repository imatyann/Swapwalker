import pygame

class Goal:
    def __init__(self,x,y,color,width,height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        
    def draw(self,screen,camera_x,camera_y):
        """ゴールを描画する関数"""
        window_y = self.y - camera_y
        window_x = self.x - camera_x
        pygame.draw.rect(screen,self.color,(window_x,window_y,self.width,self.height))

    def is_touch_object(self,x,y):
        """ゴール判定"""
        if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
            return True
        else:
            return False