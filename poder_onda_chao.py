import copy
import pygame
from spritSheet import*
class Blocos_wave:
	def __init__(self,root,posi,duracao):
		self.root = root
		self.posi=posi
		self.duracao = duracao
		self.larg=50
		self.alt=50
		self.rect = pygame.Rect(self.posi[0],self.posi[1]-self.alt,self.larg,self.alt)
		self.sprite_wave=SpriteSheet('sprite/explode/',9,80,80,colorkey=(0,0,0),atraso=2,size=0.6,unida=False)

	def update(self):
		self.duracao-=1

		if(self.duracao<0):
			self.root.lista_blocos.remove(self)

	def render(self,screen):
		#pygame.draw.rect(screen,(10,80,120), pygame.Rect(self.rect.left-self.root.root.camera.camera[0],self.rect.top-self.root.root.camera.camera[1],self.rect.width,self.rect.height))
		self.sprite_wave.animate('left',screen,[self.rect.left-self.root.root.camera.camera[0],self.rect.top-self.root.root.camera.camera[1]],ajuste=[[-0,2],[0,0]],loop=False)
class Poder_onda_chao:
	def __init__(self,root,posi,dir,qtd,velocidade,duracao):
		self.root = root
		self.posi = posi
		self.dir = dir
		self.qtd = qtd
		self.velocidade = velocidade
		self.duracao = duracao
		self.aux_velo = self.velocidade
		self.lastPosi= copy.deepcopy(self.posi)
		self.lista_blocos = [] 
	def update(self):
		self.aux_velo+=1
		if(self.aux_velo >= self.velocidade and self.qtd>0):
			self.aux_velo=0
			self.qtd-=1
			teste_bloco=Blocos_wave(self,self.lastPosi,self.duracao)
			for i in self.root.blocos:
				if(teste_bloco.rect.colliderect(i)):
					self.qtd=-1
			if(self.qtd>0):
				self.lista_blocos.append(teste_bloco)

			if(self.dir==0):
				self.lastPosi[0]+=50
			if(self.dir==1):
				self.lastPosi[0]-=50
		for i in self.lista_blocos:
			i.update()
	def render(self,screen):
		for i in self.lista_blocos:
			i.render(screen)