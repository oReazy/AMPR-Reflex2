"""

[ PAGES ]

Главная страница проекта

"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
import json, ast, datetime, time

from rxconfig import config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

import AMPR.components.header as header
import AMPR.components.registration as regButton
import AMPR.components.auth as authButton

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

@rx.page(route="/", title="«AMPR» — Главная страница", on_load=LS.onLoadLite)
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.center(rx.image('/images/logo/american-flag.webp', padding_top='200px', width='100px')),
                rx.heading('American Project', padding_top='8px', align='center', size='9'),
                rx.text(f'игровой проект нового поколения', align='center', padding_top='8px', padding_bottom='20px', weight="medium", size='4'),
                rx.cond(LS.HASH == '0',
                        rx.flex(
                            authButton.index('4'),
                            regButton.index('4'),
                            direction='row',
                            spacing='2',
                            justify='center',
                        ),
                        rx.flex(
                            rx.button(rx.icon('backpack', size=23), 'Инвентарь', size='4', on_click=rx.redirect('/inventory')),
                            rx.button(rx.icon('map', size=23), 'Карта', size='4', on_click=rx.redirect('/map')),
                            direction='row',
                            spacing='2',
                            justify='center',
                        )),
                rx.text('Узнать подробнее 🔽', align='center', padding_top='330px', padding_bottom='8px'),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('building-2', size=25, color=rx.color("blue", 9)),
                            rx.heading('Город возможностей', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Перед вами открывается целый город и окрестности возможностей. Как эти возможности использовать — дело ваше'),
                        width='100%'
                    ),
                    rx.card(
                        rx.flex(
                            rx.icon('pickaxe', size=25, color=rx.color("blue", 9)),
                            rx.heading('Работы и подработки', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Статьте богатым через работы и подработки. Это самый начальный этап в игре, через него проходят все игроки'),
                        width='100%'
                    ),
                    rx.card(
                        rx.flex(
                            rx.icon('car', size=25, color=rx.color("blue", 9)),
                            rx.heading('Траспорт', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Накопив небольшое состояние, вы можете себе купить транспортное средство для более быстрого передвижения'),
                        width='100%'
                    ),
                    spacing='2',
                    direction='row'
                ),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('laugh', size=25, color=rx.color("blue", 9)),
                            rx.heading('Мероприятия', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Каждый день для наших игроков ждут мероприятия как серверные, так и от администраторов'),
                        width='100%'
                    ),
                    rx.card(
                        rx.flex(
                            rx.icon('badge-check', size=25, color=rx.color("blue", 9)),
                            rx.heading('Обновления', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Каждый месяц на проекте выходят обновления, успевайте следить за новинками!'),
                        width='100%'
                    ),
                    rx.card(
                        rx.flex(
                            rx.icon('hotel', size=25, color=rx.color("blue", 9)),
                            rx.heading('Недвижимость', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('В игре предствлено безчисленное множество недвижимости. Купите себе огромный особняк и огроменный гараж'),
                        width='100%'
                    ),
                    spacing='2',
                    direction='row',
                    padding_top='8px'
                ),
                size='4'
            ),
            rx.center(
                rx.spinner(),
                height="100vh",  # Высота экрана
            )
        ),
        size='4'
    )

@rx.page(route="/we-be-right-back", title="«AMPR» — Мы скоро вернемся")
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                rx.center(rx.image(src='/images/logo/ampr.png', margin_top='350px', align='center'),
                          rx.spinner(size='2', margin_top='30px'),
                          direction='column',
                          ),
                size='4'
            ),
            rx.center(
                rx.spinner(),
                height="100vh",  # Высота экрана
            )
        ),
        size='4'
    )