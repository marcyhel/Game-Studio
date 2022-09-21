import pygame
import copy
from rastro import *
from entidade import*
from projetil import*
from spritSheet import*
from poder_onda_chao import*
from estados_player import *
	
class Player(Entidade):
	def __init__(self,root,x,y):
		super().__init__(root,x,y,40,60,estado=Estado.normal,elasticidade=10)
		self.rastro=Rastro(25,root)

		self.sprite_idle=SpriteSheet('sprite/newPlayer/Player/Idle/',12,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_run=SpriteSheet('sprite/newPlayer/Player/Run/',7,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_jump=SpriteSheet('sprite/newPlayer/Player/Jump/',13,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_queda=SpriteSheet('sprite/newPlayer/Player/Jump/',13,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)

		self.sprite_grenade_idle=SpriteSheet('sprite/newPlayer/Player/IdleGrenade/',12,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_grenade_run=SpriteSheet('sprite/newPlayer/Player/RunGrenade/',7,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_grenade_jump=SpriteSheet('sprite/newPlayer/Player/JumpGrenade/',13,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_grenade_queda=SpriteSheet('sprite/newPlayer/Player/JumpGrenade/',13,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)

		self.sprite_knife_idle=SpriteSheet('sprite/newPlayer/Player/IdleKnife/',12,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_knife_run=SpriteSheet('sprite/newPlayer/Player/RunKnife/',7,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_knife_jump=SpriteSheet('sprite/newPlayer/Player/JumpKnife/',13,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_knife_queda=SpriteSheet('sprite/newPlayer/Player/JumpKnife/',13,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)

		self.sprite_grenade_pega=SpriteSheet('sprite/newPlayer/Player/TakeGrenade/',11,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)
		self.sprite_knife_pega=SpriteSheet('sprite/newPlayer/Player/TakeKnife/',8,80,80,colorkey=(0,0,0),atraso=5,size=2,unida=False)

		self.id_sprite=0;
		self.id_sprite_anterior=0;
		self.visualiza_box=False

		



	
	
	def update(self):
		self.rastro.update()
		self.rastro.add([self.rect.centerx,self.rect.centery])

		if((self.movimento['left'] or self.movimento['right'] )and self.sensores['botton']):
			self.id_sprite=1
		elif(self.sensores['botton']==False and self.velocidade[1]<0):
			self.id_sprite=2
		elif(self.sensores['botton']==False and self.velocidade[1]>=0):
			self.id_sprite=3
		else:
			self.id_sprite=0
		if(self.estado==Estado.vazio):
			self.estado=Estado.normal
		if((self.id_sprite!=self.id_sprite_anterior) or (self.estado==self.proximoEstado)):
			self.id_sprite_anterior=self.id_sprite
			self.proximoEstado=Estado.vazio
			self.sprite_run.reset_animate()
			self.sprite_jump.reset_animate(inicio=2,fim=8)
			self.sprite_idle.reset_animate()
			self.sprite_queda.reset_animate(inicio=6,fim=8)

			self.sprite_grenade_run.reset_animate()
			self.sprite_grenade_jump.reset_animate(inicio=2,fim=8)
			self.sprite_grenade_idle.reset_animate()
			self.sprite_grenade_queda.reset_animate(inicio=6,fim=8)

			self.sprite_knife_run.reset_animate()
			self.sprite_knife_jump.reset_animate(inicio=2,fim=8)
			self.sprite_knife_idle.reset_animate()
			self.sprite_knife_queda.reset_animate(inicio=6,fim=8)

			self.sprite_grenade_pega.reset_animate()
			self.sprite_knife_pega.reset_animate()
	def atirar(self):
		if(self.lado_virado=='right'):
			self.root.projetil.append(Projetil(self.root,self.rect.left+40,self.rect.top,[3,-10]))
		if(self.lado_virado=='left'):
			self.root.projetil.append(Projetil(self.root,self.rect.left ,self.rect.top,[-3,-10]))
	def poder_wave(self):
		self.root.poder_wave.append(Poder_onda_chao(self.root,[self.rect.left,self.rect.bottom],0,7,8,15))
		self.root.poder_wave.append(Poder_onda_chao(self.root,[self.rect.left,self.rect.bottom],1,7,8,15))
	def render(self,screen):

		if(self.estado==Estado.normal):
			if(self.id_sprite==1):
				self.sprite_run.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])

			elif(self.id_sprite==2):
				self.sprite_jump.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])
			elif(self.id_sprite==3):
				self.sprite_queda.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]],loop=False)
			elif(self.id_sprite==0):

				self.sprite_idle.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])
		if(self.estado==Estado.granada):
			if(self.id_sprite==1):
				self.sprite_grenade_run.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])

			elif(self.id_sprite==2):
				self.sprite_grenade_jump.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])
			elif(self.id_sprite==3):
				self.sprite_grenade_queda.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]],loop=False)
			elif(self.id_sprite==0):

				self.sprite_grenade_idle.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])
		if(self.estado==Estado.granada_pega):
			self.sprite_grenade_pega.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]],loop=False)
		if(self.estado==Estado.knife_pega):
			self.sprite_knife_pega.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]],loop=False)

		if(self.estado==Estado.knife):
			if(self.id_sprite==1):
				self.sprite_knife_run.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])

			elif(self.id_sprite==2):
				self.sprite_knife_jump.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])
			elif(self.id_sprite==3):
				self.sprite_knife_queda.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]],loop=False)
			elif(self.id_sprite==0):

				self.sprite_knife_idle.animate(self.lado_virado,screen,[self.x_draw,self.y_draw],ajuste=[[-65,-60],[-55,-60]])
		
