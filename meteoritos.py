import time
import pygame, sys
from pygame.locals import *
from clases import jugador
from clases import asteroide
from random import randint

#booleano para comprobar el juego
jugando=True

#variable de ancho y alto de nuetra pantalla
width=480
height=700
listaAsteroides=[]
puntos=0

#funcion carga de asteroides
def cargarAsteroide(x,y):
    meteoro=asteroide.Asteroide(x,y)
    listaAsteroides.append(meteoro)

def gameOver():
    global jugando
    jugando=False
    for meteoritos in listaAsteroides:
        listaAsteroides.remove(meteoritos)

#funcion principal
def meteoritos(): #funcion que controla el juego
    pygame.init() #iniciamos pygame
    window=pygame.display.set_mode((width,height)) #creamos la ventana, pasando el ancho y alto
    #instancioacion de la nave
    nave=jugador.Nave()
    #fondo que usaremos
    background=pygame.image.load("imagenes/espacio.png") #cargamos la imagen

    #titulo del juego
    pygame.display.set_caption("Meteoritos")
    #ciclo de juego
    contador = 0
    puntos = 0
    #fuente de marcador
    fuenteMarcador=pygame.font.SysFont("Arial",30)
    colorFuente=(255,255,255)
    while True:
        #tiempo
        window.blit(background, (0, 0))  # metemos la imagen a la ventana, y la ubicacion
        nave.dibujar(window)
        tiempo = time.time()
        #marcador
        textoMarcador=fuenteMarcador.render("puntos: "+str(puntos),True,colorFuente)
        window.blit(textoMarcador,(0,0))
        # crear asteroides
        if (tiempo - contador) > 0.5:
            contador = tiempo
            posX = randint(2, 478)
            cargarAsteroide(posX, 0)
        # comprobacion lista de asteroide
        if len(listaAsteroides) > 0:
            for x in listaAsteroides:
                if jugando ==True:
                    x.dibujar(window)
                    x.recorrido()
                    if x.rect.top > 700:
                        listaAsteroides.remove(x)
                    else:
                        if x.rect.colliderect(nave.rect):
                            listaAsteroides.remove(x)
                            nave.vida=False
                            gameOver()

        #comprobacion de disparo efectuado
        if len(nave.listaDisparo) >0:
            for x in nave.listaDisparo:
                x.dibujar(window)
                x.recorrido()
                if x.rect.top < -10:
                    nave.listaDisparo.remove(x)
                else:
                    for meteoros in listaAsteroides:
                        if x.rect.colliderect(meteoros.rect):
                            listaAsteroides.remove(meteoros)
                            nave.listaDisparo.remove(x)
                            puntos += 1

        nave.mover()
        for action in pygame.event.get():
            if action.type == QUIT:
                pygame.quit()
                sys.exit()
            elif action.type == pygame.KEYDOWN:
                if jugando ==True:
                    if action.key == K_LEFT:
                        nave.rect.left -= nave.velocidad
                    elif action.key == K_RIGHT:
                        nave.rect.right += nave.velocidad
                    elif action.key == K_SPACE:
                        x,y=nave.rect.center
                        nave.disparo(x,y)
        if jugando == False:
            fuenteGameOver=pygame.font.SysFont("Arial",40)
            textoGameOver=fuenteGameOver.render("Game Over",True,colorFuente)
            window.blit(textoGameOver,(140,350))
        pygame.display.update()

#llamada a la funcion principal
meteoritos()