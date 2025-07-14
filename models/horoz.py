from models.base import Hayvan
from utils.constants import MOVEMENT_DISTANCES

class Horoz(Hayvan):
    def __init__(self, cinsiyet="Erkek"):
        super().__init__("Horoz", MOVEMENT_DISTANCES["Horoz"], cinsiyet)
