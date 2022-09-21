import pygame
from rastro import *
from entidade import*
from particula import*
class Particula_queda(Entidade):
	
	def __init__(self,root,x,y,cor=[((13,42,253))],velocidade=1,taxaDiminui=0.3,radial=10,dire=[]):
		self.radial=random.random()*radial+3
		super().__init__(root,x,y,self.radial,self.radial,circle=True,elasticidade=3)
		self.cor=random.sample(cor,1)[0]
		self.rastro=Rastro(self.radial,min=1,dmin=0.5,cor=self.cor)
		
		
		self.velocidade=dire#[(random.random()*2*velocidade)-1*velocidade,(random.random()*2*velocidade)-1*velocidade]
		self.velo=taxaDiminui
		
	def update(self):
		self.radial-=self.velo
		self.rastro.radial-=self.velo
		self.rastro.update()
		self.rastro.add([self.rect.centerx,self.rect.centery])
		self.rect=self.rect.inflate(-1.5,-1.5)

		if(self.radial<=0):
			self.root.particula_queda.remove(self)
	
		
	def render(self,screen):
	
		pygame.draw.circle(screen, self.cor, (self.rect.centerx,self.rect.centery), self.rect.height/2)
		self.rastro.render(screen)