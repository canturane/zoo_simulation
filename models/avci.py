from models.base import Hayvan
from utils.constants import MOVEMENT_DISTANCES

class Avci(Hayvan):
    def __init__(self):
        super().__init__("Avci", MOVEMENT_DISTANCES["Avci"], "Erkek")
