import pygame

pygame.init()

screenX = 640
screenY = 480

screen = pygame.display.set_mode((screenX, screenY))

clock = pygame.time.Clock()

score = 0

blue = [0, 45, 167]

pall_image = pygame.image.load("amg/ball-1.png")
palk_image = pygame.image.load("amg/pad.png")

pygame.transform.scale(palk_image, (120, 20))

pall_posY = 100
pall_posX = 200

palk_posY = 400
palk_posX = 250

gameover = False
while not gameover:
    clock.tick(60)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()
    pall_1 = pygame.Rect(pall_posX, pall_posY, 20, 20)
    screen.blit(pall_image, pall_1)

    palk_1 = pygame.Rect(palk_posX, palk_posY, 120, 20)
    screen.blit(palk_image, palk_1)

    pygame.display.flip()