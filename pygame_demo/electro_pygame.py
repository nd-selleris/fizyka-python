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
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse click:", event.pos)
            mouse_pos=event.pos

            if start_button.collidepoint(mouse_pos):
                print("Start")
                state="simulation"
            if exit_button.collidepoint(mouse_pos):
                print("Exit")
                pygame.quit()
                sys.exit()
 
    if state=="menu":
        okno.fill(white)
        title=big_font.render("Main menu",True,black)
        okno.blit(title,(360,120))
        
        pygame.draw.rect(okno,green,start_button)    
        pygame.draw.rect(okno,red,exit_button)

        start_text=small_font.render("Start",True,black)
        exit_text=small_font.render("Exit",True,black)

        okno.blit(start_text,(360,240))
        okno.blit(exit_text,(360,330))
    elif state=="simulation":


        okno.fill(white)
        sim_text=big_font.render("Simulation screen",True,black)
        okno.blit(sim_text,( 305,25))







    pygame.display.flip()
    zegar.tick(60)

