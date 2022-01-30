from interface_.seed import Seed
from interface_.name import Name
from interface_.level import Level
from interface_.shop_button import ShopButton


class Interface:
    def __init__(self):
        self.level = Level()
        self.shopbutton = ShopButton()
        self.name = Name()
        self.seed = Seed()

    def draw(self, screen):
        self.shop_button.draw(screen)
        self.name.draw(screen)
        self.seed.draw(screen)
        self.level.draw(screen)
