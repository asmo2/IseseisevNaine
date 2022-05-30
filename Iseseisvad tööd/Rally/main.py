import pygame
import random

pygame.init()

screenX = 640
screenY = 480

screen = pygame.display.set_mode((screenX, screenY))

clock = pygame.time.Clock()

blue = [0, 45, 167]
f1_blue_image = pygame.image.load("img/f1_blue.png")
f1_red_image = pygame.image.load("img/f1_red.png")
f1_red_image = pygame.transform.rotate(f1_red_image, 180)
bg_rally = pygame.image.load("img/bg_rally.jpg")
bg_rally2 = pygame.image.load("img/bg_rally.jpg")

f1_blue_posY = 344
f1_blue_posX = 300

f1_red_speed = 8
f1_red_posY = 230
f1_red_posX = 300

bg_rally_speed = 5
bg_rally_posY = 0

bg_rally2_posY = -480
while True:
    clock.tick(60)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and f1_blue_posX != 180:
                f1_blue_posX -= 120

            if i.key == pygame.K_RIGHT and f1_blue_posX != 420:
                f1_blue_posX += 120


    f1_red_posY += f1_red_speed  # lahutad positsioonist kiiruse
    bg_rally_posY += bg_rally_speed  # liidab positsioonile kiiruse
    bg_rally2_posY += bg_rally_speed  # liidab positsioonile kiiruse

    screen.blit(bg_rally2, (0, bg_rally2_posY))
    screen.blit(bg_rally, (0, bg_rally_posY))

    f1_blue = pygame.Rect(f1_blue_posX,f1_blue_posY, 45, 90 )
    screen.blit(f1_blue_image, f1_blue)

    f1_red = pygame.Rect(f1_red_posX, f1_red_posY, 45, 90)
    screen.blit(f1_red_image, f1_red)

    if bg_rally_posY > screenY:
        bg_rally_posY = -480
    if bg_rally2_posY > screenY:
        bg_rally2_posY = -480

    if f1_blue_posY < 0 - 90:
        f1_blue_posY = 480

    if f1_red_posY > 480:
        f1_red_posY = -90
        f1_red_speed = random.randrange(6, 15, 1)
    # screen.fill(blue)
    pygame.display.flip()
