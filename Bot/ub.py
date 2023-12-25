import os

from pyrogram       import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from Bot.config import Config


class UBIo:
    def __init__(self, message: Message):
        self.message = message

    async def edit_caption(self, caption: str):
        try:
            await self.message.edit_caption(caption)
        except BaseException as ex:
            print(f"ERROR:root:{ex.__class__.__name__}: {ex}")

    async def edit_text(self, text: str):
        try:
            await self.message.edit_text(text)
        except BaseException as ex:
            print(f"ERROR:root:{ex.__class__.__name__}: {ex}")

    @staticmethod
    async def get_chat(chat_id: int | str) -> bool:
        try:
            chat_id = int(chat_id)
            chat_member = await UBIo.app.get_chat_member(chat_id, "me")

            return chat_member.status == ChatMemberStatus.ADMINISTRATOR
        except BaseException as ex:
            print(f"ERROR:root:{ex.__class__.__name__}: {ex}")
        return False
    
    @staticmethod
    def get_chat_history(chat_id: int | str):
        try:
            chat_id = int(chat_id)
            return UBIo.app.get_chat_history(chat_id)
        except BaseException as ex:
            print(f"ERROR:root:{ex.__class__.__name__}: {ex}")

    @staticmethod
    async def connect():
        try:
            await UBIo.app.connect()
            print(f"INFO:root:connect")
        except BaseException as ex:
            print(f"ERROR:root:{ex.__class__.__name__}: {ex}")
    
    @staticmethod
    async def start():
        try:
            await UBIo.app.start()
            print(f"INFO:root:start")
        except BaseException as ex:
            print(f"ERROR:root:{ex.__class__.__name__}: {ex}")

    @staticmethod
    def path(api_id: int | str):
        dir_ = os.path.dirname(os.path.realpath(__file__))
        dir_ = os.path.dirname(dir_)

        session_dir = os.path.join(dir_, "session")

        if not os.path.exists(session_dir):
            os.mkdir(session_dir)

        return os.path.join(session_dir, str(api_id))

    app = Client(path(Config.api_id), Config.api_id, Config.api_hash)
