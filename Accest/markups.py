from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from .translation import tr

class Markups:
    def markup(bt: list[str] | str | int = None) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        
        if not isinstance(bt, list):
            bt = [bt]

        markup.row(*[KeyboardButton(j) for j in bt])

        return markup

    main = markup(tr.bt1)