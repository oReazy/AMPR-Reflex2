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

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class auth(LS):
    tShowError = False
    tTextError = ''

    tAuthLogin = ''
    tAuthPassword = ''

    def clear(self):
        self.tShowError = False
        self.tAuthLogin = ''
        self.tAuthPassword = ''


    async def auth(self):
        count = await database.getDataMultiCount('users', 'nick', f"'{self.tAuthLogin}'")
        if count > 0:
            data_bytes = self.tAuthPassword.encode('utf-8')
            hash_obj = hashlib.sha256(data_bytes)
            hash_hex = hash_obj.hexdigest()
            USER = await database.getData('users', 'nick', f"'{self.tAuthLogin}'")
            if USER[1] == hash_hex:
                self.HASH = USER[2]
                self.USER = await database.getUserHash(f"'{self.HASH}'")
            else:
                self.tShowError = True
                self.tTextError = 'Неверный пароль'
        else:
            self.tShowError = True
            self.tTextError = 'Игрок не найден'



def index(size):
    return rx.dialog.root(
    rx.dialog.trigger(rx.button("Войти", size=size, on_click=auth.clear)),
    rx.dialog.content(
        rx.cond(auth.serverOpenAuth == 1,
                rx.flex(
                    rx.dialog.title("Войти"),
                    rx.cond(auth.tShowError,
                            rx.flex(
                                rx.icon('triangle-alert', size=18, color=rx.color("tomato", 9)),
                                rx.text(auth.tTextError, color_scheme='tomato'),
                                direction='row',
                                spacing='1',
                                align='center'
                            )),
                    rx.input(value=auth.tAuthLogin, placeholder='Логин', width='100%', on_change=auth.set_tAuthLogin),
                    rx.input(value=auth.tAuthPassword, placeholder='Пароль', width='100%', on_change=auth.set_tAuthPassword, type='password'),
                    rx.button('Войти', width='100%', on_click=auth.auth),
                    direction='column',
                    spacing='2',
                ),
                rx.flex(
                    rx.center(rx.icon('octagon-x', color=rx.color('tomato', 9), size=50)),
                    rx.center(rx.text('Вход закрыт', weight='bold', size='4')),
                    rx.text('В данный момент вход для игроков приостановлен. Попробуйте позже', size='1', align='center'),
                    direction='column',
                    align='center',
                    spacing='2',
                ),
        ),
        width='250px',
        size='2'
    ),
)