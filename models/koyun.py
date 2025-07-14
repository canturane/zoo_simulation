from models.base import Hayvan
from utils.constants import MOVEMENT_DISTANCES

class Koyun(Hayvan):
    def __init__(self, cinsiyet=None):
        super().__init__("Koyun", MOVEMENT_DISTANCES["Koyun"], cinsiyet)
