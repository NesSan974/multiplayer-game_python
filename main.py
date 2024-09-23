import pygame 
  
pygame.init() 

canvas = pygame.display.set_mode((1920, 1080)) 

pygame.display.set_caption("My Game") 
exit = False
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 
