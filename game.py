import math
import pygame
from pygame.locals import *

#CONSTANTES
NEGRO   = (   0,   0,   0)
BLANCO  = ( 255, 255, 255)
VERDE   = (   0, 255,   0)
ROJO    = ( 255,   0,   0)
dimensiones = (700, 500)

#CLASES
#--------------------------------------------------

#--------------------------------------------------

#FUNCIONES
#--------------------------------------------------

#--------------------------------------------------

def main():
	rect_x = 20
	rect_y = 20
	rect_cambio_x = 5
	rect_cambio_y = 5

	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Gaza Atack")
	hecho = False
	reloj = pygame.time.Clock()
	#Eventos de procesamiento
	while not hecho:
		reloj.tick(60)
		for evento in pygame.event.get(): #acciones del usuario
			if evento.type == pygame.QUIT:
				hecho = True	
		#Logica del jueo
		#Dibujo
		pantalla.fill(BLANCO)

		pygame.draw.rect(pantalla,ROJO,[rect_x,rect_y,100,50],2)
		rect_x+= rect_cambio_x
		rect_y+= rect_cambio_y

		if rect_y >450 or rect_y <0:
			rect_cambio_y = rect_cambio_y * -1
		if rect_x > 650 or rect_x <0:
			rect_cambio_x = rect_cambio_x * -1

		pygame.display.flip()
	return 0;

if __name__ == '__main__':
	pygame.init()
	main()


