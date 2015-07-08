import math
import pygame

NEGRO   = (   0,   0,   0)
BLANCO  = ( 255, 255, 255)
VERDE   = (   0, 255,   0)
ROJO    = ( 255,   0,   0)
dimensiones = (700, 500)

pygame.init()



pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Gaza Atack")
hecho = False
reloj = pygame.time.Clock()

#Eventos de procesamiento
while not hecho:
	for evento in pygame.event.get(): #acciones del usuario
		if evento.type == pygame.QUIT:
			hecho = True

#Logica del jueo
#Dibujo
	pantalla.fill(BLANCO)

	pygame.draw.line(pantalla,VERDE,[0,0],[100,100],5)
	pygame.draw.line(pantalla,ROJO,[500,500],[100,300],5)

	for desplazar_y in range(0,100,10):
		pygame.draw.line(pantalla,ROJO,[0,10+desplazar_y],[100,110+desplazar_y],5)
	for desplazar_x in range(0,700,10):
		pygame.draw.line(pantalla,NEGRO,[30+desplazar_x,0],[30+desplazar_x,250],5)

	for i in range(200):
 		radianes_x = i / 20
    	radianes_y = i / 6
 
    	x = int( 75 * math.sin(radianes_x)) + 200
    	y = int( 75 * math.cos(radianes_y)) + 200
 
    	pygame.draw.line(pantalla,NEGRO, [x,y], [x+5,y], 5)

	pygame.draw.rect(pantalla,ROJO,[400,36,100,50],2)

	pygame.display.flip()
	reloj.tick(60)

pygame.quit()

