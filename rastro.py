import pygame
class Rastro:
	def __init__(self,radial,root,cor=(150,50,50),min=10,dmin=1.5):
		
		self.radial=radial
		self.root=root
		self.velo=dmin
		self.cor=cor
		self.rastros=[]
		self.min=min
		self.tam_rastro=[]
		
	def add(self,posi):
		surface=pygame.Surface((self.radial,self.radial))
		pygame.draw.circle(surface, self.cor, (0,0), self.radial)
		self.rastros.append([surface,posi[0],posi[1]])
		
		self.tam_rastro.append(self.radial)
	def update(self):
		#self.radial-=self.velo
		for i in range(len(self.tam_rastro)):
			self.tam_rastro[i]-=self.velo
			if(self.tam_rastro[i]>0):
				self.rastros[i][0]=pygame.transform.scale(self.rastros[i][0], (self.tam_rastro[i], self.tam_rastro[i]))

		for i in range(len(self.rastros)):
			try:
				if(self.tam_rastro[i]<self.min):

					self.rastros.remove(self.rastros[i])
					self.tam_rastro.remove(self.tam_rastro[i])
					
			except:
				pass


	def render(self,screen):
		for i in range(len(self.rastros)):
			try:
				pygame.draw.circle(screen, self.cor, (self.rastros[i][1]-self.root.camera.camera[0],self.rastros[i][2]-self.root.camera.camera[1]), self.tam_rastro[i]-5)
			except:
				pass