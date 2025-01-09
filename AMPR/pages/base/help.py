"""

[ PAGES ]

Страница карты

"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
import json, ast, datetime, time

from rxconfig import config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

import AMPR.components.header as header
from AMPR.states.base.help import State

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

style = {"text-decoration": "none !important",  # Убираем подчёркивание
         "color": "inherit !important",  # Цвет наследуется от родителя
         "cursor": "hover",  # Убираем указатель на ссылке
        }
hover = {"color": "inherit !important",  # Цвет не меняется при наведении
        "text-decoration": "none !important",  # Подчёркивание не появляется
        "background-color": "transparent !important",  # Чтобы исключить изменения фона
        }


@rx.page(route="/help", title="«AMPR» — Помощь", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.icon('circle-help', size=70, padding_top='12px'),
                    rx.heading('Помощь', size='8'),
                    rx.heading('Поможем решить ваши вопросы по игре', size='3'),
                    align='center',
                    direction='column'
                ),
                rx.flex(
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.icon('book-marked'),
                                rx.text('Правила сервера', weight='bold', size='4'),
                                direction='column'
                            ),
                        ),
                        href='/help/server-rules',
                        style=style,
                        width='100%',
                    ),
                    rx.card(
                        rx.flex(
                            rx.icon('book-open-text'),
                            rx.text('WIKI', weight='bold', size='4'),
                            direction='column'
                        ),
                        width='100%',
                    ),
                    rx.card(
                        rx.flex(
                            rx.icon('message-circle-question'),
                            rx.text('Задать вопрос', weight='bold', size='4'),
                            direction='column'
                        ),
                        background=rx.color('blue', 9),
                        width='100%',
                    ),
                    direction='row',
                    spacing='2',
                    margin_top='28px'
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

@rx.page(route="/help/server-rules", title="«AMPR» — Правила сервера", on_load=[LS.onLoad])
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
                                rx.icon('circle-chevron-left', color=rx.color('blue', 9)),
                                rx.text('Назад', padding_left='8px', weight='bold'),
                                direction='row'
                            ),
                        ),
                        width='20%',
                        style=style,
                        href='/help',
                        height='100%',
                    ),
                    rx.card(
                        rx.markdown(State.SERVER[2], margin_top='-16px', margin_bottom='-16px'),
                        width='100%'
                    ),
                    direction='row',
                    spacing='2',
                    align='start',
                    margin_top='12px'
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