"""

[ COMPONENTS ]

Компонент верхней части проекта (шапка)

"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
import json, ast, datetime, time

from rxconfig import config
from typing import Literal

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

import AMPR.states.localStorage as localStorage
import AMPR.components.auth as ButtonAuth
import AMPR.components.registration as ButtonRegistration

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class header(LS):
    tLogo = '/images/logo/a_gray.png'

    def onMouse(self):
        self.tLogo = '/images/logo/a.png'

    def unMouse(self):
        self.tLogo = '/images/logo/a_gray.png'


def index():
    return rx.container(
        rx.flex(
            rx.flex(
                rx.image(src=header.tLogo, height='35px', on_mouse_enter=header.onMouse, on_mouse_leave=header.unMouse, on_click=rx.redirect('/')),
                direction='row',
                spacing='2',
                align='center'
            ),
            rx.cond(LS.HASH == '0',
                    rx.flex(
                        ButtonAuth.index('3'),
                        ButtonRegistration.index('3'),
                        spacing='2'
                    ),
                    rx.flex(
                        rx.cond(
                            header.USER[15] != 0,
                            rx.button(rx.icon('briefcase-business', size=20), 'Рабочее место', size='3', variant='soft', on_click=rx.redirect('/admin')),
                        ),
                        rx.button(rx.icon('backpack', size=23), size='3', on_click=rx.redirect('/inventory')),
                        rx.button(rx.icon('map', size=23), size='3', on_click=rx.redirect('/map')),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.avatar(src=rx.get_upload_url(f'{header.USER[18]}')),
                            ),
                            rx.menu.content(
                                # rx.menu.item("Мой профиль"),
                                # rx.menu.separator(),
                                # rx.menu.item("Донат", shortcut="0"),
                                rx.menu.item(rx.icon('circle-help', size=20), "Помощь", on_click=rx.redirect('/help')),
                                rx.menu.separator(),
                                rx.menu.item("Выйти", color_scheme='tomato', on_click=[rx.clear_local_storage(), rx.redirect('/')]),
                                side='bottom',
                                align='end',
                                width='220px'
                            ),
                        ),
                        spacing='2'
                    ),),
            margin_top='-30px',
            justify='between',
            align='center',
        ),
        size='4'
    )




def indexWelcome():
    return rx.container(
        rx.flex(
            rx.image(src=header.tLogo, height='35px', on_mouse_enter=header.onMouse, on_mouse_leave=header.unMouse, on_click=rx.redirect('/')),
            rx.cond(LS.HASH == '0',
                    rx.flex(
                        ButtonAuth.index('3'),
                        ButtonRegistration.index('3'),
                        spacing='2'
                    ),
                    rx.flex(
                        rx.cond(
                            header.USER[15] != 0,
                            rx.button(rx.icon('briefcase-business', size=20), 'Рабочее место', size='3', variant='soft'),
                        ),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.avatar(src=rx.get_upload_url(f'{header.USER[18]}')),
                            ),
                            rx.menu.content(
                                # rx.menu.item("Мой профиль"),
                                # rx.menu.separator(),
                                # rx.menu.item("Донат", shortcut="0"),
                                # rx.menu.separator(),
                                rx.menu.item("Выйти", color_scheme='tomato', on_click=[rx.clear_local_storage(), rx.redirect('/')]),
                                side='bottom',
                                align='end',
                                width='220px'
                            ),
                        ),
                        spacing='2'
                    ),),
            margin_top='-30px',
            justify='between',
            align='center',
        ),
        size='4'
    )



def indexCloseGame():
    return rx.container(
        rx.flex(
            rx.image(src=header.tLogo, height='35px', on_mouse_enter=header.onMouse, on_mouse_leave=header.unMouse, on_click=rx.redirect('/')),
            margin_top='-30px',
            align='center',
        ),
        size='4'
    )