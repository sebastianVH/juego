import pygame
from clases import disparo

class Nave(pygame.sprite.Sprite): #heredamos la construccion
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave=pygame.image.load("imagenes/nave.png")
        #tomamos el rectangulo de la imagen
        self.rect=self.imagenNave.get_rect()
        #ubicamos la nave de mane inicial
        self.rect.centerx=240
        self.rect.centery=620
        self.velocidad=20 #velocidad de movimiento
        self.vida=True #vida de la nave
        self.listaDisparo=[] #lista de disparos
        self.imagenExplosion=pygame.image.load("imagenes/explosion.png")

    def mover(self): #funcion para el movimiento
        if self.vida == True: #si la nave tiene vida, se mueve
            if self.rect.left <= 0: #con estos if y elif nos asegiramos que no se salga de la pantalla
                self.rect.left=0
            elif self.rect.right > 490:
                self.rect.right= 490



    def disparo(self,x,y): #metodo que utilizaremos para los disparos
        if self.vida ==True:
            misil=disparo.Misil(x,y)
            self.listaDisparo.append(misil)


    def dibujar(self,superficie): #aca dibujamos la nave
        if self.vida == True:
            superficie.blit(self.imagenNave,self.rect)
        else:
            superficie.blit(self.imagenExplosion, self.rect)


