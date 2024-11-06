from aiogram import Router, F

from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext

from ikb.ikb import choose_leng, ikb_premium_ru, ikb_premium_eng, ikb_premium_es, ikb_premium_cn, tokens_ikb_ru, tokens_ikb_eng, tokens_ikb_es, tokens_ikb_cn, profile_ikb_ru, photo_text_ru, photo_text_eng, photo_text_es, photo_text_cn, profile_ikb_eng, profile_ikb_es, profile_ikb_cn, tokens_ikb_ru_prem, tokens_ikb_eng_prem, tokens_ikb_es_prem, tokens_ikb_cn_prem, change_mode_ru, change_mode_eng, change_mode_es, change_mode_cn
from keyboard.kb import menu_kb_ru, menu_kb_eng, menu_kb_es, menu_kb_cn
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_eng import LEXICON_ENG
from lexicon.lexicon_es import LEXICON_ES
from lexicon.lexicon_cn import LEXICON_CN
from db.db import lingo, check_user, user_name, user_id, lingo, asks, user_tokens, premium_days, neuro, tokens_plus_update, premium_counter_us
from db.db_premium import check_user_prem, user_in_prem, check_user_prem, days_update_plus
from .callback_handlers import FSMForm, default_state

router = Router()

#Функция /start
@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    username = message.from_user.username
    uid = message.from_user.id
    if username in ["Kseny_7", "APPROXIMATE2ZERO", "anyutka_cutie", "aynamiirei", "CODE_PIZZA", "ManaceManace"]:
        tokens_plus_update(uid, 1000)
        if check_user_prem(uid) == False:
            user_in_prem(uid, 1000)
    if check_user(uid) == True:
        if lingo(uid) == "RU":
            await message.answer(
            LEXICON_RU["menu"],
            reply_markup=menu_kb_ru()
            )
            await message.answer(
                "✅Бот перезапущен!"
            )
        elif lingo(uid) == "ENG":
            await message.answer(
                LEXICON_ENG["menu"],
                reply_markup=menu_kb_eng()
            )
            await message.answer(
                "✅Bot restarted!"
            )
        elif lingo(uid) == "ES":
            await message.answer(
                LEXICON_ES["menu"],
                reply_markup=menu_kb_es()
            )
            await message.answer(
                "✅¡Bot relanzado!"
            )
        elif lingo(uid) == "CN":
            await message.answer(
                LEXICON_CN["menu"],
                reply_markup=menu_kb_cn()
            )
            await message.answer(
                "✅机器人已重新启动"
            )
    elif check_user(uid) == False:
        await message.answer(
            LEXICON_RU["choose_lingo"],
            reply_markup=choose_leng()
        )
    await state.set_state(default_state)

#Функция /help
@router.message(Command("help"))
async def help_func(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "RU":
        await message.answer(
            "🗣Связь с администрацией @Kseny_7"
        )
    elif lingo(uid) == "ENG":
        await message.answer(
            "🗣Communication with the administration @Kseny_7"
        )
    elif lingo(uid) == "ES":
        await message.answer(
            "🗣Enlace con la administración @Kseny_7"
        )
    elif lingo(uid) == "CN":
        await message.answer(
            "🗣与行政部门联络 @Kseny_7"
        )

#Функция /premium
@router.message(Command("premium"))
async def buy_premium(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "RU":
        await message.answer(
            LEXICON_RU["premium"],
            reply_markup=ikb_premium_ru()
        )
    elif lingo(uid) == "ENG":
        await message.answer(
            LEXICON_ENG["premium"],
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await message.answer(
            LEXICON_ES["premium"],
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await message.answer(
            LEXICON_CN["premium"],
            reply_markup=ikb_premium_cn()
        )

@router.message(F.text.lower() == "💎премиум")
async def buy_premium(message: Message):
    await message.answer(
            LEXICON_RU["premium"],
            reply_markup=ikb_premium_ru()
        )

@router.message(F.text.lower() == "💎premium")
async def buy_premium(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "ENG":
        await message.answer(
            LEXICON_ENG["premium"],
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await message.answer(
            LEXICON_ES["premium"],
            reply_markup=ikb_premium_es()
        )

@router.message(F.text.lower() == "💎高級訂閱")
async def buy_premium(message: Message):
    await message.answer(
            LEXICON_CN["premium"],
            reply_markup=ikb_premium_cn()
        )

#Функция /tokens
@router.message(Command("tokens"))
async def buy_tokens(message: Message, state: FSMContext):
    uid = message.from_user.id
    if check_user_prem(uid) == False:
        if lingo(uid) == "RU":
            await message.answer(
                "Выберите желаемое количество токенов",
                reply_markup=tokens_ikb_ru()
            )
        elif lingo(uid) == "ENG":
            await message.answer(
                "Select the desired number of tokens",
                reply_markup=tokens_ikb_eng()
            )
        elif lingo(uid) == "ES":
            await message.answer(
                "Seleccione el número de fichas deseado",
                reply_markup=tokens_ikb_es()
            )
        elif lingo(uid) == "CN":
            await message.answer(
                "選擇所需的代幣數量",
                reply_markup=tokens_ikb_cn()
            )
    else:
        if lingo(uid) == "RU":
            await message.answer(
                "Выберите желаемое количество токенов",
                reply_markup=tokens_ikb_ru_prem()
            )
        elif lingo(uid) == "ENG":
            await message.answer(
                "Select the desired number of tokens",
                reply_markup=tokens_ikb_eng_prem()
            )
        elif lingo(uid) == "ES":
            await message.answer(
                "Seleccione el número de fichas deseado",
                reply_markup=tokens_ikb_es_prem()
            )
        elif lingo(uid) == "CN":
            await message.answer(
                "選擇所需的代幣數量",
                reply_markup=tokens_ikb_cn_prem()
            )
    await state.set_state(FSMForm.tokens)

#Функция /language
@router.message(Command("language"))
async def language(message: Message):
    await message.answer(
    LEXICON_RU["choose_lingo"],
    reply_markup=choose_leng()
    )

#Функция /profile/профиль
@router.message(Command("profile"))
async def command_profile(message: Message):
    uid = message.from_user.id
    username = message.from_user.username
    if username in ["Kseny_7", "APPROXIMATE2ZERO", "anyutka_cutie", "aynamiirei", "CODE_PIZZA", "ManaceManace"]:
        days_update_plus(uid)
        premium_counter_us(uid)
    if lingo(uid) == "RU":
        await message.answer(
            f"👤Добро пожаловать в ваш профиль: {message.from_user.full_name}\n├Ваш юзернейм: <code>@{user_name(uid)}</code>\n├Ваш id: <code>{user_id(uid)}</code>\n├Нейросеть: {neuro(uid)}\n└Вопросов задано: {asks(uid)}\n\n💰Токенов: {user_tokens(uid)}\n└Премиум: {premium_days(uid)} дн.",
            reply_markup=profile_ikb_ru(),
            parse_mode=ParseMode.HTML
        )
    elif lingo(uid) == "ENG":
        await message.answer(
            f"👤Welcome to your profile: {message.from_user.full_name}\n├Your username: <code>@{user_name(uid)}</code>\n├Your id: <code>{user_id(uid)}</code>\n├AI: {neuro(uid)}\n└Questions asked: {asks(uid)}\n\n💰Tokens: {user_tokens(uid)}\n└Premium: {premium_days(uid)} days",
            reply_markup=profile_ikb_eng(),
            parse_mode=ParseMode.HTML
        )
    elif lingo(uid) == "ES":
        await message.answer(
            f"👤Bienvenido a tu perfil: {message.from_user.full_name}\n├Tu nombre de usuario: <code>@{user_name(uid)}</code>\n├Su id: <code>{user_id(uid)}</code>\n├AI: {neuro(uid)}\n└Preguntas formuladas: {asks(uid)}\n\n💰Fichas: {user_tokens(uid)}\n└Premium: {premium_days(uid)} días",
            reply_markup=profile_ikb_es(),
            parse_mode=ParseMode.HTML
        )
    elif lingo(uid) == "CN":
        await message.answer(
            f"👤欢迎访问您的个人资料: {message.from_user.full_name}\n├您的用户名: <code>@{user_name(uid)}</code>\n├您的 id: <code>{user_id(uid)}</code>\n├神经网络: {neuro(uid)}\n└问题数量: {asks(uid)}\n\n💰令牌: {user_tokens(uid)}\n└溢价: {premium_days(uid)} 天数",
            reply_markup=profile_ikb_cn(),
            parse_mode=ParseMode.HTML
        )

@router.message(F.text.lower() == "👤профиль")
async def command_profile(message: Message):
    uid = message.from_user.id
    await message.answer(
        f"👤Добро пожаловать в ваш профиль: {message.from_user.full_name}\n├Ваш юзернейм: <code>@{user_name(uid)}</code>\n├Ваш id: <code>{user_id(uid)}</code>\n├Нейросеть: {neuro(uid)}\n└Вопросов задано: {asks(uid)}\n\n💰Токенов: {user_tokens(uid)}\n└Премиум: {premium_days(uid)} дн.",
        reply_markup=profile_ikb_ru(),
        parse_mode=ParseMode.HTML
    )

@router.message(F.text.lower() == "👤profile")
async def command_profile(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "ENG":
        await message.answer(
            f"👤Welcome to your profile: {message.from_user.full_name}\n├Your username: <code>@{user_name(uid)}</code>\n├Your id: <code>{user_id(uid)}</code>\n├AI: {neuro(uid)}\n└Questions asked: {asks(uid)}\n\n💰Tokens: {user_tokens(uid)}\n└Premium: {premium_days(uid)} days",
            reply_markup=profile_ikb_eng(),
            parse_mode=ParseMode.HTML
        )
    else:
        lingo(uid) == "ES"
        await message.answer(
            f"👤Bienvenido a tu perfil: {message.from_user.full_name}\n├Tu nombre de usuario: <code>@{user_name(uid)}</code>\n├Su id: <code>{user_id(uid)}</code>\n├AI: {neuro(uid)}\n└Preguntas formuladas: {asks(uid)}\n\n💰Fichas: {user_tokens(uid)}\n└Premium: {premium_days(uid)} días",
            reply_markup=profile_ikb_es(),
            parse_mode=ParseMode.HTML
        )

@router.message(F.text.lower() == "👤檔案")
async def command_profile(message: Message):
        uid = message.from_user.id
        await message.answer(
        f"👤欢迎访问您的个人资料: {message.from_user.full_name}\n├您的用户名: <code>@{user_name(uid)}</code>\n├您的 id: <code>{user_id(uid)}</code>\n├神经网络: {neuro(uid)}\n└问题数量: {asks(uid)}\n\n💰令牌: {user_tokens(uid)}\n└溢价: {premium_days(uid)} 天数",
        reply_markup=profile_ikb_cn(),
        parse_mode=ParseMode.HTML
        )

#Нейронки

@router.message(Command("neuroseti"))
async def neuro_ai(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "RU":
        await message.answer(
            "Что бы вы хотели сгенерировать?",
            reply_markup=photo_text_ru()
        )
    elif lingo(uid) == "ENG":
        await message.answer(
            "What would you like to generate?",
            reply_markup=photo_text_eng()
        )
    elif lingo(uid) == "ES":
        await message.answer(
            "¿Qué le gustaría generar?",
            reply_markup=photo_text_es()
        )

    elif lingo(uid) == "CN":
        await message.answer(
            "您希望产生什么?",
            reply_markup=photo_text_cn()
        )

@router.message(F.text.lower() == "📋сервисы")
async def service_ru(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "RU":
        await message.answer(
            "Что бы вы хотели сгенерировать?",
            reply_markup=change_mode_ru()
        )

@router.message(F.text.lower() == "📋services")
async def ser_eng(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "ENG":
        await message.answer(
            "What you want to do?",
            reply_markup=change_mode_eng()
        )


@router.message(F.text.lower() == "📋servicios")
async def ser_es(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "ES":
        await message.answer(
            "¿Qué quieres hacer?",
            reply_markup=change_mode_es()
        )


@router.message(F.text.lower() == "📋服務")
async def ser_cn(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "CN":
        await message.answer(
            "你想做什么?",
            reply_markup=change_mode_cn()
        )

@router.message(F.text.lower() == "👾нейросети")
async def neuro_ai(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "RU":
        await message.answer(
            "Что бы вы хотели сгенерировать?",
            reply_markup=photo_text_ru()
        )

@router.message(F.text.lower() == "👾ai")
async def ai(message: Message):
    uid = message.from_user.id
    if lingo(uid) == "ENG":
        await message.answer(
            "What would you like to generate?",
            reply_markup=photo_text_eng()
        )
    else:
        lingo(uid) == "ES"
        await message.answer(
            "¿Qué le gustaría generar?",
            reply_markup=photo_text_es()
        )

@router.message(F.text.lower() == "👾神經網路")
async def ai_cn(message: Message):
    await message.answer(
        "您希望产生什么?",
        reply_markup=photo_text_cn()
    )