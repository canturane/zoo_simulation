from models.base import Hayvan
from utils.constants import MOVEMENT_DISTANCES

class Inek(Hayvan):
    def __init__(self, cinsiyet=None):
        super().__init__("Inek", MOVEMENT_DISTANCES["Inek"], cinsiyet)
