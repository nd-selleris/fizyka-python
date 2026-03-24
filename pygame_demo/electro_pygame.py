import sys 
import pygame 

pygame.init()

szerokosc = 900 #peremennaya
wysokosc = 600
okno = pygame.display.set_mode((szerokosc,wysokosc)) 
pygame.display.set_caption('elektro')

zegar=pygame.time.Clock()

green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
big_font = pygame.font.SysFont(None,48)
small_font = pygame.font.SysFont(None,32)

state="menu"
switch=False 
battery=100

start_button=pygame.Rect(340,220,220,60)
exit_button=pygame.Rect(340,310,220,60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    okno.fill(white)
    title=big_font.render("Main menu",True,black)
    okno.blit(title,(360,120))
    
    pygame.draw.rect(okno,green,start_button)    
    pygame.draw.rect(okno,red,exit_button)

    start_text=small_font.render("Start",True,black)
    exit_text=small_font.render("Exit",True,black)

    okno.blit(start_text,(360,240))
    okno.blit(exit_text,(360,330))








    pygame.display.flip()
    zegar.tick(60)

