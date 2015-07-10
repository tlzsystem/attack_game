import math
import pygame,random
#from GIFImage import *
from pygame.locals import *

#CONSTANTES
NEGRO   = (   0,   0,   0)
BLANCO  = ( 255, 255, 255)
VERDE   = (   0, 255,   0)
ROJO    = ( 255,   0,   0)
dimensiones = (1200, 600)

#CLASES
#--------------------------------------------------
class Bomba(pygame.sprite.Sprite):
	vinicial = 5
	angulo = 0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([5,5])
		self.image.fill(NEGRO)
		pygame.draw.ellipse(self.image, NEGRO, [5,550,5,5])
		self.rect = self.image.get_rect()
		self.image.set_colorkey(BLANCO)
	def mover(self,tiempo):
		self.rect.x = 5+self.vinicial*math.cos(math.radians(self.angulo))*tiempo
		self.rect.y = 550+(self.vinicial*math.sin(math.radians(self.angulo))*tiempo-((0.0098*tiempo*tiempo)/2))*-1


#--------------------------------------------------

#FUNCIONES
#--------------------------------------------------

def ejex(vinicial,angulo,tiempo):
	x = vinicial*math.cos(math.radians(angulo))*tiempo
	return x
def ejey(vinicial,angulo,tiempo):
	y = vinicial*math.sin(math.radians(angulo))*tiempo-((0.0098*tiempo*tiempo)/2)
	return y

#--------------------------------------------------

def main():
	rect_x = 20
	rect_y = 20
	rect_cambio_x = 5
	rect_cambio_y = 5
	x=0
	y=520

	pantalla = pygame.display.set_mode(dimensiones)
	imagen_fondo = pygame.image.load("fondo.png")
	pygame.display.set_caption("Gaza Atack")
	hecho = False
	#soldado = GIFImage("soldado.gif")
	reloj = pygame.time.Clock()
	bomba_lista = pygame.sprite.Group()
	bomba_lanzada = Bomba()
	bomba_lanzada.rect.x =6;
	bomba_lanzada.rect.y =500;
	bomba_lanzada.angulo = random.randint(5,80)
	bomba_lista.add(bomba_lanzada)
	

	#Eventos de procesamiento
	while not hecho:
		reloj.tick(60)
		for evento in pygame.event.get(): #acciones del usuario
			if evento.type == pygame.QUIT:
				hecho = True	
		#Logica del jueo



		#Dibujo
		pantalla.fill(BLANCO)
		pantalla.blit(imagen_fondo,[0,0])
		bomba_lista.draw(pantalla)
		#soldado.render(pantalla,(x,y))
		pygame.draw.ellipse(pantalla,NEGRO,[5+ejex(5,30,x/2),550+(ejey(5,30,x/2)*-1),8,8])
		#bomba_lista.mover(self,x)
		bomba_lanzada.mover(x/2)
		x = x + 1

		pygame.display.flip()

	return 0;

if __name__ == '__main__':
	pygame.init()
	main()
	pygame.quit()


