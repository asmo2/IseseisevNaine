# Initialize the screen
import pygame
# Background
BG = [153, 255, 153]
# Set the screen mode :)
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("IseseisevToo 3: Tsüklid ja funksioonid - Asmo Voitka")
screen.fill(BG)

# Properties
joone_vrv = [255, 0, 0]
ruudud_hor = 0
ridade_arv = 50
ruudud_ver = 0
veergude_arv = 50

# The content :)
screen.fill(BG)

for i in range(ridade_arv):
    pygame.draw.line(screen, joone_vrv, [ruudud_hor, 0], [ruudud_hor, 480], 2)

    # Increase this to make the rect BIGGER
    ruudud_hor += 20

for i in range(veergude_arv):
    pygame.draw.line(screen, joone_vrv, [0, ruudud_ver], [640, ruudud_ver], 2)

    # Increase this to make the rect BIGGER
    ruudud_ver += 20

pygame.display.flip()

# Alumine osa ei lase Pygame ekraanil ise kinni minna.
while True:
    # saab pygame ylevalt x-ist kinni panna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
