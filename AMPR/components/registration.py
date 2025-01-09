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

class reg(LS):
    tShowError = False
    tTextError = ''

    tRegLogin = ''
    tRegPassword = ''

    def clear(self):
        self.tShowError = False
        self.tRegLogin = ''
        self.tRegPassword = ''


    async def registration(self):
        count = await database.getDataMultiCount('users', 'nick', f"'{self.tRegLogin}'")
        if count == 0:
            data_bytes = self.tRegPassword.encode('utf-8')
            hash_obj = hashlib.sha256(data_bytes)
            hash_hex = hash_obj.hexdigest()
            await database.addNewAccount(self.tRegLogin, hash_hex)
            USER = await database.getData('users', 'nick', f"'{self.tRegLogin}'")
            self.HASH = USER[2]
            self.USER = await database.getUserHash(f"'{self.HASH}'")
            return rx.redirect('/welcome-1')
        else:
            self.tShowError = True
            self.tTextError = 'Игрок с данным ником уже зарегистрирован'



def index(size):
    return rx.dialog.root(
    rx.dialog.trigger(rx.button("Зарегистрироваться", size=size, on_click=reg.clear)),
    rx.dialog.content(
        rx.cond(reg.serverOpenRegistation == 1,
                rx.flex(
                    rx.dialog.title("Регистрация"),
                    rx.cond(reg.tShowError,
                            rx.flex(
                                rx.icon('triangle-alert', size=18, color=rx.color("tomato", 9)),
                                rx.text(reg.tTextError, color_scheme='tomato'),
                                direction='row',
                                spacing='1',
                                align='center'
                            )),
                    rx.input(value=reg.tRegLogin, placeholder='Логин', width='100%', on_change=reg.set_tRegLogin),
                    rx.input(value=reg.tRegPassword, placeholder='Пароль', width='100%', on_change=reg.set_tRegPassword, type='password'),
                    rx.button('Зарегистрироваться', width='100%', on_click=reg.registration),
                    direction='column',
                    spacing='2',
                ),
                rx.flex(
                    rx.center(rx.icon('octagon-x', color=rx.color('tomato', 9), size=50)),
                    rx.center(rx.text('Регистрация закрыта', weight='bold', size='4')),
                    rx.text('В данный момент регистрация новых игроков приостановлена', size='1', align='center'),
                    direction='column',
                    align='center',
                    spacing='2',
                ),
                ),
        width='250px',
        size='2'
    ),
)