from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_eng import LEXICON_ENG
from lexicon.lexicon_es import LEXICON_ES
from lexicon.lexicon_cn import LEXICON_CN

#Главная клаиватура

def menu_kb_ru():
    kb = [
        [
            KeyboardButton(text=LEXICON_RU["profile_kb"]),
            KeyboardButton(text=LEXICON_RU["neuros_kb"])
        ],
        [
            KeyboardButton(text=LEXICON_RU["premium_kb"]),
            KeyboardButton(text=LEXICON_RU["service_kb"])
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    return keyboard

def menu_kb_eng():
    kb = [
        [
            KeyboardButton(text=LEXICON_ENG["profile_kb"]),
            KeyboardButton(text=LEXICON_ENG["neuros_kb"])
        ],
        [
            KeyboardButton(text=LEXICON_ENG["premium_kb"]),
            KeyboardButton(text=LEXICON_ENG["service_kb"])
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    return keyboard

def menu_kb_es():
    kb = [
        [
            KeyboardButton(text=LEXICON_ES["profile_kb"]),
            KeyboardButton(text=LEXICON_ES["neuros_kb"])
        ],
        [
            KeyboardButton(text=LEXICON_ES["premium_kb"]),
            KeyboardButton(text=LEXICON_ES["service_kb"])
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    return keyboard

def menu_kb_cn():
    kb = [
        [
            KeyboardButton(text=LEXICON_CN["profile_kb"]),
            KeyboardButton(text=LEXICON_CN["neuros_kb"])
        ],
        [
            KeyboardButton(text=LEXICON_CN["premium_kb"]),
            KeyboardButton(text=LEXICON_CN["service_kb"])
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    return keyboard