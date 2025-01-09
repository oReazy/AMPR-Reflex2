
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import ast, json
import reflex as rx
from rxconfig import config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class State(LS):
    isUsedItem = 0
    sortedTooltip = 'Сортировка'

    def setSortedTooltip1(self):
        self.sortedTooltip = 'Без сортировки'

    def setSortedTooltip2(self):
        self.sortedTooltip = 'Сортировка: от большего к меньшему'

    def setSortedTooltip3(self):
        self.sortedTooltip = 'Сортировка: от меньшего к большему'

    def setSortedTooltip4(self):
        self.sortedTooltip = 'Сортировка: от А до Я'

    def setSortedTooltip5(self):
        self.sortedTooltip = 'Сортировка: от Я до А'

    async def InventoryUseItem(self, nameItem):
        self.isUsedItem = 0
        if self.HASH != '0':
            self.SERVER = await database.getData('settings', 'id', '1')  # Получаем данные с сервера
            tServerOpen = ast.literal_eval(str(self.SERVER[4]))  # создаем локальную переменную и заносим данные об доступности сервера
            self.serverOpenRegistation = tServerOpen[0]
            self.serverOpenAuth = tServerOpen[1]
            self.serverOpenGame = tServerOpen[2]
            self.USER = await database.getUserHash(f"'{self.HASH}'")
            tSortInventory = json.loads(str(self.USER[16]))
            if self.inventorySorting == 'standart':
                self.inventory = tSortInventory
            if self.inventorySorting == 'up-to-down':
                self.inventory = dict(sorted(tSortInventory.items(), key=lambda item: item[1], reverse=True))
            if self.inventorySorting == 'down-to-up':
                self.inventory = dict(sorted(tSortInventory.items(), key=lambda item: item[1]))
            if self.inventorySorting == 'a-z':
                self.inventory = dict(sorted(tSortInventory.items()))
            if self.inventorySorting == 'z-a':
                self.inventory = dict(sorted(tSortInventory.items(), reverse=True))
            ITEM_INFO = await database.getData('items', 'names', f"'{nameItem}'")
            if ITEM_INFO[8] == 1:
                if nameItem in self.inventory:
                    if self.inventory[nameItem] > 0:
                        self.inventory[nameItem] = self.inventory[nameItem] - 1
                        if self.inventory[nameItem] <= 0:
                            self.inventory.pop(nameItem)
                        self.inventory = json.dumps(self.inventory, ensure_ascii=False)
                        await database.setUserID(self.USER[0], 'inventory', f"\'{self.inventory}\'")
                        self.USER = await database.getUserHash(f"'{self.HASH}'")
                        self.inventory = json.loads(str(self.USER[16]))
                        self.isUsedItem = 1
                        if ITEM_INFO[6] == 'Здоровье':
                            if self.USER[29] < 100:
                                newHeal = self.USER[29] + ITEM_INFO[7]
                                if newHeal > 100:
                                    newHeal = 100
                                await database.setUserID(self.USER[0], 'hp', f"'{newHeal}'")
                                self.USER = await database.getUserHash(f"'{self.HASH}'")
                        if ITEM_INFO[6] == 'Еда':
                            if self.USER[30] < 100:
                                newEat = self.USER[30] + ITEM_INFO[7]
                                if newEat > 100:
                                    newEat = 100
                                await database.setUserID(self.USER[0], 'eat', f"'{newEat}'")
                                self.USER = await database.getUserHash(f"'{self.HASH}'")
                        if ITEM_INFO[6] == 'Деньги':
                            newDollars = self.USER[6] + ITEM_INFO[7]
                            await database.setUserID(self.USER[0], 'dollars', f"'{newDollars}'")
                            self.USER = await database.getUserHash(f"'{self.HASH}'")
                        if ITEM_INFO[6] == 'Донат':
                            newDonate = self.USER[14] + ITEM_INFO[7]
                            await database.setUserID(self.USER[0], 'donate', f"'{newDonate}'")
                            self.USER = await database.getUserHash(f"'{self.HASH}'")
                        if ITEM_INFO[6] == 'Опыт':
                            newEXP = self.USER[5] + ITEM_INFO[7]
                            await database.setUserID(self.USER[0], 'exp', f"'{newEXP}'")
                            self.USER = await database.getUserHash(f"'{self.HASH}'")
                    else:
                        self.USER = await database.getUserHash(f"'{self.HASH}'")
                        self.inventory = json.loads(str(self.USER[16]))
                else:
                    self.USER = await database.getUserHash(f"'{self.HASH}'")
                    self.inventory = json.loads(str(self.USER[16]))
            count = 0
            self.inventoryCount = 0
            massive = []
            line = []
            for NAME in self.inventory:
                if count > 3:
                    massive.append(line)
                    count = 0
                    line = []
                    count = count + 1
                    self.inventoryCount = self.inventoryCount + 1
                    NAME_ITEM = await database.getDataMulti('items', 'names', f"'{NAME}'")
                    NAME_UPPER = str(NAME_ITEM[0][1]).upper()
                    HINT_INFO = ast.literal_eval(NAME_ITEM[0][5])
                    MASSIVE_ITEM = [NAME_ITEM[0][0], NAME_UPPER, NAME_ITEM[0][2], NAME_ITEM[0][3], NAME_ITEM[0][4], HINT_INFO, NAME_ITEM[0][6], NAME_ITEM[0][7], self.inventory[NAME], NAME_ITEM[0][1]]
                    line.append(MASSIVE_ITEM)
                else:
                    count = count + 1
                    self.inventoryCount = self.inventoryCount + 1
                    NAME_ITEM = await database.getDataMulti('items', 'names', f"'{NAME}'")
                    NAME_UPPER = str(NAME_ITEM[0][1]).upper()
                    HINT_INFO = ast.literal_eval(NAME_ITEM[0][5])
                    MASSIVE_ITEM = [NAME_ITEM[0][0], NAME_UPPER, NAME_ITEM[0][2], NAME_ITEM[0][3], NAME_ITEM[0][4], HINT_INFO, NAME_ITEM[0][6], NAME_ITEM[0][7], self.inventory[NAME], NAME_ITEM[0][1]]
                    line.append(MASSIVE_ITEM)
            massive.append(line)
            self.inventoryDone = massive
            tInventoryPassport = ast.literal_eval(str(self.USER[21]))
            self.inventoryLicenses = ast.literal_eval(str(self.USER[27]))
            self.inventoryPassportMax = tInventoryPassport
            self.inventoryHealth = self.USER[29] / 100 * 100
            self.inventoryEat = self.USER[30] / 100 * 100
            self.inventoryHealthInt = int(self.USER[29])
            self.inventoryEatInt = int(self.USER[30])
            if tInventoryPassport[0] == 0:
                self.inventoryPassport = '0'
            else:
                self.inventoryPassport = '1'
            if self.USER[17] != '':  # Если есть у игрока стейт, то обрабатываем его
                return await self.checkState()
            if self.isUsedItem == 1:
                return rx.toast.success("Вы использовали предмет", position='top-right')
        else:
            return rx.redirect('/')
        if self.serverOpenGame == 0:
            return rx.redirect('/we-be-right-back')