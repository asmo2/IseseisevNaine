import pygame

pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("yl2_pilt")

main = True

while main == True:
    screen.fill([255, 255, 255])
    #täidab valge värviga


    bg = pygame.image.load("yl2_pilt.jpg")
    screen.blit(bg, [0, 0])
    bg = pygame.image.load("yl2_seller.jpg")
    bg = pygame.transform.scale(bg, [253, 304])
    screen.blit(bg, [104, 159])
    bg = pygame.image.load("yl2_chat.jpg")
    bg = pygame.transform.scale(bg, [257, 202])
    screen.blit(bg, [246, 66])
    #taustapilt, asukoht, müüja pilt, müüja suurus ja laius, müüja asukoht, teksti lahtri pilt, teksti lahtri suurus ja laius, teksti lahti asukoht

    font = pygame.font.Font(None, 30)
    text = font.render("Tere, olen Aadu Kaup", True, [255, 255, 255])
    screen.blit(text, [270, 140])
    #teksti font, tekst ja teksti värv, teksti asukoht

    pygame.display.flip()
    for event in pygame.event.get():
    # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
        # Kui sündmus võrdub lahkumine
            pygame.quit()
            quit()
            # Lahkub programmist ja peatab kõik mis programmis toimub