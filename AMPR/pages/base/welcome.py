"""

[ PAGES ]

Страница велком (первичный обязательный квест)

"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
import json, ast, datetime, time

from rxconfig import config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

import AMPR.components.header as header
from AMPR.states.base.welcome import State

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

style = {"text-decoration": "none !important",  # Убираем подчёркивание
         "color": "inherit !important",  # Цвет наследуется от родителя
         "cursor": "hover",  # Убираем указатель на ссылке
        }
hover = {"color": "inherit !important",  # Цвет не меняется при наведении
        "text-decoration": "none !important",  # Подчёркивание не появляется
        "background-color": "transparent !important",  # Чтобы исключить изменения фона
        }

@rx.page(route="/welcome-1", title="«AMPR» — Добро пожаловать!", on_load=[LS.onLoadWelcome, State.CheckStage1])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.text('👋 Добро пожаловать на American Project', weight="medium"),
                        width='450px',
                    ),
                    rx.card(
                        rx.icon('check', size=40, color=rx.color("blue", 9), stroke_width=3),
                        rx.text('Мы рады, что вы решили присоединиться к проекту. Вас ждет множество увлекательных механик, интересных людей и многое другое!'),
                        width='450px',
                    ),
                    rx.button('Продолить', width='450px', on_click=[State.set2, rx.redirect('/welcome-2')]),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-2", title="«AMPR» — Предъявите документы", on_load=[LS.onLoadWelcome, State.CheckStage2])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Добрый день, вы на границе.', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Пожалуйста, предоставьте ваши документы', color=rx.color('gray', 9), size='2', weight='medium'),
                        width='450px',
                    ),
                    rx.button(rx.icon('book-user', size=20), 'Предоставить документы', width='450px', on_click=[State.set3, rx.redirect('/welcome-3')]),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-3", title="«AMPR» — Представьтесь", on_load=[LS.onLoadWelcome, State.stage3, State.CheckStage3])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Ваше имя и фамилия?', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Пожалуйста, представьтесь и как вас зовут.', color=rx.color('gray', 9), size='2', weight='medium'),
                        rx.input(placeholder='Имя', width='100%', margin_top='8px', on_change=[State.set_tName, State.check], max_length=20),
                        rx.input(placeholder='Фамилия', width='100%', margin_top='8px', on_change=[State.set_tSurname, State.check], max_length=20),
                        width='450px',
                    ),
                    rx.button(rx.icon('message-circle', size=20), 'Представиться', width='450px', disabled=State.tIsName, on_click=[State.set4, rx.redirect('/welcome-4')]),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-4", title="«AMPR» — Выберить пол персонажа", on_load=[LS.onLoadWelcome, State.CheckStage4])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Хорошо. Подождите минутку.', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Пока инспектор проверяет ваши паспортные данные, укажите пол вашего персонажа.', color=rx.color('gray', 9), size='2', weight='medium'),
                        width='450px',
                    ),
                    rx.flex(
                        rx.button(rx.icon('user', size=20), 'Мужчина', width='221px', on_click=[State.set5, State.MAN, rx.redirect('/welcome-5')]),
                        rx.button(rx.icon('user', size=20), 'Женщина', width='221px', on_click=[State.set5, State.WOMAN, rx.redirect('/welcome-5')], color_scheme='tomato'),
                        direction='row',
                        spacing='2',
                        width='450px'
                    ),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-5", title="«AMPR» — Сколько вам лет", on_load=[LS.onLoadWelcome, State.stage5, State.CheckStage5])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Сколько вам лет?', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Скажите инспектору, сколько вам лет', color=rx.color('gray', 9), size='2', weight='medium'),
                        rx.input(placeholder='Возраст', width='100%', margin_top='8px', on_change=[State.set_tAge, State.check_age]),
                        width='450px',
                    ),
                    rx.button(rx.icon('message-circle', size=20), 'Сказать', width='450px', disabled=State.tIsAge, on_click=[State.set6, State.SETAGEDB, rx.redirect('/welcome-6')]),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-6", title="«AMPR» — С какой целью вы приехали в США?", on_load=[LS.onLoadWelcome, State.stage6, State.CheckStage6])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('С какой целью вы приехали в США?', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Укажите вашу цель', color=rx.color('gray', 9), size='2', weight='medium'),
                        width='450px',
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.cond(State.tEmigrate == '1',
                                        rx.icon('check', size=25, color=rx.color("blue", 9), stroke_width=3),
                                        rx.icon('earth', size=25),
                                        ),
                                rx.heading('Ситуация в своей стране', size='3'),
                                spacing='2',
                                align='center',
                                direction='row'
                            ),
                            rx.divider(margin_top='8px', margin_bottom='4px'),
                            rx.text('Рассказать сотруднику таможни про ситуацию в вашей стране и то, что вы стали эмигрантом из той страны, откуда вы приехали.'),
                            width='450px',
                            on_click=State.Emigrate1
                        ),
                        style=style,
                        _hover=hover,
                        href='javascript:void(0);'
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.cond(State.tEmigrate == '2',
                                        rx.icon('check', size=25, color=rx.color("blue", 9), stroke_width=3),
                                        rx.icon('wallet', size=25),
                                ),
                                rx.heading('Заработок денег', size='3'),
                                spacing='2',
                                align='center',
                                direction='row'
                            ),
                            rx.divider(margin_top='8px', margin_bottom='4px'),
                            rx.text('Рассказать инспектору, что вы приехали за заработком денег.'),
                            width='450px',
                            on_click=State.Emigrate2
                        ),
                        style=style,
                        _hover=hover,
                        href='javascript:void(0);'
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.cond(State.tEmigrate == '3',
                                        rx.icon('check', size=25, color=rx.color("blue", 9), stroke_width=3),
                                        rx.icon('store', size=25),
                                        ),
                                rx.heading('Бизнес', size='3'),
                                spacing='2',
                                align='center',
                                direction='row'
                            ),
                            rx.divider(margin_top='8px', margin_bottom='4px'),
                            rx.text('Рассказать инспектору, что вы приехали в штаты, чтобы начать вести свой бизнес.'),
                            width='450px',
                            on_click=State.Emigrate3
                        ),
                        style=style,
                        _hover=hover,
                        href='javascript:void(0);'
                    ),
                    rx.link(
                        rx.card(
                            rx.flex(
                                rx.cond(State.tEmigrate == '4',
                                        rx.icon('check', size=25, color=rx.color("blue", 9), stroke_width=3),
                                        rx.icon('armchair', size=25),
                                        ),
                                rx.heading('Карьера', size='3'),
                                spacing='2',
                                align='center',
                                direction='row'
                            ),
                            rx.divider(margin_top='8px', margin_bottom='4px'),
                            rx.text('Рассказать инспектору, что вы приехали в штаты, чтобы продвигаться по карьерной лестнице.'),
                            width='450px',
                            on_click=State.Emigrate4
                        ),
                        style=style,
                        _hover=hover,
                        href='javascript:void(0);'
                    ),
                    rx.button(rx.icon('message-circle', size=20), 'Рассказать', width='450px', disabled=State.tIsEmigrate, on_click=[State.set7, rx.redirect('/welcome-7')]),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-7", title="«AMPR» — Аватарка", on_load=[LS.onLoadWelcome, State.CheckStage7])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Хорошо. Сейчас все сверим.', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Пока сотрудник границы перепроверяет данные, вы можете выбрать себе аватарку.', color=rx.color('gray', 9), size='2', weight='medium'),
                        width='450px',
                    ),
                    rx.upload(
                        rx.button('Загрузить аватарку'),
                        id="my_upload",
                        max_files=1,
                        max_size=10000000,
                        width='450px',
                        height='200px',
                        accept={
                            "image/png": [".png"],
                            "image/jpeg": [".jpg", ".jpeg"],
                        },
                        on_drop=State.handle_upload(
                            rx.upload_files(upload_id="my_upload")
                        ),
                        border_radius = '8px'
                    ),
                    rx.cond(
                        State.tImg == '',
                        rx.button(rx.icon('redo', size=20), 'Пропустить', width='450px', on_click=[State.set8, rx.redirect('/welcome-8')]),
                        rx.button(rx.icon('circle-arrow-right', size=20), 'Продолжить', width='450px', on_click=[State.set8, rx.redirect('/welcome-8')]),
                    ),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-8", title="«AMPR» — Все отлично", on_load=[LS.onLoadWelcome, State.CheckStage8])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Все отлично', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('С вашими документами все отлично. Вам разрешен въезд в Соединенные Штаты Америки.\n\nВаш паспорт больше не действителен в нашей стране. В первую очередь вам необходимо будет его переоформить в мэрии.', color=rx.color('gray', 9), size='2', weight='medium'),
                        width='450px',
                    ),
                    rx.button(rx.icon('message-circle', size=20), 'Хорошо', width='450px', on_click=[State.set9, rx.redirect('/welcome-9')]),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-9", title="«AMPR» — Получите субсидию", on_load=[LS.onLoadWelcome, State.CheckStage9, State.getBonusDollars])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Это еще не все.', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Каждому въезжаещему в нашу страну, страна выдает начальную субсидию. Распорядитесь ею с умом.', color=rx.color('gray', 9), size='2', weight='medium'),
                        width='450px',
                    ),
                    rx.card(
                        rx.flex(
                            rx.icon("dollar-sign", size=30),
                            rx.flex(
                                rx.text('ДОЛЛАРЫ', size='1'),
                                rx.text(f'{State.tStartBonus}', size='4', weight='bold'),
                                direction='column',
                                padding_left='0.5em'
                            ),
                            align='center',
                            direction='row'
                        ),
                        align='center',
                        width='450px'
                    ),
                    rx.button(rx.icon('hand', size=20), 'Забрать субсидию', width='450px', on_click=[State.set10, rx.redirect('/welcome-10')]),
                    direction='column',
                    align='center',
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

@rx.page(route="/welcome-10", title="«AMPR» — Получите субсидию", on_load=[LS.onLoadWelcome, State.CheckStage10])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('user', size=25, color=rx.color('blue', 9)),
                            rx.text('Сотрудник таможни', weight="medium", padding_left='8px'),
                            direction='row'
                        ),
                        width='450px',
                    ),
                    rx.card(
                        rx.text('Хорошего дня', color=rx.color('blue', 9), size='5', weight='medium'),
                        rx.text('Держите ваши документы и хорошего дня.', color=rx.color('gray', 9), size='2', weight='medium'),
                        width='450px',
                    ),
                    rx.button(rx.icon('hand', size=20), 'Забрать документы и покинуть пограничный контроль', width='450px', on_click=[State.set11, rx.redirect('/excursion-0')]),
                    direction='column',
                    align='center',
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


# НЕ ИСПОЛЬЗУЕТСЯ
@rx.page(route="/welcome-11", title="«AMPR» — Получите субсидию", on_load=[LS.onLoadWelcome, State.CheckStage11])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('info', size=25, color=rx.color("blue", 9), stroke_width=3),
                            rx.heading('Совет', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Проходите сюжетную линию, тем самым вы сможете лучше узнать о проекте.\n\nПроходите различные дополнительные задания и получайте за них награду.'),
                        width='450px',
                        on_click=State.Emigrate3
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Продолжить', width='450px', on_click=[State.set12, rx.redirect('/excursion-0')]),
                    direction='column',
                    align='center',
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