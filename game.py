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
pantalla = pygame.display.set_mode(dimensiones)



#CLASES
#--------------------------------------------------
class Bomba(pygame.sprite.Sprite):
	vinicial = 5
	angulo = 0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([5,5])
		self.image.fill(NEGRO)
		self.image.set_colorkey(BLANCO)
		#pygame.draw.ellipse(self.image, NEGRO, [6,500,5,5])
		self.rect = self.image.get_rect()
	def mover(self,tiempo):
		self.rect.x = 6+self.vinicial*math.cos(math.radians(self.angulo))*tiempo
		self.rect.y = 500+(self.vinicial*math.sin(math.radians(self.angulo))*tiempo-((0.0098*tiempo*tiempo)/2))*-1
	def verificaLimitePantalla(self):
		if self.rect.x>1200:
			return True
		else:
			return False

class Proyectil(pygame.sprite.Sprite):
	tiempo = 1
	angulo = 0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([5,5])
		self.image.fill(ROJO)
		self.image.set_colorkey(BLANCO)
		#pygame.draw.ellipse(self.image, ROJO, [600,500,5,5])
		self.rect = self.image.get_rect()
		self.tiempo = 1
		self.angulo = 0
	def disparar(self,xangulo):
		self.angulo = xangulo
	def update(self):
		pos = 550+((math.tan(math.radians(self.angulo))*self.tiempo)*-1)
		print(self.tiempo)
		print(pos)
		self.rect.x = 1180-self.tiempo
		self.rect.y = pos	
		self.tiempo = self.tiempo +8
		
		
		

class escudoDeHierro():
	def __init__(self):
		pygame.draw.line(pantalla,NEGRO,[1140,530],[1180,550],5)
	def dibujar(self,angulo):
		coordenadax=0.0
		coordenaday=0.0
		ladoa=0
		ladob=0
		ladoa=(math.sin(math.radians(angulo))*40)
		ladob=(math.sqrt((40*40)-(ladoa*ladoa)))
		coordenadax = 1180 - ladob
		coordenaday = 550 - ladoa
		pygame.draw.line(pantalla,NEGRO,[coordenadax,coordenaday],[1180,550],5)




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
	contador=0
	angulo_escudo=45

	imagen_fondo = pygame.image.load("fondo.png")
	pygame.display.set_caption("Atack")
	hecho = False
	#soldado = GIFImage("soldado.gif")
	reloj = pygame.time.Clock()

	bomba_lista = pygame.sprite.Group()
	proyectiles_lista = pygame.sprite.Group()

	for i in range (50):
		bomba_lanzada = Bomba()
		bomba_lanzada.rect.x =6;
		bomba_lanzada.rect.y =500;
		bomba_lanzada.angulo = random.randint(15,40)
		bomba_lista.add(bomba_lanzada)
	escudo = escudoDeHierro()


	#Eventos de procesamiento
	while not hecho:
		
		for evento in pygame.event.get(): #acciones del usuario
			if evento.type == pygame.QUIT:
				hecho = True
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_UP:
					angulo_escudo = angulo_escudo + 3
				if evento.key == pygame.K_DOWN:
					angulo_escudo = angulo_escudo - 3
				if evento.key == pygame.K_SPACE:
					proyectil_lanzado = Proyectil()
					proyectil_lanzado.rect.x=1180
					proyectil_lanzado.rect.y=550
					proyectil_lanzado.disparar(angulo_escudo)
					proyectiles_lista.add(proyectil_lanzado)

					

		
		#Logica del jueo
		#bomba_lista.mover(x/2)
		if contador<=47:
			bomba_lanzada = bomba_lista.sprites()[contador]
			if bomba_lanzada.verificaLimitePantalla()==True:
				contador = contador +1
				x=0
				bomba_lanzada = bomba_lista.sprites()[contador]
			bomba_lanzada.mover(x/2)
		x = x + 1
		proyectiles_lista.update()

		#Dibujo
		pantalla.fill(BLANCO)
		pantalla.blit(imagen_fondo,[0,0])
		#bomba_lista.draw(pantalla)
		#soldado.render(pantalla,(x,y))
		#pygame.draw.ellipse(pantalla,NEGRO,[5+ejex(5,30,x/2),550+(ejey(5,30,x/2)*-1),8,8])
		#bomba_lista.mover(self,x)
		#bomba_lanzada.mover(x/2)
		#pygame.draw.line(pantalla,NEGRO,[1140,530],[1180,550],5)
		escudo.dibujar(angulo_escudo)
		bomba_lista.draw(pantalla)
		proyectiles_lista.draw(pantalla)


		reloj.tick(60)
		pygame.display.flip()

	return 0;

if __name__ == '__main__':
	pygame.init()
	main()
	pygame.quit()


