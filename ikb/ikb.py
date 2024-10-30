from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.filters.callback_data import CallbackData

from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_eng import LEXICON_ENG
from lexicon.lexicon_es import LEXICON_ES
from lexicon.lexicon_cn import LEXICON_CN

from db.db_pag import pages, pages_count

class Pagination_ru(CallbackData, prefix="pag_ru"):
    page: int

class Pagination_eng(CallbackData, prefix="pag_eng"):
    page: int

class Pagination_es(CallbackData, prefix="pag_es"):
    page: int

class Pagination_cn(CallbackData, prefix="pag_cn"):
    page: int

#Кнопка назад

def ikb_back_ru():

    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["back"], callback_data="back_one")
        ]

    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def ikb_back_eng():

    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ENG["back"], callback_data="back_one")
        ]

    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def ikb_back_es():

    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ES["back"], callback_data="back_one")
        ]

    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def ikb_back_cn():

    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_CN["back"], callback_data="back_one")
        ]

    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Проверка подписки

def sub_ikb_ru():
    
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["sub"], url="https://t.me/+8uvdYCpsuxJjNzcy"),
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["sub_ready"], callback_data="check_ru")
        ]
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

def sub_ikb_eng():
    
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ENG["sub"], url="https://t.me/+8uvdYCpsuxJjNzcy"),
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["sub_ready"], callback_data="check_eng")
        ]
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

def sub_ikb_esp():
    
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ES["sub"], url="https://t.me/+8uvdYCpsuxJjNzcy"),
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["sub_ready"], callback_data="check_esp")
        ]
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

def sub_ikb_cn():
    
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_CN["sub"], url="https://t.me/+8uvdYCpsuxJjNzcy"),
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["sub_ready"], callback_data="check_cn")
        ]
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

#Языки

def choose_leng():

    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["ru_btn"], callback_data="ru_kb"),
            InlineKeyboardButton(text=LEXICON_RU["eng_btn"], callback_data="eng_kb"),
            InlineKeyboardButton(text=LEXICON_RU["esp_btn"], callback_data="esp_kb"),
            InlineKeyboardButton(text=LEXICON_RU["cn_btn"], callback_data="cn_kb")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Покупка премиум

def ikb_premium_ru():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["buy"], callback_data="buy"),
            InlineKeyboardButton(text=LEXICON_RU["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def ikb_premium_eng():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ENG["buy"], callback_data="buy"),
            InlineKeyboardButton(text=LEXICON_ENG["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def ikb_premium_es():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ES["buy"], callback_data="buy"),
            InlineKeyboardButton(text=LEXICON_ES["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def ikb_premium_cn():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_CN["buy"], callback_data="buy"),
            InlineKeyboardButton(text=LEXICON_CN["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Покупка токенов

def tokens_ikb_ru():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["10k"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["30k"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["150k"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["500k"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def tokens_ikb_ru_prem():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["10k_prem"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k_prem"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["30k_prem"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["150k_prem"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["500k_prem"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def tokens_ikb_eng():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["10k"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["30k"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["150k"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["500k"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def tokens_ikb_eng_prem():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["10k_prem"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k_prem"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["30k_prem"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["150k_prem"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["500k_prem"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def tokens_ikb_es():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["10k"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["30k"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["150k"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["500k"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def tokens_ikb_es_prem():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["10k_prem"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k_prem"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["30k_prem"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["150k_prem"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["500k_prem"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def tokens_ikb_cn():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["10k"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["30k"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["150k"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["500k"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def tokens_ikb_cn_prem():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["10k_prem"], callback_data="10k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["20k_prem"], callback_data="20k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["30k_prem"], callback_data="30k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["150k_prem"], callback_data="150k")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["500k_prem"], callback_data="500k")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Покупка токенов
def buy_tokens_ru():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def buy_tokens_eng():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ENG["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def buy_tokens_es():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ES["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def buy_tokens_cn():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_CN["check_pay"], callback_data="check")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["back"], callback_data="back")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Клавиатура профиля
def profile_ikb_ru():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_RU["premium_kb"], callback_data="premium"),
            InlineKeyboardButton(text=LEXICON_RU["tokens"], callback_data="tokens")
        ],
        [
            InlineKeyboardButton(text=LEXICON_RU["help"], callback_data="help"),
            InlineKeyboardButton(text=LEXICON_RU["support"], url="https://t.me/Kseny_7")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def profile_ikb_eng():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ENG["premium_kb"], callback_data="premium"),
            InlineKeyboardButton(text=LEXICON_ENG["tokens"], callback_data="tokens")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ENG["help"], callback_data="help"),
            InlineKeyboardButton(text=LEXICON_ENG["support"], url="https://t.me/Kseny_7")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def profile_ikb_es():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_ES["premium_kb"], callback_data="premium"),
            InlineKeyboardButton(text=LEXICON_ES["tokens"], callback_data="tokens")
        ],
        [
            InlineKeyboardButton(text=LEXICON_ES["help"], callback_data="help"),
            InlineKeyboardButton(text=LEXICON_ES["support"], url="https://t.me/Kseny_7")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def profile_ikb_cn():
    ikb = [
        [
            InlineKeyboardButton(text=LEXICON_CN["premium_kb"], callback_data="premium"),
            InlineKeyboardButton(text=LEXICON_CN["tokens"], callback_data="tokens")
        ],
        [
            InlineKeyboardButton(text=LEXICON_CN["help"], callback_data="help"),
            InlineKeyboardButton(text=LEXICON_CN["support"], url="https://t.me/Kseny_7")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Фото-текст
def photo_text_ru():
    ikb = [
        [
            InlineKeyboardButton(text="💬Текст", callback_data="text_ru")
        ],
        [
            InlineKeyboardButton(text="📷Фото", callback_data="photo_ru")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def photo_text_eng():
    ikb = [
        [
            InlineKeyboardButton(text="💬Text", callback_data="text_eng")
        ],
        [
            InlineKeyboardButton(text="📷Photo", callback_data="photo_eng")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def photo_text_es():
    ikb = [
        [
            InlineKeyboardButton(text="💬Texto", callback_data="text_es")
        ],
        [
            InlineKeyboardButton(text="📷Foto", callback_data="photo_es")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def photo_text_cn():
    ikb = [
        [
            InlineKeyboardButton(text="💬文本", callback_data="text_cn")
        ],
        [
            InlineKeyboardButton(text="📷照片", callback_data="photo_cn")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Фото повтор

def photo_again_ru():
    ikb = [
        [
            InlineKeyboardButton(text="🔁Повторить генерацию", callback_data="photo_ru")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def photo_again_eng():
    ikb = [
        [
            InlineKeyboardButton(text="🔁Repeat generation", callback_data="photo_eng")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def photo_again_es():
    ikb = [
        [
            InlineKeyboardButton(text="🔁Generación repetida", callback_data="photo_es")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def photo_again_cn():
    ikb = [
        [
            InlineKeyboardButton(text="🔁重复生成", callback_data="photo_cn")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard


#Пагинация
def get_paginated_kb_ru(page: int = 1) -> InlineKeyboardMarkup:
    ikb = [
            [
                InlineKeyboardButton(text="⬅️", callback_data=Pagination_ru(page=page - 1).pack()),
                InlineKeyboardButton(text=f"🟢{pages(page)}/{pages_count()}", callback_data="None"),
                InlineKeyboardButton(text="➡️", callback_data=Pagination_ru(page=page + 1).pack())
            ]
            ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def get_paginated_kb_eng(page: int = 1) -> InlineKeyboardMarkup:
    ikb = [
            [
                InlineKeyboardButton(text="⬅️", callback_data=Pagination_eng(page=page - 1).pack()),
                InlineKeyboardButton(text=f"🟢{pages(page)}/{pages_count()}", callback_data="None"),
                InlineKeyboardButton(text="➡️", callback_data=Pagination_eng(page=page + 1).pack())
            ]
            ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def get_paginated_kb_es(page: int = 1) -> InlineKeyboardMarkup:
    ikb = [
            [
                InlineKeyboardButton(text="⬅️", callback_data=Pagination_es(page=page - 1).pack()),
                InlineKeyboardButton(text=f"🟢{pages(page)}/{pages_count()}", callback_data="None"),
                InlineKeyboardButton(text="➡️", callback_data=Pagination_es(page=page + 1).pack())
            ]
            ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def get_paginated_kb_cn(page: int = 1) -> InlineKeyboardMarkup:
    ikb = [
            [
                InlineKeyboardButton(text="⬅️", callback_data=Pagination_cn(page=page - 1).pack()),
                InlineKeyboardButton(text=f"🟢{pages(page)}/{pages_count()}", callback_data="None"),
                InlineKeyboardButton(text="➡️", callback_data=Pagination_cn(page=page + 1).pack())
            ]
            ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Режимы
def change_mode_ru():
    ikb = [
    [
        InlineKeyboardButton(text=LEXICON_RU["no_mode"], callback_data="1")
    ],
    [
        InlineKeyboardButton(text=LEXICON_RU["Essay"], callback_data="2")
    ],
    [
        InlineKeyboardButton(text=LEXICON_RU["Coursework"], callback_data="3")
    ],
    [
        InlineKeyboardButton(text=LEXICON_RU["Seo"], callback_data="4")
    ],
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

def change_mode_eng():
    ikb = [
    [
        InlineKeyboardButton(text=LEXICON_ENG["no_mode"], callback_data="1")
    ],
    [
        InlineKeyboardButton(text=LEXICON_ENG["Essay"], callback_data="2")
    ],
    [
        InlineKeyboardButton(text=LEXICON_ENG["Coursework"], callback_data="3")
    ],
    [
        InlineKeyboardButton(text=LEXICON_ENG["Seo"], callback_data="4")
    ],
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

def change_mode_es():
    ikb = [
    [
        InlineKeyboardButton(text=LEXICON_ES["no_mode"], callback_data="1")
    ],
    [
        InlineKeyboardButton(text=LEXICON_ES["Essay"], callback_data="2")
    ],
    [
        InlineKeyboardButton(text=LEXICON_ES["Coursework"], callback_data="3")
    ],
    [
        InlineKeyboardButton(text=LEXICON_ES["Seo"], callback_data="4")
    ],
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

def change_mode_cn():
    ikb = [
    [
        InlineKeyboardButton(text=LEXICON_CN["no_mode"], callback_data="1")
    ],
    [
        InlineKeyboardButton(text=LEXICON_CN["Essay"], callback_data="2")
    ],
    [
        InlineKeyboardButton(text=LEXICON_CN["Coursework"], callback_data="3")
    ],
    [
        InlineKeyboardButton(text=LEXICON_CN["Seo"], callback_data="4")
    ],
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord