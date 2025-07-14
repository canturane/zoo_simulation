import pygame
from utils.constants import MAP_SIZE

RENKLER = {
    "Koyun": (255, 255, 255),
    "Inek": (150, 75, 0),
    "Tavuk": (255, 255, 0),
    "Horoz": (255, 165, 0),
    "Kurt": (128, 128, 128),
    "Aslan": (255, 215, 0),
    "Avci": (255, 0, 0),
}

HARITA_BOYUTU = 500
BILGI_PANELI_GENISLIK = 200
ORAN = HARITA_BOYUTU / MAP_SIZE
FONT = None

def ciz(hayvanlar, ekran, sayim=None, step=None):
    ekran.fill((0, 100, 0), pygame.Rect(0, 0, HARITA_BOYUTU, HARITA_BOYUTU))  # Harita
    ekran.fill((0, 0, 0), pygame.Rect(HARITA_BOYUTU, 0, BILGI_PANELI_GENISLIK, HARITA_BOYUTU))  # Bilgi paneli

    # Hayvanları çiz
    for h in hayvanlar:
        if not h.canli:
            continue
        x = int(h.x * ORAN)
        y = int(h.y * ORAN)
        x = max(5, min(x, HARITA_BOYUTU - 5))
        y = max(5, min(y, HARITA_BOYUTU - 5))
        renk = RENKLER.get(h.tur, (0, 0, 0))
        pygame.draw.circle(ekran, renk, (x, y), 5)

    # Bilgi paneli: tür renkleri + sayılar
    if sayim:
        global FONT
        if not FONT:
            FONT = pygame.font.SysFont(None, 20)
        text_x = HARITA_BOYUTU + 30
        text_y = 10
        for tur, adet in sorted(sayim.items()):
            renk = RENKLER.get(tur, (255, 255, 255))
            # Renkli daire sembolü
            pygame.draw.circle(ekran, renk, (HARITA_BOYUTU + 15, text_y + 8), 6)
            # Yazı
            text = FONT.render(f"{tur}: {adet}", True, (255, 255, 255))
            ekran.blit(text, (text_x, text_y))
            text_y += 22

    # Step numarası
    if step is not None:
        step_text = FONT.render(f"Adım: {step}", True, (255, 255, 255))
        ekran.blit(step_text, (HARITA_BOYUTU + 10, HARITA_BOYUTU - 30))

    pygame.display.flip()
