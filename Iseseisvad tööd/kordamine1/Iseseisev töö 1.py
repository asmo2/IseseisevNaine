# import pygame
# pygame.init()
#
# screen=pygame.display.set_mode([640,480])
# pygame.display.set_caption("My Screen")


import pygame
pygame.init()

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)
pygame.display.set_caption("My Screen")


import pygame
pygame.init()
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("My Screen")
screen.fill([204, 255, 255])
pygame.display.flip()




import pygame
pygame.init()

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("My Screen")
screen.fill([204, 255, 255])

pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2



pygame.display.flip()
pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2)
pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1)
pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)
pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2)
pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1)



