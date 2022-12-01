import pygame

class Misil(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenMisil=pygame.image.load("imagenes/misil.png")
        self.rect=self.imagenMisil.get_rect()
        self.velocidadDisparo=2
        self.rect.top =posY #para que vaya hacia arriba
        self.rect.left=posX

    def recorrido(self): #metodo para el recorrido
        self.rect.top = self.rect.top - self.velocidadDisparo

    def dibujar(self,superficie):
        superficie.blit(self.imagenMisil,self.rect)

