"""

[ STATES ]

Бэкенд велкоме-страницы

"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
import re, ast
from rxconfig import config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class State(LS):

    tName = ''
    tSurname = ''
    tAge = ''
    tEmigrate = ''
    tImg = ''

    tIsName = True
    tIsAge = True
    tIsEmigrate = True
    tStartBonus: int

    async def set2(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-2'")

    async def set3(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-3'")

    async def set4(self):
        tPassport = ast.literal_eval(str(self.USER[21]))
        tPassport[2] = self.tName
        tPassport[3] = self.tSurname
        await database.setUserID(self.USER[0], 'passport', f"\"{tPassport}\"")
        await database.setUserID(self.USER[0], 'state', "'welcome-4'")

    async def set5(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-5'")

    async def set6(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-6'")

    async def set7(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-7'")

    async def set8(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-8'")

    async def set9(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-9'")

    async def set10(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-10'")

    async def set11(self):
        await database.setUserID(self.USER[0], 'state', "'welcome-11'")

    async def set12(self):
        await database.setUserID(self.USER[0], 'state', "''")

    def stage3(self):
        self.tName = ''
        self.tSurname = ''
        self.tIsName = True

    def stage5(self):
        self.tAge = ''
        self.tIsAge = True

    async def MAN(self):
        await database.setUserID(self.USER[0], 'sex', "'1'")

    async def WOMAN(self):
        await database.setUserID(self.USER[0], 'sex', "'2'")

    def stage6(self):
        self.tIsEmigrate = True
        self.tEmigrate = ''

    def check(self):
        if self.tName != '' and self.tSurname != '':
            self.tIsName = False
        else:
            self.tIsName = True


    def check_age(self):
        if str(self.tAge).isdigit():
            age = int(self.tAge)
            if 18 <= age < 81:
                self.tIsAge = False
            else:
                self.tIsAge = True
        else:
            self.tIsAge = True

    async def SETAGEDB(self):
        await database.setUserID(self.USER[0], 'age', f"'{int(self.tAge)}'")

    def Emigrate1(self):
        self.tIsEmigrate = False
        self.tEmigrate = '1'

    def Emigrate2(self):
        self.tIsEmigrate = False
        self.tEmigrate = '2'

    def Emigrate3(self):
        self.tIsEmigrate = False
        self.tEmigrate = '3'

    def Emigrate4(self):
        self.tIsEmigrate = False
        self.tEmigrate = '4'

    def getBonusDollars(self):
        Temporary = str(self.SERVER[5])
        Temporary = ast.literal_eval(Temporary)
        self.tStartBonus = Temporary[2]

    @rx.event
    async def handle_upload(
            self, files: list[rx.UploadFile]
    ):
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.tImg = file.filename
            await database.setUserID(self.USER[0], 'avatar', f"'{self.tImg}'")
            self.USER = await database.getUserHash(f"'{self.HASH}'")


    def CheckStage1(self):
        if self.USER[18] != 'welcome-1':
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage2(self):
        if self.USER[18] != 'welcome-2':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage3(self):
        if self.USER[18] != 'welcome-3':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage4(self):
        if self.USER[18] != 'welcome-4':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage5(self):
        if self.USER[18] != 'welcome-5':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage6(self):
        if self.USER[18] != 'welcome-6':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage7(self):
        if self.USER[18] != 'welcome-7':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage8(self):
        if self.USER[18] != 'welcome-8':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage9(self):
        if self.USER[18] != 'welcome-9':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage10(self):
        if self.USER[18] != 'welcome-10':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    def CheckStage11(self):
        if self.USER[18] != 'welcome-11':
            if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
            if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
            if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
            if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
            if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
            if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
            if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
            if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
            if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
            if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')