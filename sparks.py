import pygame
import math
import random
class Sparks:
    def __init__(self,root,posi,angulox,anguloy,larg,cor=[(255,255,255)]):
        self.root=root
        self.posi=posi
        self.angulox=angulox
        self.anguloy=anguloy
        self.larg=larg +random.randint(-2,2)
        self.cor=random.sample(cor,1)[0]
        self.velocidade=5+random.randint(-2,2)
        self.parametro=1
        self.dmin=0.2 +random.random()/3
        novo_posi= [self.posi[0]-self.root.camera.camera[0],self.posi[1]-self.root.camera.camera[1]]
        
        self.poligono=[self.advance(novo_posi.copy(), self.angulox, self.anguloy* self.larg),
            self.advance(novo_posi.copy(), self.angulox + math.pi / 2, self.anguloy* self.larg * 0.1),
            self.advance(novo_posi.copy(), self.angulox + math.pi,  self.anguloy* self.larg * 0.6),
            self.advance(novo_posi.copy(), self.angulox - math.pi / 2,  self.anguloy* self.larg * 0.1),
            ]
    def advance(self,pos, rot, amt):
        pos[0] += math.cos(rot) * amt
        pos[1] += math.sin(rot) * amt
        return pos
    def update(self):
        self.larg -= self.dmin * 1
        self.posi[0] +=math.cos(self.angulox)*self.velocidade*self.parametro 
        self.posi[1] +=math.sin(self.angulox)*self.velocidade*self.parametro
        novo_posi= [self.posi[0]-self.root.camera.camera[0],self.posi[1]-self.root.camera.camera[1]]

        self.poligono=[self.advance(novo_posi.copy(), self.angulox, self.anguloy* self.larg),
            self.advance(novo_posi.copy(), self.angulox + math.pi / 2, self.anguloy* self.larg * 0.1),
            self.advance(novo_posi.copy(), self.angulox + math.pi,  self.anguloy* self.larg * 0.6),
            self.advance(novo_posi.copy(), self.angulox - math.pi / 2,  self.anguloy* self.larg * 0.1),
            ]
        if(self.larg<=0):
            self.root.sparks.remove(self)
    def render(self,screen):
        pygame.draw.polygon(screen, self.cor, self.poligono)
'''

for i in range(5):
                sparks.append([spawn.copy(), angle + math.radians(random.randint(0, 80) - 40), 4 + random.randint(0, 30) / 10, 6, (0, 0, 0)])
            projectiles.append([spawn, vel, 'enemy'])
            sounds['eye_shoot'].play()

    # sparks
    for i, spark in sorted(enumerate(sparks), reverse=True):
        # pos, rot, speed, scale, color
        advance(spark[0], spark[1], spark[2] * dt)
        spark[2] -= 0.2 * dt
        if spark[2] < 0:
            sparks.pop(i)
            continue
        point_list = [
            advance(spark[0].copy(), spark[1], spark[2] * spark[3]),
            advance(spark[0].copy(), spark[1] + math.pi / 2, spark[2] * spark[3] * 0.1),
            advance(spark[0].copy(), spark[1] + math.pi, spark[2] * spark[3] * 0.6),
            advance(spark[0].copy(), spark[1] - math.pi / 2, spark[2] * spark[3] * 0.1),
        ]
        point_list = [[p[0] - scroll[0], p[1] - scroll[1]] for p in point_list]
        pygame.draw.polygon(display, spark[4], point_list)
'''