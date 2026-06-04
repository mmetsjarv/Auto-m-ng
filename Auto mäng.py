import pygame
import random

pygame.init()  # Mängu algseadistamine

# Määrame mänguakna mõõtmed
ekraani_laius = 640
ekraani_korgus = 480

# Loome mänguakna
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Auto mäng - Metsjärv") # Paneme aknale nime

# Tekst värvid ja font
tekst = (0, 102, 51)
font = pygame.font.SysFont("Comic Sans MS", 24, bold=True)

# Lisame mängu pildid
taust = pygame.image.load("bg_rally.jpg")
punane_auto_pilt = pygame.image.load("f1_red.png")
sinine_auto_pilt = pygame.image.load("f1_blue.png")

# Muudame piltide suurust
punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, (50, 80))
sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, (50, 80))

# Punase auto positsioon
punane_x = ekraani_laius // 2 - 25
punane_y = ekraani_korgus - 100

rajad = [180, 300, 420]  # Rajad, millel sinised autod võivad liikuda

# Siniste autode positsioonid/rajad (igaüks oma rajal)
sinised_autod = [
    [rajad[0], -100, 3],
    [rajad[1], -300, 5],
    [rajad[2], -500, 7]
]

skoor = 0  # Algne skoor
kell = pygame.time.Clock()  # Kell kaadrisageduse juhtimiseks
mang_kaib = True  # Mängu töösoleku muutuja

# Mängu põhitsükkel
while mang_kaib:

    # Sündmuste kontrollimine
    for syndmus in pygame.event.get():
        if syndmus.type == pygame.QUIT:
            mang_kaib = False

    ekraan.blit(taust, (0, 0))  # Lisame tausta
    for auto in sinised_autod:  # Käime kõik sinised autod läbi
        auto[1] += auto[2]  # Liigutame autot alla

        if auto[1] > ekraani_korgus:  # Kui auto jõuab ekraani alla välja
            auto[1] = random.randint(-500, -100)  # Viime auto uuesti ekraani kohale
            vabad_rajad = rajad.copy()  # Vali rada, kus pole teist autot liiga lähedal

            # Kontrollime, kas mõni teine auto on samal rajal liiga lähedal
            for teine_auto in sinised_autod:
                if teine_auto != auto and teine_auto[0] in vabad_rajad:
                    if teine_auto[1] < 150:
                        vabad_rajad.remove(teine_auto[0])

            # Kui leidub vabu radu, valime neist ühe
            if vabad_rajad:
                auto[0] = random.choice(vabad_rajad)
            else:
                auto[0] = random.choice(rajad)  # Kui kõik rajad on hõivatud, valime suvalise raja

            skoor += 1  # Suurendame skoori iga möödunud auto eest

        ekraan.blit(sinine_auto_pilt, (auto[0], auto[1]))  # Joonistame sinise auto

    ekraan.blit(punane_auto_pilt, (punane_x, punane_y))  # Joonistame punase auto (püsib keskel all)
    skoori_tekst = font.render("Skoor: " + str(skoor), True, tekst)  # Skoori kuvamine (teisendamine tekstiks)
    ekraan.blit(skoori_tekst, (10, 10))  # Kuvame skoori asukoht
    pygame.display.flip()  # Ekraani uuendamine
    kell.tick(60)  # Piirame mängu kiiruse 60 kaadrini sekundis

pygame.quit()  # Sulgeme pygame'i korrektselt
