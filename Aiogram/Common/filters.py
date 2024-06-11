from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message


class ChatFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.chat_types

class IsAdmin(Filter):
    def __init__(self) -> None:
        pass
    async def __call__(self, message: Message, bot: Bot) -> bool:
        from ..Handlers.admin_handlers import ADMINS_LIST
        return message.chat.id in ADMINS_LIST

class IsNum(Filter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        try:
            text = message.text
            text = text.replace(',', '.')
            if (str(float(text)) == text) or (str(int(text)) == text):
                return True
        except Exception:
            return False