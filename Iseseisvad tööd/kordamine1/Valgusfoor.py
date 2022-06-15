import pygame
# impordib mooduli pygame
import sys
# impordib mooduli sys

while True:
    # Kui True == True, siis:
    screen = pygame.display.set_mode([300, 300])
    # loob akna suurusega 300 x 300 pikslit
    pygame.display.set_caption("Valgusfoor")
    # paneb akna nimeks "Valgusfoor"
    screen.fill([0, 0, 0])
    # muudab tausta pildi mustaks

    pygame.draw.rect(screen, [150, 150, 150], [100, 15, 100, 270], 2)
    # pygame.draw.rect(screen, värv, [x, y, w, h], joone_paksus)
    pygame.draw.circle(screen,[255, 0, 0], [150,65],40, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.draw.circle(screen, [255, 255, 0], [150, 150], 40, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.draw.circle(screen, [0, 255, 0], [150, 235], 40, 0)
    # pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
    pygame.display.update()
    # Uuendab akent viimaste muudatustega
    for event in pygame.event.get():
        # otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
            # kui kasutaja klõpsab rakenudse kinni, siis:
            pygame.quit(); sys.exit();
            # pygame sulgeb akna ja süsteem peatab protsessi

