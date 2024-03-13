#Pytong Ośmiokąt Figura 4
#kuba lis, sześciokat, figura 2
import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("zadanie idk")
BLACK = (0,0,0)
CZERWONY = (255, 0, 0)
run = True
while run:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   run = False	
 pygame.draw.rect(window, CZERWONY , (100, 100, 400, 50))
 poprzeczka =  pygame.Surface((500,50))
 poprzeczka.set_colorkey(BLACK)
 poprzeczka.fill(CZERWONY)
 rect = poprzeczka.get_rect()
 poprzeczka = pygame.transform.rotate(poprzeczka, 45)
 rect = poprzeczka.get_rect()
 rect.center = (300,300)
 window.blit(poprzeczka,rect)
 pygame.display.flip()
 pygame.transform.rotate(window,45)
 pygame.draw.rect(window, CZERWONY , (100, 450, 400, 50))
 #pygame.draw.rect(window, CZERWONY , (100, 300, 400, 50))
 pygame.display.update()
