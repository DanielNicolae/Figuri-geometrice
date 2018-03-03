import pygame

pygame.init()                                         # initializare

alb=(255,255,255)                                     # culorile iau valori intre 0 si 255 pentru cele trei numere naturale
negru=(0,0,0)                                         # culoare=(0...255, 0...255, 0...255)
rosu=(255,0,0)                                        #           rosu     verde   albastru
verde=(0,255,0)
albastru=(0,0,255) 
galben=(255,255,0)                                    # prin combinarea culorilor primare se poate obtine orice nuanta de culoare

ecran=pygame.display.set_mode((800,600))              # defineste rezolutia ecranului
ecran.fill(negru)                                     # seteaza culoarea fundalului

pixelRosu=pygame.PixelArray(ecran)                        # specifica locul unde se afiseaza pixelul
pixelRosu[400][300]=rosu                                  # specifica pozitia [x][y] a pixelului pe ecran si culoarea acestuia
pygame.draw.line(ecran, verde, (100,100),(200,250),4) # Afiseaza o linie de culoare verde pe ecran,
                                                      # cu grosimea de 4 pixeli; linie care are primul capat la (100,100) si cel de-al doilea capat la (200,250)
pygame.draw.rect(ecran, albastru, (400,400,60,70))    # Afiseaza pe ecran un dreptunghi de culoare albastra, ce are varful din stanga sus la coordonatele (400,400),
                                                      # latimea de 60 si inaltimea de 70
cerc=pygame.draw.circle(ecran, galben, (250,140), 50)      # Afiseaza pe ecran un cerc de culoare galbena, cu centrul in punctul de coordonate (150,140) si de raza 50
pygame.draw.polygon(ecran, alb, ((25,25),(50,25),(37,10))) # Afiseaza pe ecran un triunghi de culoare alba, ce are coordonatele celor trei puncte definite de
                                                           #((x,y),(x,y),(x,y))
pygame.draw.polygon(ecran, rosu, ((270,350),(300,390),(360,390),(390,350),(330,310))) # Afiseaza un pentagon pe ecran,
                                                                                      # ce are coordonatele celor cinci puncte ((x,y),(x,y),(x,y),(x,y),(x,y))

                                    
while True:                                       # start bucla
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()                                # inchidere bucla


    pygame.display.update()                               # updateaza ecranul

