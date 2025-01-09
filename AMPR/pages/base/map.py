"""

[ PAGES ]

Страница карты

"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx

from rxconfig import config
import json
from typing import Tuple

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

import AMPR.components.header as header
from AMPR.states.base.map import State

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

style = {"text-decoration": "none !important",  # Убираем подчёркивание
         "color": "inherit !important",  # Цвет наследуется от родителя
         "cursor": "hover",  # Убираем указатель на ссылке
        }
hover = {"color": "inherit !important",  # Цвет не меняется при наведении
        "text-decoration": "none !important",  # Подчёркивание не появляется
        "background-color": "transparent !important",  # Чтобы исключить изменения фона
        }


@rx.page(route="/map", title="«AMPR» — Карта", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Важные места', size='4', weight='bold', color='black'),
                                rx.icon('castle', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                        ),
                        href='/map/important-places',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Развлечения', size='4', weight='bold', color='black'),
                                rx.icon('laugh', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='50%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Магазины', size='4', weight='bold', color='black'),
                                rx.icon('store', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='50%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Банки', size='4', weight='bold', color='black'),
                                rx.icon('landmark', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                        ),
                        href='/map/banks',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    direction='row',
                    spacing='2',
                ),
                rx.flex(
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Подработки', size='4', weight='bold', color='black'),
                                rx.icon('pickaxe', margin_top='20px', margin_bottom='-14px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                        ),
                        href='/map/underworking',
                        width='50%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Организации', size='4', weight='bold', color='black'),
                                rx.icon('briefcase-business', margin_top='20px', margin_bottom='-16px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Автосалоны', size='4', weight='bold', color='black'),
                                rx.icon('car', margin_top='20px', margin_bottom='-17.3px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='50%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Образование', size='4', weight='bold', color='black'),
                                rx.icon('graduation-cap', margin_top='20px', margin_bottom='-17.7px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    direction='row',
                    spacing='2',
                    padding_top='8px'
                ),
                rx.flex(
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Риэлторские агентства', size='4', weight='bold', color='black'),
                                rx.icon('building', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Аэропорты', size='4', weight='bold', color='black'),
                                rx.icon('plane', margin_top='20px', margin_bottom='-14px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='50%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Рестораны', size='4', weight='bold', color='black'),
                                rx.icon('utensils', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='50%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Прочее', size='4', weight='bold', color='black'),
                                rx.icon('layers', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    direction='row',
                    spacing='2',
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

@rx.page(route="/map/important-places", title="«AMPR» — Важные места", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Назад', size='4', weight='bold', color='black'),
                                rx.icon('circle-chevron-left', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='180px',
                        ),
                        href='/map',
                        width='180px',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Мэрия', size='4', weight='bold', color='black'),
                                rx.icon('university', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                        ),
                        href='/places/cityHall',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Центр лицензирования', size='4', weight='bold', color='black'),
                                rx.icon('notebook-tabs', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                        ),
                        href='/places/licensing-center',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    direction='row',
                    spacing='2',
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

@rx.page(route="/map/banks", title="«AMPR» — Банки", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('Назад', size='4', weight='bold', color='black'),
                                rx.icon('circle-chevron-left', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='180px',
                        ),
                        href='/map',
                        width='180px',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('BNG Bank', size='4', weight='bold', color='black'),
                                rx.icon('landmark', margin_top='22px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('NBank', size='4', weight='bold', color='black'),
                                rx.icon('landmark', margin_top='22px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.text('NEO Bank', size='4', weight='bold', color='black'),
                                rx.icon('landmark', margin_top='22px', margin_bottom='-12.6px', size=40, color='black'),
                                direction='column'
                            ),
                            align='center',
                            width='100%',
                            background='tomato'
                        ),
                        href='/',
                        width='100%',
                        style=style,
                        _hover=hover
                    ),
                    direction='row',
                    spacing='2',
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

@rx.page(route="/map/underworking", title="«AMPR» — Подработка", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.flex(
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Назад', size='4', weight='bold', color='black'),
                                    rx.icon('circle-chevron-left', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='180px',
                            ),
                            href='/map',
                            width='180px',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Ферма', size='4', weight='bold', color='black'),
                                    rx.icon('tractor', margin_top='24px', margin_bottom='-17px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Грузчик', size='4', weight='bold', color='black'),
                                    rx.icon('package', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Работник на заводе', size='4', weight='bold', color='black'),
                                    rx.icon('hammer', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        direction='row',
                        spacing='2',
                    ),
                    rx.flex(
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Доставщик', size='4', weight='bold', color='black'),
                                    rx.icon('truck', margin_top='24px', margin_bottom='-17px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Сборщик автомобилей', size='4', weight='bold', color='black'),
                                    rx.icon('car', margin_top='25px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Водитель автобуса', size='4', weight='bold', color='black'),
                                    rx.icon('bus', margin_top='23.5px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Таксист', size='4', weight='bold', color='black'),
                                    rx.icon('car-taxi-front', margin_top='24px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        direction='row',
                        spacing='2',
                    ),
                    rx.flex(
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Инкассатор', size='4', weight='bold', color='black'),
                                    rx.icon('landmark', margin_top='20px', margin_bottom='-17px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Пожарник', size='4', weight='bold', color='black'),
                                    rx.icon('fire-extinguisher', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Пилот', size='4', weight='bold', color='black'),
                                    rx.icon('plane', margin_top='22px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Механик', size='4', weight='bold', color='black'),
                                    rx.icon('wrench', margin_top='22px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        direction='row',
                        spacing='2',
                    ),
                    rx.flex(
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Машинист электропоезда', size='4', weight='bold', color='black'),
                                    rx.icon('train-front', margin_top='20px', margin_bottom='-17px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Дорожная служба', size='4', weight='bold', color='black'),
                                    rx.icon('traffic-cone', margin_top='20px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        rx.link(
                            rx.card(
                                rx.flex(
                                    rx.text('Продавец хот-догов', size='4', weight='bold', color='black'),
                                    rx.icon('chef-hat', margin_top='22px', margin_bottom='-12.6px', size=40, color='black'),
                                    direction='column'
                                ),
                                align='center',
                                width='100%',
                                background='tomato',
                                height='97.41px'
                            ),
                            href='/',
                            width='100%',
                            style=style,
                            _hover=hover
                        ),
                        direction='row',
                        spacing='2',
                    ),
                    direction='column',
                    spacing='2'
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