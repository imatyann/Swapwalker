import pygame

class Reticle:
    def __init__(self,width,color):
        self.width = width
        self.color = color

    def draw(self):
        # 照準の描画関数
        