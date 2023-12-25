from aiogram import types

from Accest.translation import tr

from Bot.bot import Bot_

from Handlers.setting import Setting, FormSetting


Bot_.dp.register_message_handler(
    Setting.start,
    commands = "start",
    state = "*"
)

Bot_.dp.register_message_handler(
    Setting.send_add_channel,
    regexp = tr.t3,
    content_types = types.ContentType.TEXT,
    state = "*"
)


Bot_.dp.register_message_handler(
    Setting.add_channel,
    content_types = types.ContentType.TEXT,
    state = FormSetting.add_channel
)