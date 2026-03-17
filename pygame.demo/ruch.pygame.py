import pygame
import sys

pygame.init()

szerokosc = 900
wysokosc = 450
okno = pygame.display.set_mode((szerokosc,wysokosc))
pygame.display.set_caption('Ruch jednostajny')

czcionka = pygame.font.SysFont(None,32)
zegar=pygame.time.clock()

x_start=50
y_samochodu=260
x_samochodu=x_start

predkosc=5
czas=0
klatki=0
fps=60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    klatki+=1
    if klatki >= fps:
        klatki = 0
        czas += 1
        droga=predkosc*czas
        x_samochodu = x_start + droga


    if x_samochodu > szerokosc - 60:
        czas = 0
        klatki = 0
        x_samochodu=x_start

    okno.fill((235,245,255))
    pygame.draw.rect(okno, (100,100,100), (0,300, szerokosc,90))
    pygame.draw.rect(okno, (220,50,50),(x_samochodu,y_samochodu, 60, 30))
    pygame.draw.circle(okno,(0,0,0),(x_samochodu+15,y_samochodu+30),8)
    pygame.draw.circle(okno,(0,0,0),(x_samochodu+45,y_samochodu+30),8)

    tekst1=czcionka.render(f'Predkosc: {predkosc} j/s',True,(0,0,0))
    tekst2=czcionka.render(f'Czas: {czas} s',True,(0,0,0))
    tekst3=czcionka.render(f'Droga: {predkosc*czas} j',True,(0,0,0))

    okno.blit(tekst1,(30,30))
    okno.blit(tekst2,(30,70))
    okno.blit(tekst3,(30,110))

    pygame.display.flip()
    zegar.tick(fps)


