from models.base import Hayvan
from utils.constants import MOVEMENT_DISTANCES

class Tavuk(Hayvan):
    def __init__(self, cinsiyet="Dişi"):
        super().__init__("Tavuk", MOVEMENT_DISTANCES["Tavuk"], cinsiyet)
