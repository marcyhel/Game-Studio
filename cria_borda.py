import pygame
import copy
class Cria_borda:
	def __init__(self,surface):
		self.surface = surface
		self.surfaceBorda = pygame.Surface(self.surface.get_size()).convert_alpha()
	def palette_swap(self,surf, old_c, new_c):
		img_copy = pygame.Surface(surf.get_size())
		img_copy.fill(new_c)
		surf.set_colorkey(old_c)
		img_copy.blit(surf, (0, 0))
		return img_copy
	def changColor(self,image, color):
		colouredImage = pygame.Surface(image.get_size())
		colouredImage.fill(color)
		
		finalImage = image.copy()
		finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
		return finalImage
	def perfect_outline_2(img, loc):
		mask = pygame.mask.from_surface(img)
		mask_outline = mask.outline()
		mask_surf = pygame.Surface(img.get_size())
		for pixel in mask_outline:
			mask_surf.set_at(pixel,(255,255,255))
		mask_surf.set_colorkey((0,0,0))
		display.blit(mask_surf,(loc[0]-1,loc[1]))
		display.blit(mask_surf,(loc[0]+1,loc[1]))
		display.blit(mask_surf,(loc[0],loc[1]-1))
		display.blit(mask_surf,(loc[0],loc[1]+1))
	def add(self,surf,x,y,larg=1):
		#aux=copy.deepcopy(surf)
		#aux=self.changColor(surf.copy(),(150,150,150))
		#aux=surf.copy()
		#aux.fill((255,255,255))

		
		#aux.set_alpha(0)
		mask = pygame.mask.from_surface(surf)
		aux = mask.to_surface()
		aux.set_colorkey((0,0,0))
		#self.surfaceBorda.set_colorkey((0,0,0))
		self.surfaceBorda.blit(aux,(x-larg,y))
		self.surfaceBorda.blit(aux,(x+larg,y))
		self.surfaceBorda.blit(aux,(x,y-larg))
		self.surfaceBorda.blit(aux,(x,y+larg))
		self.surfaceBorda.blit(aux,(x,y-2))

		self.surfaceBorda.blit(aux,(x+larg,y+larg))
		self.surfaceBorda.blit(aux,(x-larg,y-larg))
		self.surfaceBorda.blit(aux,(x-larg,y+larg))
		self.surfaceBorda.blit(aux,(x+larg,y-larg))

	def render(self,surface):
		surface.blit(self.surfaceBorda,(0,0))
		self.surfaceBorda = pygame.Surface(self.surface.get_size()).convert_alpha()
