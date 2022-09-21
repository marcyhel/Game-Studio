import random 
class Camera:
	def __init__(self,x,y,limit_x=None,limit_y=None):
		self.camera = [x,y]
		self.posiFinal = [x,y]
		self.velocidadex = 0
		self.velocidadey = 0
		self.delay = 0.01
		self.maxvelo = 1
		self.sacudir = -1
		self.targuet = None
		self.limit_y = limit_y
		self.limit_x = limit_x
	def novo_targuet(self,elemento):
		self.targuet = elemento
	def update(self):
		novax = self.targuet.rect.centerx
		novay = self.targuet.rect.centery

		self.camera[0] += (novax-self.camera[0]-320)/15
		self.camera[1] += (novay-self.camera[1]-306)/20
		if(self.limit_x!=None  and self.camera[0] < self.limit_x[0] ):
			self.camera[0] = self.limit_x[0] 
		elif(self.limit_x!=None  and self.camera[0] > self.limit_x[1] ):
			self.camera[0] = self.limit_x[1] 
		if(self.limit_y!=None  and self.camera[1] < self.limit_y[0] ):
			self.camera[1] = self.limit_y[0] 
		elif(self.limit_y!=None  and self.camera[1] > self.limit_x[1] ):
			self.camera[1] = self.limit_y[1] 
		self.balanga()
	def trigaSacudir(self):
		self.sacudir = 10
	def balanga(self):
		
		if(self.sacudir >= 0):
			self.sacudir -= 1
			if(self.sacudir % 4):
			
				self.camera[0] += (random.random()*20)-10
				self.camera[1] += (random.random()*20)-10