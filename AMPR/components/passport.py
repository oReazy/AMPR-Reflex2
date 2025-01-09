"""

[ COMPONENTS ]

Компонент верхней части проекта (шапка)

"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
import json, ast, datetime, time

import hashlib
from rxconfig import config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS
from AMPR.states.base.inventory import State as StateInv

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class State(LS):
    pass

def index():
    return rx.dialog.root(
    rx.tooltip(rx.dialog.trigger(rx.button(rx.icon('book', size=25), width='50px', height='50px', variant='soft', color_scheme='blue')), content='Паспорт', side='bottom', delay_duration=1),
    rx.dialog.content(
        rx.flex(
            rx.dialog.title("Паспорт"),
            rx.divider(margin_top='-12px'),
            rx.flex(
                rx.avatar(src=rx.get_upload_url(f'{State.USER[18]}'), width='100px', height='100px'),
                rx.flex(
                    rx.text(f'{StateInv.inventoryPassportMax[2]} {StateInv.inventoryPassportMax[3]}', weight='bold', size='5'),
                    rx.cond(
                        State.USER[19] == 1,
                        rx.text(f'Пол: Мужчина'),
                        rx.text(f'Пол: Женщина'),
                    ),
                    rx.text(f'Возраст: {State.USER[20]} лет'),
                    spacing='1',
                    direction='column'
                ),
                spacing='2',
                direction='row'
            ),
            rx.divider(),
            rx.flex(
                rx.cond(StateInv.inventoryLicenses[0] == 0,
                        rx.text(f'🚗 Лицензия на автомобили » ❌ Отсутствуют'),
                        rx.text(f'🚗 Лицензия на автомобили » ✅ Имеется')),
                rx.cond(StateInv.inventoryLicenses[1] == 0,
                        rx.text(f'🏍 Лицензия на мотоциклы » ❌ Отсутствуют'),
                        rx.text(f'🏍 Лицензия на мотоциклы » ✅ Имеется')),
                rx.cond(StateInv.inventoryLicenses[2] == 0,
                        rx.text(f'🚚 Лицензия на грузовой транспорт » ❌ Отсутствуют'),
                        rx.text(f'🚚 Лицензия на грузовой транспорт » ✅ Имеется')),
                rx.cond(StateInv.inventoryLicenses[3] == 0,
                        rx.text(f'🔫 Лицензия на оружие » ❌ Отсутствуют'),
                        rx.text(f'🔫 Лицензия на оружие » ✅ Имеется')),
                rx.cond(StateInv.inventoryLicenses[4] == 0,
                        rx.text(f'🐠 Лицензия на ловлю рыбы » ❌ Отсутствуют'),
                        rx.text(f'🐠 Лицензия на ловлю рыбы » ✅ Имеется')),
                rx.cond(StateInv.inventoryLicenses[5] == 0,
                        rx.text(f'🛩 Лицензия на воздушный транспорт » ❌ Отсутствуют'),
                        rx.text(f'🛩 Лицензия на воздушный транспорт » ✅ Имеется')),
                rx.cond(StateInv.inventoryLicenses[6] == 0,
                        rx.text(f'🛥 Лицензия на водный транспорт » ❌ Отсутствуют'),
                        rx.text(f'🛥 Лицензия на водный транспорт » ✅ Имеется')),
                rx.cond(StateInv.inventoryLicenses[7] == 0,
                        rx.text(f'🐅 Лицензия на охоту » ❌ Отсутствуют'),
                        rx.text(f'🐅 Лицензия на охоту » ✅ Имеется')),
                direction='column',
            ),
            rx.divider(),
            rx.text(f'РАЗРЕШЕНО ПРИБЫВАНИЕ В СТРАНЕ', color_scheme='green', size='3', weight='bold'),
            direction='column',
            spacing='2',
        ),
        width='550px',
        size='2'
    ),
)