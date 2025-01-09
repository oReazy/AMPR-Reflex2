"""

AMPR — игровой проект, где игроки развивают персонажей и добиваются поставленных целей.

"""

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

from .pages.base import index, welcome, excursion, help, inventory, map
from .pages.locations import cityHall, licensingCenter
from .states.base import index, welcome, excursion, help, inventory, map
from .states.locations import cityHall, licensingCenter

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

app = rx.App()