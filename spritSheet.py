import pygame
class SpriteSheet:
	def __init__(self,sprite,qtd,x,y, colorkey = None,atraso=10,size=None,unida=True):
		self.sheet = sprite
		self.qtd=qtd
		self.x=x
		self.y=y
		self.lista=[]
		self.lista_imagem=[]
		self.colorkey=colorkey

		self.sprite_Atual=0
		self.cont_Sprite=0
		self.atraso=atraso

		
		self.size=size

		if(unida):
			self.carregaImage_unida()
		else:
			self.carregaImage_saparada()

		self.fimSprite=len(self.lista_imagem)-1
	def carregaImage_saparada(self):
		
		for i in range(self.qtd):
			aux2=pygame.image.load(self.sheet+str(i)+'.png').convert_alpha()
			
			#aux2=self.changColor(aux2,(255- self.color[0],255- self.color[1],255-self.color[2]))
			self.lista_imagem.append(pygame.transform.scale(aux2, (self.x*self.size, self.y*self.size)))
		


	def carregaImage_unida(self):
		self.sheet = pygame.image.load(self.sheet).convert()
		cont=0

		for i in range(self.qtd):
			self.lista.append((cont,0,self.x,self.y))
			cont+=self.x
		
		self.lista_imagem= self.images_at(self.sheet,self.lista,colorkey=self.colorkey)

		
	def image_at(self,sheet, rectangle, colorkey = None):
		"Loads image from x,y,x+offset,y+offset"
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		if(self.size==None):
			return image
		else:
			return pygame.transform.scale(image, (self.x*self.size, self.y*self.size))
		
	def images_at(self,sheet, rects, colorkey = None):
		"Loads multiple images, supply a list of coordinates" 
		return [self.image_at(sheet,rect, colorkey) for rect in rects]
	def reset_animate(self,inicio=0,fim=None):
		self.cont_Sprite=0
		self.sprite_Atual=inicio
		if(fim==None):
			self.fimSprite=len(self.lista_imagem)-1
		else:
			self.fimSprite=fim
	def animate(self,direcao,screen,posi,ajuste=[[0,0],[0,0]],apartir=0,ate=None,loop=True):
		self.cont_Sprite+=1
		if(self.cont_Sprite>=self.atraso):
			self.cont_Sprite=0
			self.sprite_Atual+=1
			if(self.sprite_Atual>=self.fimSprite):

				if(loop):
					self.sprite_Atual=0
				else:
					self.sprite_Atual=self.fimSprite

		image=self.lista_imagem[self.sprite_Atual]
		if(direcao=='left'):
			image=pygame.transform.flip(image, True, False)
			screen.blit(image,(posi[0]+ajuste[0][0],posi[1]+ajuste[0][1]))
		else:
			screen.blit(image,(posi[0]+ajuste[1][0],posi[1]+ajuste[1][1]))
		