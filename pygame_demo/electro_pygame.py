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
yellow=(255,255,0)
purple=(255,0,255)
cyan=(0,255,255)
grey=(211,211,211)

big_font = pygame.font.SysFont(None,48)
small_font = pygame.font.SysFont(None,32)

state="menu"
switch=False 
battery=100

start_button=pygame.Rect(340,220,220,60)
exit_button=pygame.Rect(340,310,220,60)
back_button=pygame.Rect(0,0,75,30)
switch_button=pygame.Rect(250,300,70,70)
battery=pygame.Rect(500,300, 70,70)
light=pygame.Rect(375,175,70,70)

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

            if back_button.collidepoint(mouse_pos):
                state="menu"

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

        pygame.draw.rect(okno,black,back_button)
        back_text=small_font.render("Back",True,white)
        okno.blit(back_text,(0,0))


        pygame.draw.ellipse(okno,purple,battery)
        pygame.draw.rect(okno,cyan,switch_button)
        pygame.draw.rect(okno,grey,light)

        battery_text=small_font.render("Battery",True,black)
        light_text=small_font.render("Light",True,black)
        switch_text=small_font.render("Switch",True,black)
        
        okno.blit(battery_text,(500,300))   
        okno.blit(light_text,(375,175))
        okno.blit(switch_text,(250,300))

    count=100
    counting=False


    if event.type == pygame.MOUSEBUTTONDOWN:
        switch_button.collidepoint(event.pos)
        light=(yellow)
        counting=True







    pygame.display.flip()
    zegar.tick(60)

