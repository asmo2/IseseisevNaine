import pygame

pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("yl2_pilt")

main = True

while main == True:
    screen.fill([255, 255, 255])

    bg = pygame.image.load("yl2_pilt.jpg")
    screen.blit(bg, [0, 0])
    mees = pygame.image.load("yl2_seller.jpg")
    mees = pygame.transform.scale(mees, [253, 304])
    screen.blit(mees, [104, 159])
    chat = pygame.image.load("yl2_chat.jpg")
    chat = pygame.transform.scale(chat, [257, 202])
    screen.blit(chat, [246, 66])

    font = pygame.font.Font(None, 30)
    text = font.render("Tere, olen Aadu Kaup", True, [255, 255, 255])
    screen.blit(text, [270, 140])

    logo = pygame.image.load("VIKK logo.png")
    logo = pygame.transform.scale(logo, [300, 40])
    screen.blit(logo, [0, 0])

    kook = pygame.image.load("Cake.png")
    kook = pygame.transform.scale(kook, [100, 100])
    screen.blit(kook, [450, 190])

    sword = pygame.image.load("Mook.png")
    sword = pygame.transform.scale(sword, [100, 100])
    screen.blit(sword, [540, 190])

    pygame.display.flip()
    for event in pygame.event.get():
    # Otsib kas on mingi "Event" toimunud
        if event.type == pygame.QUIT:
        # Kui sündmus võrdub lahkumine
            pygame.quit()
            quit()
            # Lahkub programmist ja peatab kõik mis programmis toimub