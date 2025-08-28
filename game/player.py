import pygame

class Player:
    def __init__(self,color,x,y,g,fall_speed,on_ground,radius):
        self.color = color
        self.x = x
        self.y = y
        self.fall_speed = fall_speed
        self.g = g
        self.on_ground = on_ground
        self.radius = radius


    def draw(self,screen,camera_x,camera_y,center_pos):
        """主人公を描画する関数"""
        window_y = self.y - camera_y
        window_x = self.x - camera_x
        pygame.draw.circle(screen,self.color,(center_pos[0],window_y),self.radius)

    def fall(self):
        """重力を実装する関数"""
        if not self.on_ground:
            self.y += self.fall_speed
            self.fall_speed += self.g

    def reset_fall(self):
        """重力加速度をリセットする関数"""
        self.fall_speed = 5

    def move_x(self,value):
        """主人公を水平方向に動かす関数"""
        self.x += value
    def move_y(self,value):
        """主人公を鉛直方向に動かす関数"""
        self.y += value