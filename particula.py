import random
import pygame
class Particula:
	def __init__(self,root,x,y,cor=[(200,150,100)],velocidade=1,taxaDiminui=0.3,radial=10):
		self.posi=[x,y]
		self.radial=random.random()*radial+3
		self.velocidade=[(random.random()*2*velocidade)-1*velocidade,(random.random()*2*velocidade)-1*velocidade]
		self.velo=taxaDiminui
		self.cor=random.sample(cor,1)[0]
		self.root=root
	def update(self):
		self.radial-=self.velo
		self.posi[0] += self.velocidade[0]
		self.posi[1] += self.velocidade[1]
		if(self.radial<=0):
			self.root.particula.remove(self)
	def render(self,screen):
		pygame.draw.circle(screen, self.cor, (self.posi[0]-self.root.camera.camera[0],self.posi[1]-self.root.camera.camera[1]), self.radial)