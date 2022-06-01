import pygame
pygame.init()

screenX = 640 #ekraani suurus
screenY = 480

screen = pygame.display.set_mode((screenX, screenY)) #teeb ekraani
clock = pygame.time.Clock()

clock = pygame.time.Clock() #aeg

score = 0

pall_image = pygame.image.load("amg/ball-1.png") #laeb palli
palk_image = pygame.image.load("amg/pad.png") #laeb palgi

palk_image = pygame.transform.scale(palk_image,(120, 20)) #teeb palgi õigeks suuruseks

pall_posY = 100 #palli asukoht
pall_posX = 200
pall_speedX = 5
pall_speedY = 5

palk_posY = 400 #palgi asukoht
palk_posX = 250
palk_speedX = 2


gameover = False
while not gameover:
    clock.tick(60)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()
    screen.fill((1, 43, 24)) #uuendab ekraani(ei tule traili)
    pall_1 = pygame.Rect(pall_posX, pall_posY, 20, 20) # hit detection'i jaoks
    screen.blit(pall_image, pall_1)

    palk_1 = pygame.Rect(palk_posX, palk_posY, 120, 20) # hit detection'i jaoks
    screen.blit(palk_image, palk_1)

    palk_posX += -palk_speedX #palk liigub

    pall_posY += -pall_speedY #pall liigub
    pall_posX += -pall_speedX  # pall liigub

    if pall_posX < 0 or pall_posX > 620: #ei lase pallil minna piiridest välja
        pall_speedX = -pall_speedX
    if pall_posY < 0 or pall_posY > 460:
        pall_speedY = -pall_speedY

    if palk_posX < 0 or palk_posX > 520: #ei lase palgil minna piiridest välja
        palk_speedX = -palk_speedX

    if pall_1.colliderect(palk_1) and pall_speedY < 0: #ei lase pallil minna palgi pealt läbi vaid põrkab minema
        pall_speedY = -pall_speedY


    pygame.display.flip()