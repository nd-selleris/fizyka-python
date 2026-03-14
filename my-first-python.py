print('Projekt: Ruch samochodu')
print('Obliczam droge i predkosc')

droga=100
czas=2
predkosc=0

def oblicz_predkosc_sriednia(droga,czas):
    return droga / czas

predkosc=oblicz_predkosc_sriednia(droga,czas)





if predkosc > 50:
    print('Samochod jedzie szybko')
else: print('Samochod jedzie wolno')



sekunda=1
sekund_w_godzinie=3600


def odleglosc_za_czas_w_sekundach(predkosc,sekund_w_godzinie,sekunda):
    odleglosc=(predkosc/sekund_w_godzinie)*sekunda
    odleglosc_rounded=round(odleglosc,2)
    return odleglosc_rounded


while sekunda<=5:
    print(sekunda,odleglosc_za_czas_w_sekundach(predkosc,sekund_w_godzinie,sekunda),'km')
    sekunda=sekunda + 1
 





