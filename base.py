from random import randint, random
import sys
import math
import pygame
from player import *
from cria_borda import*
from projetil import*
from particula import*
from particula_queda import*
from sparks import*
from estados_player import *
from camera import*
from poder_onda_chao import*
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('teste')

fps = 60
tempo = pygame.time.Clock()
class Bloco:
    def __init__(self,root,x1,x2,x3,x4):
        self.root=root
        self.rect=pygame.Rect(x1,x2,x3,x4)
    def render(self,surface):

        pygame.draw.rect(surface,(100,180,120), pygame.Rect(self.rect.left-self.root.camera.camera[0],self.rect.top-self.root.camera.camera[1],self.rect.width,self.rect.height))

class Geral:
    def __init__(self,surface):
        self.surface=surface
        self.camera=Camera(500,500)
        self.borda=Cria_borda(self.surface)
        self.blocos=[Bloco(self,100,500,950,50),Bloco(self,100,450,50,50),Bloco(self,50,300,50,200),Bloco(self,950,300,50,200)]
        self.player=Player(self,200,300)
        self.camera.novo_targuet(self.player)
        self.projetil=[]
        self.particula=[]
        self.particula_queda=[]
        self.sparks=[]
        self.itens=[]
        self.poder_wave=[]
    def criaParticula(self,num,x,y,cor=[(200,150,100)],velocidade=1,taxaDiminui=0.3,radial=10):
        for i in range(num):
                self.particula.append(Particula(self,x,y,cor=cor,velocidade=velocidade,taxaDiminui=taxaDiminui,radial=radial))
    def criaSparks(self,posi,num,angle,cor=[(255,255,255)]):
        for i in range(num):
            self.sparks.append(Sparks(self,posi.copy(), math.radians(angle) + math.radians(random.randint(0, 80) - 40), 4 + random.randint(0, 30) / 10, 6,cor=cor))
    def criaParticula_queda(self,num,x,y,cor=[(200,150,100)],velocidade=1,taxaDiminui=0.3,radial=10,dire=[0,0]):
        for i in range(num):
            dir=dire.copy()
            dir[0]+= random.random()
            dir[1]+= random.random()
            self.particula_queda.append(Particula_queda(self,x,y,cor=cor,velocidade=velocidade,taxaDiminui=taxaDiminui,radial=radial,dire=dir))
    def update(self):
        self.player.updatePai(self.blocos)
        self.camera.update()
        if(self.projetil!=[]):
            self.camera.novo_targuet(self.projetil[0])
        else:
            self.camera.novo_targuet(self.player)
        for i in self.particula:
            i.update()
        for i in self.sparks:
            i.update()
        for i in self.poder_wave:
            i.update()
        for i in self.particula_queda:
            i.updatePai(self.blocos)
        for i in self.projetil:
            i.updatePai(self.blocos)

    def render(self):
        #self.borda.render(self.surface)
        for i in self.blocos:
            i.render(self.surface)
        
        for i in self.projetil:
            i.renderPai(self.surface)
        self.player.renderPai(self.surface)
        for i in self.sparks:
            i.render(self.surface)
        for i in self.poder_wave:
            i.render(self.surface)

        for i in self.particula:
            i.render(self.surface)
        for i in self.particula_queda:
            i.render(self.surface)
        

geral=Geral(screen)
while True:
    screen.fill((60,100,60))
    #desenhaRetangulos()
    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.scancode == 26:
                geral.player.jump()
            if event.scancode == 7:
                #play.move=2
                geral.player.move('right',True)
            if event.scancode == 4:
                #play.move=1
                print('d')
                geral.player.move('left',True)
            if event.scancode == 44:
                geral.player.atirar()
                #geral.criaSparks([200,200],5,0)
            if(event.scancode==30):
                geral.player.estado_altera(Estado.normal)
                geral.player.poder_wave()
            if(event.scancode==31):
                geral.player.segura_estado(50,Estado.granada_pega,Estado.granada)
            if(event.scancode==32):
                geral.player.segura_estado(40,Estado.knife_pega,Estado.knife)
            print(event.scancode)
        if event.type == pygame.KEYUP:
            if event.scancode == 7:
                geral.player.move('right',False)
            if event.scancode == 4:
                geral.player.move('left',False)
    geral.render()
    geral.update()
   
    
    
    #for i in range(len(lista_luz)): # seta  posicao das luzes dos vagalumes
    #    iluminacao.set_pos(lista_luz[i], (lista_vag[i].get_posicao()[0]-10,lista_vag[i].get_posicao()[1]-10))
    
    #iluminacao.render() # renderiza a iluminação do ambiente

    #for i in lista_vag: # renderiza a lista de vagalumes e as luzes
    #    i.render()
    
    #iluminacao.set_pos(luz_geral, (pygame.mouse.get_pos()[0]-300,pygame.mouse.get_pos()[1]-300))





    tempo.tick(fps)
    font = pygame.font.Font(None, 30)
    fpss = font.render("fps: "+str(int(tempo.get_fps())), True, pygame.Color('white'))
    screen.blit(fpss, (50, 50))
    pygame.display.update()
