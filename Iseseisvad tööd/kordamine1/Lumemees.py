import pygame
# impordib mooduli pygame
import sys
# impordib mooduli sys

screen = pygame.display.set_mode([300, 300])
#
pygame.display.set_caption("Lumemees")
# Paneb display nime lumemeheks
screen.fill([0, 0, 0])
# Täidab ekraani mustaga
pygame.draw.circle(screen, [255, 255, 255], [150, 85], 30, 0)
# pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen, [0, 0, 0], [160, 80], 5, 0)
# pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen, [0, 0, 0], [140, 80], 5, 0)
# pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.polygon(screen, [255, 0, 0], [[145, 90], [150, 105], [155, 90]])


# pygame.draw.polygon(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen, [255, 255, 255], [150, 150], 40, 0)
# pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen, [255, 255, 255], [150, 235], 50, 0)
# pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.display.update()
# Uuendab akent viimaste muudatustega


#
### LISA
#

pygame.draw.line(screen, [153, 102, 51], [190, 150], [200, 110], 2)
pygame.draw.line(screen, [153, 102, 51], [200, 110], [200, 100], 2)
pygame.draw.line(screen, [153, 102, 51], [200, 110], [195, 100], 2)
pygame.draw.line(screen, [153, 102, 51], [200, 110], [205, 100], 2)
# parem käsi

pygame.draw.line(screen, [153, 102, 51], [110, 150], [100, 110], 2)
pygame.draw.line(screen, [153, 102, 51], [100, 110], [100, 100], 2)
pygame.draw.line(screen, [153, 102, 51], [100, 110], [95, 100], 2)
pygame.draw.line(screen, [153, 102, 51], [100, 110], [105, 100], 2)
# vasak käsi

pygame.draw.polygon(screen, [50, 50, 50], [[125, 70], [175, 70], [175, 60],[165, 60],[165, 30],[135, 30],[135, 60],[125, 60]], 0)
pygame.draw.polygon(screen, [255, 255, 255], [[135, 60], [165, 60], [165, 55],[135, 55]], 0)
pygame.draw.circle(screen, [200, 0, 0], [165, 55], 5, 0)
pygame.draw.circle(screen, [255, 0, 0], [165, 55], 3, 0)
# müts


pygame.draw.circle(screen, [0, 0, 0], [150, 130], 5, 0)
pygame.draw.circle(screen, [0, 0, 0], [150, 150], 5, 0)
pygame.draw.circle(screen, [0, 0, 0], [150, 170], 5, 0)
# nööbid

pygame.display.update()
# Uuendab akent viimaste muudatustega

while True:
    for event in pygame.event.get():
        # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
            # Kui sündmus võrdub lahkumine
            pygame.quit()
            sys.exit()
            # Lahkub programmist ja peatab kõik mis programmis toimub
