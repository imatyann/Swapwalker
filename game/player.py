import pygame

class Player:
    def __init__(self,color,y,g,fall_speed,on_ground):
        self.color = color
        self.y = y
        self.fall_speed = fall_speed
        self.g = g
        self.on_ground = on_ground


    def draw(self,screen,camera_x,camera_y,center_pos):
        """主人公を描画する関数"""
        pygame.draw.circle(screen,(0,0,0),(center_pos[0],self.y),10)

    def fall(self):
        """重力を実装する関数"""
        if not self.on_ground:
            self.y += self.fall_speed
            self.fall_speed += self.g

    def reset_fall(self):
        """重力加速度をリセットする関数"""
        self.fall_speed = 5