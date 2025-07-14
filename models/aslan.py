from models.base import Hayvan
from utils.constants import MOVEMENT_DISTANCES

class Aslan(Hayvan):
    def __init__(self, cinsiyet=None):
        super().__init__("Aslan", MOVEMENT_DISTANCES["Aslan"], cinsiyet)
