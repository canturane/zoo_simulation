from models.base import Hayvan
from utils.constants import MOVEMENT_DISTANCES

class Kurt(Hayvan):
    def __init__(self, cinsiyet=None):
        super().__init__("Kurt", MOVEMENT_DISTANCES["Kurt"], cinsiyet)
