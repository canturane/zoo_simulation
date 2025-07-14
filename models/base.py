import random
from utils.constants import MAP_SIZE

class Hayvan:
    def __init__(self, tur, hareket_miktari, cinsiyet=None):
        self.tur = tur
        self.x = random.randint(0, MAP_SIZE)
        self.y = random.randint(0, MAP_SIZE)
        self.hareket_miktari = hareket_miktari
        self.cinsiyet = cinsiyet if cinsiyet else random.choice(["Erkek", "Dişi"])
        self.canli = True

    def hareket_et(self):
        dx = random.randint(-self.hareket_miktari, self.hareket_miktari)
        dy = random.randint(-self.hareket_miktari, self.hareket_miktari)
        self.x = max(0, min(MAP_SIZE, self.x + dx))
        self.y = max(0, min(MAP_SIZE, self.y + dy))

    def konum(self):
        return (self.x, self.y)

    def mesafe(self, diger):
        return ((self.x - diger.x)**2 + (self.y - diger.y)**2)**0.5
