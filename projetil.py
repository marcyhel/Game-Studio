import pygame
from rastro import *
from entidade import*
from particula import*
class Projetil(Entidade):
	
	def __init__(self,root,x,y,velo):
		super().__init__(root,x,y,15,15,circle=True,elasticidade=3)
		self.root = root
		self.velocidade=velo
		self.rastro=Rastro(13,root,min=5,dmin=1.5)
		self.time_some=100
	def update(self):
		self.time_some-=1
		self.rastro.update()
		self.rastro.add([self.rect.centerx,self.rect.centery])
		if(self.time_some<0):
			
			self.root.projetil.remove(self)
		if(self.sensores['botton'] or self.sensores['left']or self.sensores['right']or self.sensores['top']):
			aux=[0,0]
			if(self.sensores['left']):
				aux=aux=[self.velocidade[0]+random.random()*2,-random.randint(2,10)]
				self.root.criaSparks([self.rect.centerx,self.rect.centery],5,0)
				#self.root.criaParticula_queda(1,self.rect.centerx+5,self.rect.centery,dire=aux,taxaDiminui=0.1,cor=[(13,42,253),(11,95,227),(0,164,250),(11,208,227),(13,253,207)])
			if(self.sensores['right']):
				aux=[self.velocidade[0]+random.random()*2,-random.randint(2,10)]
				print(self.velocidade[0])

				#self.root.criaParticula_queda(30,self.rect.centerx-5,self.rect.centery,dire=aux,taxaDiminui=0.1,cor=[(13,42,253),(11,95,227),(0,164,250),(11,208,227),(13,253,207)])
				self.root.criaSparks([self.rect.centerx,self.rect.centery],5,180)
			if(self.sensores['botton']):
				aux=[self.velocidade[0]+random.random()*2,-random.randint(2,5)]
				self.root.criaSparks([self.rect.centerx,self.rect.centery],5,-90)
				#self.root.criaParticula_queda(1,self.rect.centerx,self.rect.centery-5,dire=aux,taxaDiminui=0.1,cor=[(13,42,253),(11,95,227),(0,164,250),(11,208,227),(13,253,207)])
			self.root.criaParticula(10,self.rect.centerx,self.rect.centery,cor=[(60,120,80),(20,100,50),(50,120,60),(60,130,100),(13,120,90)])
			self.root.camera.trigaSacudir()
			self.root.projetil.remove(self)
	def render(self,screen):
		self.rastro.render(screen)