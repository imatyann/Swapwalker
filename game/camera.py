import pygame

class Camera:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def move_x(self,value):
        """カメラを水平方向に動かす関数"""
        self.x += value
    def move_y(self,value):
        """カメラを鉛直方向に動かす関数"""
        self.y += value
