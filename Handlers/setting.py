import re

from aiogram            import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from pyrogram.types import Message

from Accest.markups     import Markups
from Accest.translation import tr

from Bot.bot import Bot_
from Bot.ub  import UBIo



class FormSetting(StatesGroup):
    add_channel = State()


class Setting:
    # --> /start
    # <-- tr.bt1 - ["Добавить канналы", "Изменить юзернейм", "Запустить"]
    async def start(message: types.Message, state: FSMContext):
        await state.finish()
        await Bot_(message).answer(tr.t1, reply_markup = Markups.main)

    # --> tr.bt1[0]
    # <-- tr.t2 - """
#Введите id каннала старый юзернейм и новый юзернейм через 
#пробел пример: 
#-1001000001 new_test1
#-1001000002 new_test2
#"""
    async def send_add_channel(message: types.Message, state: FSMContext):
        await Bot_(message).answer(tr.t2, reply_markup = Markups.main)
        await FormSetting.add_channel.set()

    # --> types.ContentType.TEXT - FormSetting.add_channel
    async def add_channel(message: types.Message, state: FSMContext):
        await state.finish()
        channels = re.findall(r"(-100\d+) (\w+)", message.text)
        
        if not channels:
            await Bot_(message).answer(tr.et1)
            return await Setting.send_add_channel(message, state)
        
        for channel_id, new_username in channels:
            if not await UBIo.get_chat(channel_id):
                await Bot_(message).answer(tr.et2.format(channel_id))
                continue
            
            await Bot_(message).answer(tr.t7.format(channel_id))

            async for msg in UBIo.app.get_chat_history(int(channel_id)):
                msg: Message = msg

                if msg.caption:
                    await UBIo(msg).edit_caption(Setting.replace(msg.caption, new_username))

                elif msg.text:
                    await UBIo(msg).edit_text(Setting.replace(msg.text, new_username))

            await Bot_(message).answer(tr.t8.format(channel_id))
            
        await Bot_(message).answer(tr.t9)

    def replace(text: str, new_username: str):
        old_username = re.search(r"@(\w+)", text)

        if old_username is None:
            return text.html

        return text.html.replace(old_username.group(1), new_username)