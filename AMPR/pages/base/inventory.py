"""

[ PAGES ]

Страница инвентаря

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
import AMPR.components.passport as passport
from AMPR.states.base.inventory import State

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

@rx.page(route="/inventory", title="«AMPR» — Инвентарь", on_load=[LS.onLoadInventory])
def index():
    return rx.container(
        rx.cond(
            rx.State.is_hydrated,
            rx.container(
                header.index(),
                rx.flex(
                    rx.flex(
                        # Левая
                        rx.heading('Деньги на руках', size='5', padding_bottom="8px"),
                        rx.flex(
                            rx.card(
                                rx.flex(
                                    rx.icon("dollar-sign", size=30),
                                    rx.flex(
                                        rx.text('ДОЛЛАРЫ', size='1'),
                                        rx.text(LS.USER[6], size='4', weight='bold'),
                                        direction='column',
                                        padding_left='0.5em'
                                    ),
                                    align='center',
                                    direction='row'
                                ),
                                align='center',
                                width='150px'
                            ),
                            rx.card(
                                rx.flex(
                                    rx.icon("euro", size=30),
                                    rx.flex(
                                        rx.text('ЕВРО', size='1'),
                                        rx.text(LS.USER[7], size='4', weight='bold'),
                                        direction='column',
                                        padding_left='0.5em'
                                    ),
                                    align='center',
                                    direction='row'
                                ),
                                align='center',
                                width='150px'
                            ),
                            direction='row',
                            spacing='2'
                        ),
                        rx.flex(
                            rx.card(
                                rx.flex(
                                    rx.icon("japanese-yen", size=30),
                                    rx.flex(
                                        rx.text('ИЕНЫ', size='1'),
                                        rx.text(LS.USER[8], size='4', weight='bold'),
                                        direction='column',
                                        padding_left='0.5em'
                                    ),
                                    align='center',
                                    direction='row'
                                ),
                                align='center',
                                width='150px'
                            ),
                            rx.card(
                                rx.flex(
                                    rx.icon("pound-sterling", size=30),
                                    rx.flex(
                                        rx.text('ФУНТЫ', size='1'),
                                        rx.text(LS.USER[9], size='4', weight='bold'),
                                        direction='column',
                                        padding_left='0.5em'
                                    ),
                                    align='center',
                                    direction='row'
                                ),
                                align='center',
                                width='150px'
                            ),
                            direction='row',
                            spacing='2'
                        ),
                        rx.heading('Взаимодействие', size='5', padding_top="8px"),
                        rx.flex(
                            rx.cond(State.inventoryPassport == '0',
                                    rx.tooltip(rx.button(rx.icon('book', size=25), width='50px', height='50px', variant='soft', color_scheme='gray'), content='❌ У вас нет паспорта', side='bottom', delay_duration=1),
                                    passport.index()
                                    ),
                            rx.tooltip(rx.button(rx.icon('smartphone', size=25), width='50px', height='50px', variant='soft', color_scheme='gray'), content='❌ У вас нет телефона', side='bottom', delay_duration=1),
                            rx.tooltip(rx.button(rx.icon('notebook-text', size=25), width='50px', height='50px', variant='soft', color_scheme='gray'), content='❌ У вас нет записной книжки', side='bottom', delay_duration=1),
                            rx.tooltip(rx.button(rx.icon('scroll-text', size=25), width='50px', height='50px', variant='soft', color_scheme='gray'), content='❌ У вас нет принятых квестов', side='bottom', delay_duration=1),
                            spacing='2',
                            direction='row',
                        ),
                        rx.heading('Персонаж', size='5', padding_top="8px"),
                        rx.hover_card.root(
                            rx.hover_card.trigger(
                                rx.card(
                                    rx.flex(
                                        rx.icon('heart', color=rx.color('tomato', 9), size=30, stroke_width=2),
                                        rx.flex(
                                            rx.flex(
                                                rx.text('Здоровье', weight='bold'),
                                                rx.text(f'{State.inventoryHealthInt}'),
                                                justify='between',
                                                align='center'
                                            ),
                                            rx.progress(value=State.inventoryHealth, width='100%', color_scheme='tomato'),
                                            direction='column',
                                            spacing='2',
                                            width='100%',
                                        ),
                                        direction='row',
                                        align='center',
                                        spacing='2',
                                        width='100%',
                                    ),
                                    width='100%'
                                ),
                            ),
                            rx.hover_card.content(
                                rx.flex(
                                    rx.flex(
                                        rx.inset(
                                            rx.image(
                                                src=f"/images/items/heart.png",
                                                width=f"150px",
                                                height='100%',
                                                style=style2
                                            ),
                                            margin_right='0px',
                                            padding_right='0px',
                                            width=f"150px",
                                            side="left",
                                        ),
                                        width=f'auto'
                                    ),
                                    rx.flex(
                                        rx.flex(
                                            rx.flex(
                                                rx.heading(f'Здоровье', size='4'),
                                                direction='row',
                                                spacing='2',
                                                align='center'
                                            ),
                                            rx.text(f'Это важный показатель у вашего персонажа. Если показатель опустится ниже 0, то вы попадете в больницу'),
                                            direction='column',
                                            spacing='2'
                                        ),
                                        rx.button(rx.icon('arrow-up-right'), 'Подробнее в WIKI', on_click=rx.redirect(f'/'), variant=f'soft'),
                                        direction='column',
                                        justify='between',
                                        spacing='2',
                                        align='baseline',
                                    ),
                                    spacing='4',
                                    direction='row',
                                    width='100%'
                                ),
                                side='right',
                                style={
                                    "overflow": "hidden",
                                    "max_width": "600px"
                                },
                                width='100%'
                            ),
                        ),
                        rx.hover_card.root(
                            rx.hover_card.trigger(
                                rx.card(
                                    rx.flex(
                                        rx.icon('pizza', color=rx.color('amber', 9), size=30, stroke_width=2),
                                        rx.flex(
                                            rx.flex(
                                                rx.text('Еда', weight='bold'),
                                                rx.text(f'{State.inventoryEatInt}'),
                                                justify='between',
                                                align='center'
                                            ),
                                            rx.progress(value=State.inventoryEat, width='100%', color_scheme='amber'),
                                            direction='column',
                                            spacing='2',
                                            width='100%'
                                        ),
                                        direction='row',
                                        spacing='2',
                                        width='100%',
                                        align='center'
                                    ),
                                    width='100%'
                                ),
                            ),
                            rx.hover_card.content(
                                rx.flex(
                                    rx.flex(
                                        rx.inset(
                                            rx.image(
                                                src=f"/images/items/eat.png",
                                                width=f"150px",
                                                height='100%',
                                                style=style2
                                            ),
                                            margin_right='0px',
                                            padding_right='0px',
                                            width=f"150px",
                                            side="left",
                                        ),
                                        width=f'auto'
                                    ),
                                    rx.flex(
                                        rx.flex(
                                            rx.flex(
                                                rx.heading(f'Еда', size='4'),
                                                direction='row',
                                                spacing='2',
                                                align='center'
                                            ),
                                            rx.text(f'Показатель, который показывает сытость вашего персонажа. Кушайте любую еду и пейте воду, чтобы пополнить данный показатель. Если показатель еды у вас будет на низком значении, то ваш персонаж будет терять здоровье'),
                                            direction='column',
                                            spacing='2'
                                        ),
                                        rx.button(rx.icon('arrow-up-right'), 'Подробнее в WIKI', on_click=rx.redirect(f'/'), variant=f'soft'),
                                        direction='column',
                                        justify='between',
                                        spacing='2',
                                        align='baseline',
                                    ),
                                    spacing='4',
                                    direction='row',
                                    width='100%'
                                ),
                                side='right',
                                style={
                                    "overflow": "hidden",
                                    "max_width": "600px"
                                },
                                width='100%'
                            ),
                        ),
                        spacing='2',
                        direction='column',
                    ),
                    rx.flex(
                        # Правая
                        rx.flex(
                            rx.heading('Предметы', size='5', padding_bottom="8px"),
                            rx.tooltip(
                                rx.segmented_control.root(
                                    rx.segmented_control.item(rx.icon('arrow-down-up', size=15), value="standart", on_mouse_enter=State.setSortedTooltip1),
                                    rx.segmented_control.item(rx.icon('arrow-down-wide-narrow', size=15), value="up-to-down", on_mouse_enter=State.setSortedTooltip2),
                                    rx.segmented_control.item(rx.icon('arrow-down-narrow-wide', size=15), value="down-to-up", on_mouse_enter=State.setSortedTooltip3),
                                    rx.segmented_control.item(rx.icon('arrow-down-a-z', size=15), value="a-z", on_mouse_enter=State.setSortedTooltip4),
                                    rx.segmented_control.item(rx.icon('arrow-down-z-a', size=15), value="z-a", on_mouse_enter=State.setSortedTooltip5),
                                    value=LS.inventorySorting,
                                    on_change=[LS.set_inventorySorting, LS.onLoadInventory],
                                ),
                                content=State.sortedTooltip,
                                side='left',
                                delay_duration=3
                            ),
                            justify='between',
                            direction='row',
                            align='center'
                        ),
                        rx.cond(LS.inventoryCount == 0,
                                rx.card(
                                    rx.flex(
                                        rx.icon(tag='x', size=30, color=rx.color(f"tomato", 9)),
                                        rx.flex(
                                            rx.text(f'Инветарь пустой', size='4', weight='bold'),
                                            direction='column',
                                            padding_left='0.5em'
                                        ),
                                        align='center',
                                        direction='row'
                                    ),
                                    align='center',
                                    width='100%'
                                )),
                        rx.foreach(LS.inventoryDone, lambda line:
                                   rx.flex(
                                       rx.foreach(line, lambda item:
                                       rx.flex(
                                           rx.cond(item[5][0] == 0,
                                                   rx.card(
                                                       rx.flex(
                                                           rx.match(
                                                               item[2],
                                                               ('tree-deciduous', rx.icon(tag='tree-deciduous', size=30, color=rx.color(f"{item[4]}", 9))),
                                                               ('brick-wall', rx.icon(tag='brick-wall', size=30, color=rx.color(f"{item[4]}", 9))),
                                                               ('gift', rx.icon(tag='gift', size=30, color=rx.color(f"{item[4]}", 9))),
                                                               ('leaf', rx.icon(tag='leaf', size=30, color=rx.color(f"{item[4]}", 9))),
                                                               ('box', rx.icon(tag='box', size=30, color=rx.color(f"{item[4]}", 9))),
                                                           ),
                                                           rx.flex(
                                                               rx.text(item[1], size='1'),
                                                               rx.text(item[8], size='4', weight='bold'),
                                                               direction='column',
                                                               padding_left='0.5em'
                                                           ),
                                                           align='center',
                                                           direction='row'
                                                       ),
                                                       align='center',
                                                       width='100%',
                                                   ),
                                                   rx.hover_card.root(
                                                       rx.hover_card.trigger(
                                                           rx.card(
                                                               rx.flex(
                                                                   rx.match(
                                                                       item[2],
                                                                       ('tree-deciduous', rx.icon(tag='tree-deciduous', size=30, color=rx.color(f"{item[4]}", 9))),
                                                                       ('brick-wall', rx.icon(tag='brick-wall', size=30, color=rx.color(f"{item[4]}", 9))),
                                                                       ('gift', rx.icon(tag='gift', size=30, color=rx.color(f"{item[4]}", 9))),
                                                                       ('leaf', rx.icon(tag='leaf', size=30, color=rx.color(f"{item[4]}", 9))),
                                                                       ('box', rx.icon(tag='box', size=30, color=rx.color(f"{item[4]}", 9))),
                                                                   ),
                                                                   rx.flex(
                                                                       rx.text(item[1], size='1'),
                                                                       rx.text(item[8], size='4', weight='bold'),
                                                                       direction='column',
                                                                       padding_left='0.5em'
                                                                   ),
                                                                   align='center',
                                                                   direction='row'
                                                               ),
                                                               align='center',
                                                               width='100%'
                                                           ),
                                                           on_click=State.InventoryUseItem(item[9]),
                                                       ),
                                                       rx.hover_card.content(
                                                           rx.flex(
                                                               rx.cond(item[5][6] == 1,
                                                                       rx.flex(
                                                                           rx.inset(
                                                                               rx.image(
                                                                                   src=f"{item[5][1]}",
                                                                                   width=f"{item[5][2]}",
                                                                                   height='100%',
                                                                                   style=style2
                                                                               ),
                                                                               margin_right='0px',
                                                                               padding_right='0px',
                                                                               width=f"{item[5][2]}",
                                                                               side="left",
                                                                           ),
                                                                           width=f'auto'
                                                                       ),
                                                                       ),
                                                               rx.flex(
                                                                   rx.flex(
                                                                       rx.flex(
                                                                           rx.heading(f'{item[9]}', size='4'),
                                                                           rx.badge(item[6], color_scheme='gray'),
                                                                           direction='row',
                                                                           spacing='2',
                                                                           align='center'
                                                                       ),
                                                                       rx.text(f'{item[5][3]}'),
                                                                       direction='column',
                                                                       spacing='2'
                                                                   ),
                                                                   rx.flex(
                                                                       rx.cond(item[6] == 'Здоровье',
                                                                               rx.button(rx.icon('hand'), 'Использовать', variant=f'solid', color_scheme='tomato', on_click=State.InventoryUseItem(item[9]))),
                                                                       rx.cond(item[6] == 'Еда',
                                                                               rx.button(rx.icon('hand'), 'Использовать', variant=f'solid', color_scheme='amber', on_click=State.InventoryUseItem(item[9]))),
                                                                       rx.cond(item[6] == 'Деньги',
                                                                               rx.button(rx.icon('hand'), 'Использовать', variant=f'solid', color_scheme='green', on_click=State.InventoryUseItem(item[9]))),
                                                                       rx.cond(item[6] == 'Донат',
                                                                               rx.button(rx.icon('hand'), 'Использовать', variant=f'solid', color_scheme='blue', on_click=State.InventoryUseItem(item[9]))),
                                                                       rx.cond(item[6] == 'Опыт',
                                                                               rx.button(rx.icon('hand'), 'Использовать', variant=f'solid', color_scheme='blue', on_click=State.InventoryUseItem(item[9]))),
                                                                       rx.cond(item[5][4] == 1,
                                                                               rx.button(rx.icon('arrow-up-right'), 'Подробнее в WIKI', on_click=rx.redirect(f'{item[5][5]}'), variant=f'soft')),
                                                                       direction='row',
                                                                       spacing='2'
                                                                   ),
                                                                   direction='column',
                                                                   justify='between',
                                                                   spacing='2',
                                                                   align='baseline',
                                                               ),
                                                               spacing='4',
                                                               direction='row',
                                                               width='100%'
                                                           ),
                                                           style={
                                                                "overflow": "hidden",
                                                                "max_width": "600px"
                                                            },
                                                           width='100%'
                                                       ),
                                                   ),
                                                   ),
                                           width='100%'
                                       ),
                                       ),
                                       direction='row',
                                       spacing='2',
                                       width='787px'
                                       # width='772px'
                                   ),
                                   ),
                        direction='column',
                        padding_left='8px',
                        spacing='2'
                    ),
                    # Основа между двумя раздлениями
                    direction='row',
                ),
                rx.theme_panel(default_open=False),
                size='4'
            ),
            rx.center(
                rx.spinner(),
                height="100vh",  # Высота экрана
            )
        ),
        size='4'
    )