import pygame,random

pygame.init()

sc_size = 650
kl = 50
fps = 5

screen = pygame.display.set_mode([sc_size,sc_size])

dude = pygame.image.load("data/vrag.png")
ship = pygame.image.load("data/ship.png")
clock = pygame.time.Clock()

spBul = []
spProt = []
num_of_prot = 10
for i in range(10):
    spProt.append([kl*(i+1),kl])
x,y = kl*6, kl*11
direct = True
count = 0
while True:
    screen.fill(pygame.Color('white'))
    sp = []
    for i in range(len(spProt)):
        if spProt[i][0] != -1000:
            sp = spProt[i:len(spProt)].copy()
            break
    sp2 = []
    for i in range(len(sp)-1,-1,-1):
        if sp[i][0] != -1000:
            sp2 = sp[0:i+1].copy()
            break
    spProt = sp2.copy()
    
    if direct:
        if spProt[-1][0] != sc_size-kl:
            for i in range(len(spProt)):
                spProt[i][0] += kl
        else:
            direct = False
            if count == 3:
                count = 0
                for i in range(len(spProt)):
                    spProt[i][1] += kl
            else:
                count += 1
    else:
        if spProt[0][0] != 0:
            for i in range(len(spProt)):
                spProt[i][0] -= kl
        else:
            direct = True
            if count == 3:
                count = 0
                for i in range(len(spProt)):
                    spProt[i][1] += kl
            else:
                count += 1

    for i in range(len(spBul)):
        for j in range(len(spProt)):
            if spProt[j][0]<=spBul[i][0]<=spProt[j][0]+49 and spProt[j][1]<=spBul[i][1]<=spProt[j][1]+49:
                spProt[j] = [-1000,-1000]

                
    for i,j in spProt:
        screen.blit(dude,(i,j))
    screen.blit(ship, (x,y))
    sp2 = []
    for i in range(len(spBul)):
        pygame.draw.rect(screen,pygame.Color('black'),(spBul[i][0], spBul[i][1], 10,10))
        spBul[i][1] -= 50
        if spBul[i][1] > 0:
            sp2.append(spBul[i])
    spBul = sp2.copy()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= kl
    if key[pygame.K_RIGHT]:
        x += kl
    if key[pygame.K_UP] and len(spBul)<=3:
        spBul.append([x+20,y-10])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(fps)
