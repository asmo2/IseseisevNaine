import pygame
import random

pygame.init()

screenX = 640
screenY = 480

screen = pygame.display.set_mode((screenX, screenY))

clock = pygame.time.Clock() #fps

Score = 0

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
f1_red_posX = 420

bg_rally_speed = 5
bg_rally_posY = 0

bg_rally2_posY = -480

gameover = False
while not gameover:
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

    screen.blit(bg_rally2, (0, bg_rally2_posY)) #uuendab ekraani
    screen.blit(bg_rally, (0, bg_rally_posY)) #uuendab ekraani

    f1_blue = pygame.Rect(f1_blue_posX, f1_blue_posY, 45, 90)
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
        f1_red_posX = random.randrange(180, 540, 120)
        Score += 1

    if f1_red.colliderect(f1_blue):
        gameover = True
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {Score}", True, [255, 255, 255]), [10, 10])
    pygame.display.flip()

while gameover:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()

    screen.fill(blue)
    screen.blit(pygame.font.Font(None, 50).render(f"Skoor: {Score}", True, [255, 255, 255]), [250, 400])
    screen.blit(pygame.font.Font(None, 50).render(f"sitt oled", True, [255, 255, 255]), [320, 225])
    pygame.display.flip()
