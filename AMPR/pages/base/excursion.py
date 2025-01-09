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

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

style = {
            "object-fit": "cover",  # Покрытие всей области
            "object-position": "center",  # Центровка изображения
         }

@rx.page(route="/excursion-0", title="«AMPR» — Совет: сюжетная линия", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('info', size=25, color=rx.color("blue", 9)),
                            rx.heading('Совет: сюжетная линия', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Проходите сюжетную линию, тем самым вы сможете лучше узнать о проекте.\n\nПроходите различные дополнительные задания и получайте за них награду.'),
                        width='450px',
                    ),
                    rx.button('Продолить', width='450px', on_click=rx.redirect('/excursion-1')),
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

@rx.page(route="/excursion-1", title="«AMPR» — Приглашение на экскурсию", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.indexWelcome(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon('message-circle-question', size=25, color=rx.color("blue", 9)),
                            rx.heading('Экскурсия', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Желаете ли вы пройти небольшую экскурсию и разобраться в игре?'),
                        width='450px',
                    ),
                    rx.button(rx.icon('graduation-cap', size=20), 'Пройти экскурсию', width='450px', on_click=rx.redirect('/excursion-2')),
                    rx.button(rx.icon('redo', size=20), 'Пропустить', width='450px', on_click=rx.redirect('/inventory')),
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

@rx.page(route="/excursion-2", title="«AMPR» — Добро пожаловать!", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.image('/images/excursion/emoji1.png', width='25px', height='25px'),
                            rx.heading('Добро пожаловать', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('На нашем проекте вы найдете много интересного для себя. Увлекательные работы, системы, которыми приятно пользоваться каждый раз — это то, что вас ждет в данной игре. '),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-3')),
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

@rx.page(route="/excursion-3", title="«AMPR» — Первым делом", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image2.jpg",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji2.png', width='25px', height='25px'),
                            rx.heading('Первым делом', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Сейчас вам желательно добраться до мэрии и получить новый паспорт. Чтобы получить паспорт, вам необходимо поговорить с сотрудником мэрии. После получения паспорта, вы сможете начать строить свою карьеру, учиться и покупать имущество.'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-4')),
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

@rx.page(route="/excursion-4", title="«AMPR» — Одевайтесь", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image3.jpg",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji3.png', width='25px', height='25px'),
                            rx.heading('Одевайтесь', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('В любой момент вы можете посетить магазин одежды и подобрать новый образ вашему персонажу. Носить модные вещи или носить дорогие — решать вам'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-5')),
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

@rx.page(route="/excursion-5", title="«AMPR» — Пора работать", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image4.jpg",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji4.png', width='25px', height='25px'),
                            rx.heading('Пора работать', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('На нашем проекте есть множество подработок и основных работ, где вы можете заработать денег.'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-6')),
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

@rx.page(route="/excursion-6", title="«AMPR» — Получение прав", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image5.jpg",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji5.png', width='25px', height='25px'),
                            rx.heading('Получение прав', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('После получения паспорта и немного заработанных денег, вы можете отправиться в центр лицензирования и сдать теорию и практику.'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-7')),
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

@rx.page(route="/excursion-7", title="«AMPR» — Организации", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image6.webp",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji6.png', width='25px', height='25px'),
                            rx.heading('Организации', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Если вам нравится составлять отчеты, наказывать преступников или же делать газеты, то ваш путь в государственные структуры.'),
                        rx.text('Если вам нравится кого-либо грабить, заниматься черными делами, то ваш путь лежит в банды или мафии.', padding_top='25px'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-8')),
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

@rx.page(route="/excursion-8", title="«AMPR» — Автосалоны", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image7.jpg",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji7.png', width='25px', height='25px'),
                            rx.heading('Автосалоны', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('На проекте есть более 1000 различных автомобилей. Все их можно посмотреть в различных автосалонах.'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-9')),
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

@rx.page(route="/excursion-9", title="«AMPR» — Дома", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image8.jpe",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji8.png', width='25px', height='25px'),
                            rx.heading('Дома', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('На проекте есть больше 3000 видов домов. Только вы можете решить, как будет выглядеть ваш дом.'),
                        rx.text('В домах можно крафтить предметы, припарковывать автомобили, хранить вещи и многое другое!', padding_top='25px'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-10')),
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

@rx.page(route="/excursion-10", title="«AMPR» — Будьте осторожны со здоровьем", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/images/excursion/image10.jpg",
                                width="100%",
                                height="171px",
                                style=style
                            ),
                            side="top",
                            decoding='cover',
                            pb="current",
                        ),
                        rx.flex(
                            rx.image('/images/excursion/emoji10.png', width='25px', height='25px'),
                            rx.heading('Будьте осторожны со здоровьем', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Следите за показателем здоровья. В случае, если у вас будет мало здоровья, вас отвезут в больницу.'),
                        rx.text('Становитесь здоровее с помощью физкультуры, таблеток и многого другого.', padding_top='25px'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Далее', width='450px', on_click=rx.redirect('/excursion-11')),
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

@rx.page(route="/excursion-11", title="«AMPR» — Поздравляем, вы прошли экскурсию", on_load=[LS.onLoad])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.image('/images/excursion/emoji11.png', width='25px', height='25px'),
                            rx.heading('Поздравляем, вы прошли экскурсию', size='3'),
                            spacing='2',
                            align='center',
                            direction='row'
                        ),
                        rx.divider(margin_top='8px', margin_bottom='4px'),
                        rx.text('Если у вас возникнут вопросы, то вы всегда можете посмотреть прохождения и уроки на YouTube, а также вы можете с нами связаться в группе ВКонтакте'),
                        width='450px',
                    ),
                    rx.button(rx.icon('circle-arrow-right', size=20), 'Закончить экскурсию', width='450px', on_click=rx.redirect('/inventory')),
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