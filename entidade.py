import pygame
import copy
class Entidade:
	def __init__(self,root,x,y,larg,alt,circle=False,elasticidade=100000000000,estado=None):
		self.root=root
		self.x = x
		self.y = y

		self.larg = larg
		self.alt = alt
		self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
		self.x_draw = self.rect.left - self.root.camera.camera[0]
		self.y_draw = self.rect.top - self.root.camera.camera[1]
		self.gravidade = 0.5
		self.velocidade = [0,0]
		self.direcao = [0,0]
		self.surface = pygame.Surface((self.larg,self.alt))
		self.sensores={'botton':False,"left":False,'right':False,'top':False}
		self.val_jump=10
		self.veloMov=5
		self.movimento={"left":False,'right':False}
		self.circle=circle
		self.elasticidade=elasticidade
		self.lado_virado='left'
		self.visualiza_box=False
		
		self.estado=estado
		self.atraso_ativado=False
		self.atrasa_estado=0
		self.proximoEstado=0

	def segura_estado(self,num,estado,proximoEstado):
		self.atrasa_estado=num
		self.estado=estado
		self.proximoEstado=proximoEstado
		self.atraso_ativado=True
	def estado_altera(self,estado):
		self.estado=estado
	def atualiza_estado(self):
		self.atrasa_estado-=1
		self.altera_estado()
	def altera_estado(self):
		if(self.atraso_ativado and self.atrasa_estado<0):
			self.estado=self.proximoEstado
			self.atraso_ativado=False
	def collision_test(self,rect,tiles):
		collisions = []
		for tile in tiles:
			if rect.colliderect(tile.rect):
				collisions.append(tile.rect)
		return collisions

	def detceta_colision(self,rect,movement,tiles): # movement = [5,2]
		rect.y += movement[1]
		collisions = self.collision_test(rect,tiles)
		#self.sensores={'botton':False,"left":False,'right':False,'top':False}
		for tile in collisions:
			if movement[1] > 0:
				self.sensores['botton']=True
				rect.bottom = tile.top
				if(self.velocidade[1]>3):
					self.velocidade[1]=(self.velocidade[1]*-1)/self.elasticidade
				else:
					self.velocidade[1]=0
			
			if movement[1] < 0:
				self.sensores['top']=True
				rect.top = tile.bottom
				self.velocidade[1]=0
				

		rect.x += movement[0]
		collisions = self.collision_test(rect,tiles)
		for tile in collisions:
			if movement[0] > 0:
				self.sensores['right']=True
				
				self.velocidade[0]=(self.velocidade[0]*-1)/self.elasticidade
				if(self.velocidade[1]>1  ):
					
					self.velocidade[1]=1
					
				rect.right = tile.left
			if movement[0] < 0:
				self.sensores['left']=True
				
				self.velocidade[0]=(self.velocidade[0]*-1)/self.elasticidade
				if(self.velocidade[1]>1):
					
					self.velocidade[1]=1
					
				rect.left = tile.right
		
		return rect
	def move(self,dir,acao):
		self.movimento[dir]=acao
	def moverse(self):
		if self.movimento['left']:
			#self.posi[0]-= self.veloMov
			self.lado_virado='left'
			self.direcao[0]-=self.veloMov
			
		if self.movimento['right']:
			self.lado_virado='right'
			self.direcao[0]+=self.veloMov
			
	def detecta_cair(self):
		if(self.velocidade[1]>3):
			self.sensores['botton']=False
	def jump(self):
		self.velocidade[1]=-self.val_jump
		self.sensores['botton']=False
	def update(self):
		pass
	def updatePai(self,blocos_colide):
		self.update()
		self.velocidade[1]+=self.gravidade
		self.direcao=[0,0]
		self.direcao[1]+=self.velocidade[1]
		self.direcao[0]+=self.velocidade[0]
		self.moverse()
		self.rect=self.detceta_colision(self.rect,self.direcao,blocos_colide)
		self.detecta_cair()
		self.atualiza_estado()

		
	def render(self,screen):
		pass
	def renderPai(self,screen):
		self.x_draw = self.rect.left - self.root.camera.camera[0]
		self.y_draw = self.rect.top - self.root.camera.camera[1]

		if(self.visualiza_box):
			color=(180,20,50)
			
			if(self.sensores['botton']):
				self.surface.fill((5,70,255))
				color=(5,70,255)
			else:
				self.surface.fill((180,20,50))
			if(self.circle):
				pygame.draw.circle(screen, color, (self.rect.left+self.larg/2,self.rect.top+self.alt/2),self.larg/2)
			else:
				screen.blit(self.surface,(self.x_draw,self.y_draw))
		self.render(screen)
		#pygame.draw.rect(screen,(250,25,20), self.rect)