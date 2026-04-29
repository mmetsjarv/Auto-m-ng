import pygame
import random

# Mängu algseadistamine
pygame.init()
ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Auto mäng - Metsjärv")

# Värvid ja tekst
valge = (0, 102, 51)
font = pygame.font.SysFont("comicsansms", 24)

# Lisame pildid
taust = pygame.image.load("bg_rally.jpg")
punane_auto_pilt = pygame.image.load("f1_red.png")
sinine_auto_pilt = pygame.image.load("f1_blue.png")

# Muudame piltide suurust
punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, (50, 80))
sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, (50, 80))

# Autode positsioonid
punane_x = ekraani_laius // 2 - 25
punane_y = ekraani_korgus - 100

# Siniste autode list
sinised_autod = []
for i in range(3):
    x = random.randint(90, 600) # Tee vahemik
    y = random.randint(-500, -100)
    kiirus = random.randint(3, 7)
    sinised_autod.append([x, y, kiirus])

skoor = 0
kell = pygame.time.Clock()
mang_kaib = True

# Mängu põhitsükkel
while mang_kaib:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            mang_kaib = False

    # Lisame tausta
    ekraan.blit(taust, (0, 0))

    # Siniste autode liikumine ja skoori lugemine
    for auto in sinised_autod:
        # Liigutame autot alla
        auto[1] += auto[2]

        # Kui auto jõuab ekraani alla välja
        if auto[1] > ekraani_korgus:
            auto[1] = random.randint(-200, -50) # Uus algus kõrgemal
            auto[0] = random.randint(150, 450)  # Uus juhuslik tee koht
            skoor += 1  # Lisame punkti

        # Joonistame sinise auto
        ekraan.blit(sinine_auto_pilt, (auto[0], auto[1]))

    # Joonistame punase auto (püsib keskel all)
    ekraan.blit(punane_auto_pilt, (punane_x, punane_y))

    # Skoori kuvamine (teisendamine tekstiks)
    skoori_tekst = font.render("Skoor: " + str(skoor), True, valge)
    ekraan.blit(skoori_tekst, (10, 10))

    # Ekraani uuendamine
    pygame.display.flip()
    kell.tick(60) # 60 kaadrit sekundis

pygame.quit()
