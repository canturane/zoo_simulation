import random
from models.koyun import Koyun
from models.inek import Inek
from models.tavuk import Tavuk
from models.horoz import Horoz
from models.kurt import Kurt
from models.aslan import Aslan
from models.avci import Avci
from utils.constants import ANIMAL_COUNTS
from utils.constants import HUNT_DISTANCES, REPRODUCTION_DISTANCE
import pygame
from visual.visualizer import ciz
from utils.constants import MAP_SIZE

hayvanlar = []

def hayvan_uret():
    # Koyun
    for i in range(ANIMAL_COUNTS["Koyun"] // 2):
        hayvanlar.append(Koyun("Erkek"))
        hayvanlar.append(Koyun("Dişi"))
    
    # İnek
    for i in range(ANIMAL_COUNTS["Inek"] // 2):
        hayvanlar.append(Inek("Erkek"))
        hayvanlar.append(Inek("Dişi"))
    
    # Tavuk
    for _ in range(ANIMAL_COUNTS["Tavuk"]):
        hayvanlar.append(Tavuk("Dişi"))  
    
    # Horoz
    for _ in range(ANIMAL_COUNTS["Horoz"]):
        hayvanlar.append(Horoz("Erkek"))
    
    # Kurt
    for i in range(ANIMAL_COUNTS["Kurt"] // 2):
        hayvanlar.append(Kurt("Erkek"))
        hayvanlar.append(Kurt("Dişi"))
    
    # Aslan
    for i in range(ANIMAL_COUNTS["Aslan"] // 2):
        hayvanlar.append(Aslan("Erkek"))
        hayvanlar.append(Aslan("Dişi"))
    
    # Avcı
    hayvanlar.append(Avci())

def hareket_et():
    for hayvan in hayvanlar:
        if hayvan.canli:
            hayvan.hareket_et()

def sayim_yap():
    sayim = {}
    for h in hayvanlar:
        if h.canli:
            sayim[h.tur] = sayim.get(h.tur, 0) + 1
    return sayim

def avlanma():
    for avci_h in hayvanlar:
        if not avci_h.canli:
            continue
        if avci_h.tur in ["Kurt", "Aslan", "Avci"]:
            for av_h in hayvanlar:
                if not av_h.canli or av_h == avci_h:
                    continue
                mesafe = avci_h.mesafe(av_h)
                if avci_h.tur == "Kurt" and av_h.tur in ["Koyun", "Tavuk", "Horoz"]:
                    if mesafe <= HUNT_DISTANCES["Kurt"]:
                        av_h.canli = False
                elif avci_h.tur == "Aslan" and av_h.tur in ["Koyun", "Inek"]:
                    if mesafe <= HUNT_DISTANCES["Aslan"]:
                        av_h.canli = False
                elif avci_h.tur == "Avci" and av_h.tur != "Avci":
                    if mesafe <= HUNT_DISTANCES["Avci"]:
                        av_h.canli = False

def ureme():
    yeni_hayvanlar = []
    ureyenler = set()

    for i, h1 in enumerate(hayvanlar):
        if not h1.canli or i in ureyenler:
            continue
        for j, h2 in enumerate(hayvanlar[i+1:], start=i+1):
            if not h2.canli or j in ureyenler:
                continue
            if h1.tur == h2.tur and h1.cinsiyet != h2.cinsiyet:
                if h1.mesafe(h2) <= REPRODUCTION_DISTANCE:
                    yeni_cinsiyet = random.choice(["Erkek", "Dişi"])
                    yeni = None

                    if h1.tur == "Koyun":
                        from models.koyun import Koyun
                        yeni = Koyun(yeni_cinsiyet)
                    elif h1.tur == "Inek":
                        from models.inek import Inek
                        yeni = Inek(yeni_cinsiyet)
                    elif h1.tur == "Kurt":
                        from models.kurt import Kurt
                        yeni = Kurt(yeni_cinsiyet)
                    elif h1.tur == "Aslan":
                        from models.aslan import Aslan
                        yeni = Aslan(yeni_cinsiyet)

                    if yeni:
                        yeni.x = random.randint(0, MAP_SIZE)
                        yeni.y = random.randint(0, MAP_SIZE)
                        yeni_hayvanlar.append(yeni)
                        ureyenler.add(i)
                        ureyenler.add(j)
                        break  # aynı hayvan tekrar doğurmasın

    hayvanlar.extend(yeni_hayvanlar)



def sayim_goster(sayim: dict, baslik: str):
    print(f"\n {baslik}")
    print("-" * 30)
    toplam = 0
    for tur, adet in sorted(sayim.items(), key=lambda x: x[0]):
        print(f"{tur:<10}: {adet}")
        toplam += adet
    print(f"{'Toplam':<10}: {toplam}")


def basla():
    pygame.init()
    ekran = pygame.display.set_mode((700, 500))  
    pygame.display.set_caption("Hayvanat Bahçesi Simülasyonu")

    hayvan_uret()
    print("Başlangıç:")
    sayim_goster(sayim_yap(), "Başlangıç Sayımları")

    for step in range(1000):
        pygame.event.pump()
        hareket_et()
        avlanma()
        ureme()
        ciz(hayvanlar, ekran, sayim=sayim_yap(), step=step + 1)
        pygame.time.delay(30)

    sayim_goster(sayim_yap(), "1000 Adım Sonrası Sayımlar")
    pygame.quit()
