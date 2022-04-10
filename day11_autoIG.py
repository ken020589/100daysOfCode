##!/usr/bin/env python
#day11 instabot

from instabot import Bot
bot = Bot()
user = str(input('your username: '))
passwd = str(input('your password: '))
bot.login(username=user,password=passwd)

bot.upload_photo('yobammarere.jpg',caption='yobammarere!!! test Auto po on IG')

bot.follow('elonrmuskk')
