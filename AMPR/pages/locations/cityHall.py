"""

[ LOCATIONS ]

Мэрия

"""
from idlelib.colorizer import color_config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx

from rxconfig import config
import json
from typing import Tuple

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

import AMPR.components.header as header
from AMPR.states.locations.cityHall import State

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

style = {"text-decoration": "none !important",  # Убираем подчёркивание
         "color": "inherit !important",  # Цвет наследуется от родителя
         "cursor": "hover",  # Убираем указатель на ссылке
        }
hover = {"color": "inherit !important",  # Цвет не меняется при наведении
        "text-decoration": "none !important",  # Подчёркивание не появляется
        "background-color": "transparent !important",  # Чтобы исключить изменения фона
        }
style2 = {
            "object-fit": "cover",  # Покрытие всей области
            "object-position": "center",  # Центровка изображения
         }


@rx.page(route="/places/cityHall/give-passport", title="«AMPR» — Услуга: получить паспорт", on_load=[LS.onLoad, State.startDialog])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.flex(
                        rx.card(
                            rx.flex(
                                rx.button(
                                    rx.icon('circle-arrow-left', size=20), 'Назад', variant='solid', on_click=rx.redirect('/places/cityHall/')),
                                direction='row'
                            ),
                            rx.divider(margin_top='8px'),
                            rx.flex(
                                rx.flex(
                                    rx.text('Вас обслуживает:'),
                                    align='center',
                                    spacing='2',
                                    margin_top='8px',
                                ),
                                rx.flex(
                                    rx.image(
                                        src="/images/places/SF-CityHall-Passport.jpg",
                                        width="45px",
                                        height="45px",
                                        border_radius="300px",
                                        style=style2
                                    ),
                                    rx.flex(
                                        rx.text('Carol Rivera', weight='bold'),
                                        rx.text('сотрудник мэрии', size='2'),
                                        direction='column'
                                    ),
                                    align='center',
                                    spacing='2',
                                    margin_top='8px',
                                    direction='row'),
                                direction='column'
                            ),
                            width='350px',
                            direction='column',
                        ),
                        # rx.card(
                        #     rx.flex(
                        #         rx.icon('newspaper', color=rx.color('blue', 9)),
                        #         rx.text('Новости', padding_left='8px', weight='bold'),
                        #         direction='row',
                        #     ),
                        #     width='100%'
                        # ),
                        spacing='2',
                        width='350px',
                        direction='column',
                    ),
                    rx.cond(State.Stage == '1',
                            rx.flex(
                                rx.flex(
                                    rx.card(
                                        rx.flex(
                                            rx.match(
                                                State.tDialogIcon,
                                                ('message-circle', rx.icon(tag='message-circle', size=24, color=rx.color(State.tDialogIconColor, 9))),
                                                ('hand', rx.icon(tag='hand', size=24, color=rx.color(State.tDialogIconColor, 9))),
                                                ('x', rx.icon(tag='x', size=24, color=rx.color(State.tDialogIconColor, 9))),
                                                ('banknote', rx.icon(tag='banknote', size=24, color=rx.color(State.tDialogIconColor, 9))),
                                                ('plus', rx.icon(tag='plus', size=24, color=rx.color(State.tDialogIconColor, 9))),
                                                ('message-square', rx.icon(tag='message-square', size=24, color=rx.color(State.tDialogIconColor, 9))),
                                                ('credit-card', rx.icon(tag='credit-card', size=24, color=rx.color(State.tDialogIconColor, 9))),
                                            ),
                                            rx.text(State.tDialogText, width='90%'),
                                            width='100%',
                                            spacing='2',
                                            direction='row'
                                        ),
                                        rx.cond(
                                            State.tDialogImage != '',
                                            rx.inset(
                                                rx.image(
                                                    src=f"{State.tDialogImage}",
                                                    width="100%",
                                                    height=State.tDialogImageHeight,
                                                    style=style2
                                                ),
                                                margin_top='8px',
                                                side="bottom",
                                            ),
                                        ),
                                        width='100%',
                                    ),
                                    spacing='2',
                                    direction='row',
                                    width='100%'
                                ),
                                rx.foreach(State.tDialogMassiveDone,
                                           lambda tLine:
                                           rx.flex(
                                               rx.foreach(tLine,
                                                          lambda item:
                                                          rx.link(
                                                              rx.card(
                                                                  rx.flex(
                                                                      rx.match(
                                                                          item[0],
                                                                          ('message-circle', rx.icon(tag='message-circle', size=24, color=rx.color(item[1], 9))),
                                                                          ('hand', rx.icon(tag='hand', size=24, color=rx.color(item[1], 9))),
                                                                          ('x', rx.icon(tag='x', size=24, color=rx.color(item[1], 9))),
                                                                          ('banknote', rx.icon(tag='banknote', size=24, color=rx.color(item[1], 9))),
                                                                          ('plus', rx.icon(tag='plus', size=24, color=rx.color(item[1], 9))),
                                                                          ('message-square', rx.icon(tag='message-square', size=24, color=rx.color(item[1], 9))),
                                                                          ('credit-card', rx.icon(tag='credit-card', size=24, color=rx.color(item[1], 9))),
                                                                      ),
                                                                      rx.text(item[3], weight='bold'),
                                                                      width='100%',
                                                                      spacing='2',
                                                                      direction='row'
                                                                  ),
                                                                  background=rx.color(item[2], 4),
                                                                  on_click=State.controlState(item[5]),
                                                                  width='100%'
                                                              ),
                                                              style=style,
                                                              _hover=hover,
                                                              href=item[4],
                                                              width='100%',
                                                          ),
                                                          ),
                                               spacing='2',
                                           )),
                                spacing='2',
                                width='67.5%',
                                direction='column',
                            ),
                        ),
                    direction='row',
                    spacing='2',
                ),
            ),
            rx.center(
                rx.spinner(),
                height="100vh",  # Высота экрана
            )
        ),
        size='4'
    )


@rx.page(route="/places/cityHall", title="«AMPR» — Мэрия", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.flex(
                        rx.card(
                            rx.flex(
                                rx.inset(
                                    rx.image(
                                        src="/images/places/SF-CityHall.jpg",
                                        width="350px",
                                        height="300px",
                                        style=style2
                                    ),
                                    side="top",
                                ),
                                rx.button(
                                    rx.icon('circle-arrow-left', size=20), 'Назад', margin_left='-328px', variant='solid', background='white', color='black', on_click=rx.redirect('/map/important-places')),
                                direction='row'
                            ),
                            rx.flex(
                                rx.flex(
                                    rx.icon('university', color=rx.color('blue', 9), size=25),
                                    rx.text('Мэрия', weight='bold'),
                                    rx.badge('Правительство', color_scheme='lime'),
                                    rx.badge('Гос. структура'),
                                    align='center',
                                    spacing='2',
                                    margin_top='8px',
                                ),
                                rx.divider(margin_top='8px', margin_bottom='8px'),
                                rx.flex(
                                    rx.text('Мэрия — неотъемлемая часть любого города. Тут вы можете получить услуги от правительства')
                                ),
                                direction='column'
                            ),
                            width='350px',
                            direction='column',
                        ),
                        # rx.card(
                        #     rx.flex(
                        #         rx.icon('newspaper', color=rx.color('blue', 9)),
                        #         rx.text('Новости', padding_left='8px', weight='bold'),
                        #         direction='row',
                        #     ),
                        #     width='100%'
                        # ),
                        spacing='2',
                        width='350px',
                        direction='column',
                    ),
                    rx.flex(
                        rx.flex(
                            rx.link(
                                rx.card(
                                    rx.flex(
                                        rx.text('Получить паспорт', weight='bold'),
                                        rx.badge(rx.icon('zap', color=rx.color('lime', 11), size=12), 'Популярно', color_scheme='lime', size='2'),
                                        spacing='2',
                                        justify='between',
                                        align='center'
                                    ),
                                    rx.flex(
                                        rx.icon('book', color=rx.color('lime', 7), size=35),
                                        align='center',
                                        spacing='2',
                                        justify='between',
                                        direction='row',
                                        margin_top='12px',
                                        margin_bottom='-12px',
                                    ),
                                    width='100%',
                                    direction='column',
                                ),
                                href='/places/cityHall/give-passport',
                                width='100%',
                                style=style,
                                _hover=hover,
                            ),
                            rx.card(
                                rx.flex(
                                    rx.text('Налоги штата', weight='bold'),
                                    spacing='2',
                                    justify='between',
                                    align='center'
                                ),
                                rx.flex(
                                    rx.icon('hand-coins', color=rx.color('lime', 7), size=35),
                                    align='center',
                                    spacing='2',
                                    justify='between',
                                    direction='row',
                                    margin_top='12px',
                                    margin_bottom='-12px',
                                ),
                                width='100%',
                                direction='column',
                            ),
                            spacing='2',
                            direction='row',
                            width='100%'
                        ),
                        rx.flex(
                            # rx.card(
                            #     rx.flex(
                            #         rx.image(
                            #             src="/images/logo/Frame 103.png",
                            #             width="50px",
                            #             height="50px",
                            #             border_radius="300px",
                            #             style=style2
                            #         ),
                            #         rx.flex(
                            #             rx.text('Vova Batenkov', weight='bold'),
                            #             rx.text('губернатор штата', size='1'),
                            #             direction='column'
                            #         ),
                            #         align='center',
                            #         direction='row',
                            #         spacing='2',
                            #     ),
                            #     rx.text('«Моя цель — сделать каждого гражданина счастливым»', margin_top='12px'),
                            #     width='100%',
                            #     direction='column',
                            # ),
                            spacing='2',
                            direction='row',
                            width='100%'
                        ),
                        spacing='2',
                        width='67.5%',
                        direction='column',
                    ),
                    direction='row',
                    spacing='2',
                    align='start'
                ),
            ),
            rx.center(
                rx.spinner(),
                height="100vh",  # Высота экрана
            )
        ),
        size='4'
    )