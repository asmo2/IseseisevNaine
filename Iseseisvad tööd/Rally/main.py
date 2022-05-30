import pygame

pygame.init()

screenX = 640
screenY = 480

screen = pygame.display.set_mode((screenX, screenY))

clock = pygame.time.Clock()

blue = [0,45,167]
f1_blue = pygame.image.load("img/f1_blue.png")
f1_red = pygame.image.load("img/f1_red.png")
bg_rally = pygame.image.load("img/bg_rally.jpg")

f1_blue_speed = 3
f1_blue_posY = 344

f1_red_speed = 3
f1_red_posY = 230

bg_rally_speed = 5
bg_rally_posY = 0
while True:
    clock.tick(60)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()
    f1_red_posY -= f1_red_speed
    f1_blue_posY -= f1_blue_speed
    bg_rally_posY += bg_rally_speed

    screen.blit(bg_rally, (0, bg_rally_posY))
    screen.blit(f1_blue, (300, f1_blue_posY))
    screen.blit(f1_red, (200, f1_red_posY))
    # screen.fill(blue)
    pygame.display.flip()
