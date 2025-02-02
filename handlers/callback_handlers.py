import random
import string

from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaVideo
from aiogram.filters import StateFilter
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.markdown import hlink
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state

from yoomoney import Quickpay, Client

from ikb.ikb import sub_ikb_ru, sub_ikb_eng, sub_ikb_esp, sub_ikb_cn, ikb_premium_ru, ikb_premium_eng, ikb_premium_es, ikb_premium_cn, ikb_back_ru, ikb_back_eng, ikb_back_es, ikb_back_cn, tokens_ikb_ru, tokens_ikb_eng, tokens_ikb_es, tokens_ikb_cn, get_paginated_kb_ru, get_paginated_kb_eng, get_paginated_kb_es, get_paginated_kb_cn, buy_tokens_ru, buy_tokens_eng, buy_tokens_es, buy_tokens_cn, choose_luma_ikb_ru_standard, choose_luma_ikb_ru_pro, choose_luma_ikb_eng_pro, choose_luma_ikb_eng_standard, choose_luma_ikb_es_pro, choose_luma_ikb_es_standard, choose_luma_ikb_cn_pro, choose_luma_ikb_cn_standard, choose_udio_ikb_ru, choose_udio_ikb_eng, choose_udio_ikb_es, choose_udio_ikb_cn, Pagination_ru, Pagination_eng, Pagination_es, Pagination_cn
from db.db import user_in_db, check_user, lingo, user_lingo, update_ai, tokens_plus_update, set_mode
from db.db_pag import title, stat, stat_eng, stat_es, stat_cn
from db.db_premium import check_user_prem, user_in_prem
from db.luma import check_user_in_luma, add_user_in_luma
from db.udio import add_user_in_udio, check_user_in_udio
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_eng import LEXICON_ENG
from lexicon.lexicon_es import LEXICON_ES
from lexicon.lexicon_cn import LEXICON_CN
from .payment import TOKEN_API_U
from keyboard.kb import menu_kb_ru, menu_kb_eng, menu_kb_es, menu_kb_cn

router = Router()

user_do_buy: dict[int, dict[str]] = {}
premium_timer: dict[int, dict[int], dict[int]] = {}
user_page: dict[int] = {}
tokens: dict[int] = {}
days_luma: dict[int, dict[int]] = {}
luma_times: dict[int, dict[int]] = {}
kling_version: dict[int, dict[int]] = {}
kling_sec: dict[int, dict[int]] = {}

client = Client(TOKEN_API_U)

class FSMForm(StatesGroup):
    pre_menu=State() #Покупка премиум
    menu_pay=State() #Меню со страницей оплаты
    tokens=State() #Назад в меню с токенами
    luma=State()
    udio = State()


#Выбор языка + сохранение данных
@router.callback_query(F.data == "ru_kb")
async def ru_lingo(callback: CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    user_name = callback.from_user.full_name
    user_ling = "RU"
    user_balance_tokens = 10000
    user_asks = 0
    neuronetwork = None
    premium_days = 0
    check = check_user(user_id)
    if check == False:
        user_in_db(user_id=user_id, username=username, user_name=user_name, user_ling=user_ling, user_balance_tokens=user_balance_tokens, user_asks=user_asks, neuronetwork=neuronetwork, premium_days=premium_days)
        await callback.message.edit_text(
        f"Привет <b>{callback.from_user.full_name}</b>, я – <b>Ник</b> – генератор твоих идей!\n\nЧтобы продолжить работу, подпишись на мой канал, который принесет тебе много новых знаний!",
        parse_mode = ParseMode.HTML,
        reply_markup=sub_ikb_ru()
    )
    else:
        user_lingo(user_id, user_ling)
        await callback.message.answer(
        LEXICON_RU["ling"],
        reply_markup=menu_kb_ru()
    )

@router.callback_query(F.data == "eng_kb")
async def ru_lingo(callback: CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    user_name = callback.from_user.full_name
    user_ling = "ENG"
    user_balance_tokens = 10000
    user_asks = 0
    neuronetwork = None
    premium_days = 0
    check = check_user(user_id)
    if check == False:
        user_in_db(user_id=user_id, username=username, user_name=user_name, user_ling=user_ling, user_balance_tokens=user_balance_tokens, user_asks=user_asks, neuronetwork=neuronetwork, premium_days=premium_days)
        await callback.message.edit_text(
        f"Hello <b>{callback.from_user.full_name}</b>, my name – <b>Nick</b> – I'm generator of your ideas\n\nFor continue work, sunscribe on my channel, you will find a lot of new knoweldges there!",
        parse_mode = ParseMode.HTML,
        reply_markup=sub_ikb_eng()
    )
    else:
        user_lingo(user_id, user_ling)
        await callback.message.answer(
        LEXICON_ENG["ling"],
        reply_markup=menu_kb_eng())

@router.callback_query(F.data == "esp_kb")
async def ru_lingo(callback: CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    user_name = callback.from_user.full_name
    user_ling = "ES"
    user_balance_tokens = 10000
    user_asks = 0
    neuronetwork = None
    premium_days = 0
    check = check_user(user_id)
    if check == False:
        user_in_db(user_id=user_id, username=username, user_name=user_name, user_ling=user_ling, user_balance_tokens=user_balance_tokens, user_asks=user_asks, neuronetwork=neuronetwork, premium_days=premium_days)
        await callback.message.edit_text(
        f"Hola <b>{callback.from_user.full_name}</b>, soy <b>Nick</b> – ¡el generador de tus ideas!\n\n¡Para continuar, suscríbete a mi canal que te traerá un montón de nuevos conocimientos!",
        parse_mode = ParseMode.HTML,
        reply_markup=sub_ikb_esp()
    )
    else:
        user_lingo(user_id, user_ling)
        await callback.message.answer(
        LEXICON_ES["ling"],
        reply_markup=menu_kb_es())

@router.callback_query(F.data == "cn_kb")
async def ru_lingo(callback: CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    user_name = callback.from_user.full_name
    user_ling = "CN"
    user_balance_tokens = 10000
    user_asks = 0
    neuronetwork = None
    premium_days = 0
    check = check_user(user_id)
    if check == False:
        user_in_db(user_id=user_id, username=username, user_name=user_name, user_ling=user_ling, user_balance_tokens=user_balance_tokens, user_asks=user_asks, neuronetwork=neuronetwork, premium_days=premium_days)
        await callback.message.edit_text(
        f"您好 <b>{callback.from_user.full_name}</b>, 我是<b>尼克</b> – 您的创意生成器!\n\n要继续观看，请订阅我的频道，它将为您带来许多新知识！",
        parse_mode = ParseMode.HTML,
        reply_markup=sub_ikb_cn()
    )
    else:
        user_lingo(user_id, user_ling)
        await callback.message.answer(
        LEXICON_CN["ling"],
        reply_markup=menu_kb_cn())

#Покупка премиум
@router.callback_query(F.data == "buy")
async def buy_premium(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    num1 = random.randint(1, 2147483647)
    num2 = random.randint(-2147483647, -1)
    num3 = (num1 + num2) * 3
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    invoice = Quickpay(
            receiver="410012465765599",
            quickpay_form="shop",
            targets="Sponsor",
            paymentType="SB",
            sum=499,
            label=num3
        )
    if lingo(uid) == "RU":
        await callback.message.edit_text(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=ikb_premium_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(FSMForm.pre_menu)

@router.callback_query(F.data == "check", StateFilter(FSMForm.pre_menu))
async def check(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    premium_days = 30
    try:
        history = client.operation_history(label = user_do_buy[callback.from_user.id]["labl"])
        for operation in history.operations:
            stata = operation.status
        try:
            if stata == "success":
                check_user_prem(uid)
                if check_user_prem(uid) == False:
                    user_in_prem(user_id = uid, days = premium_days)
                    if lingo(uid) == "RU":
                        await callback.message.edit_text(
                            LEXICON_RU["pay_yes"]
                        )
                    elif lingo(uid) == "ENG":
                        await callback.message.edit_text(
                            LEXICON_ENG["pay_yes"]
                        )
                    elif lingo(uid) == "ES":
                        await callback.message.edit_text(
                            LEXICON_ES["pay_yes"]
                        )
                    elif lingo(uid) == "CN":
                        await callback.message.edit_text(
                            LEXICON_CN["pay_yes"]
                        )
            else:
                    if lingo(uid) == "RU":
                        await callback.message.edit_text(
                            LEXICON_RU["pay_yes"]
                        )
                    elif lingo(uid) == "ENG":
                        await callback.message.edit_text(
                            LEXICON_ENG["pay_yes"]
                        )
                    elif lingo(uid) == "ES":
                        await callback.message.edit_text(
                            LEXICON_ES["pay_yes"]
                        )
                    elif lingo(uid) == "CN":
                        await callback.message.edit_text(
                            LEXICON_CN["pay_yes"]
                        )
        except UnboundLocalError:
            if lingo(uid) == "RU":
                await callback.message.edit_text(
                    LEXICON_RU["pay_no"],
                    reply_markup=ikb_back_ru()
                )
            elif lingo(uid) == "ENG":
                await callback.message.edit_text(
                    LEXICON_ENG["pay_no"],
                    reply_markup=ikb_back_eng()
                )
            elif lingo(uid) == "ES":
                await callback.message.edit_text(
                    LEXICON_ES["pay_no"],
                    reply_markup=ikb_back_es()
                )
            elif lingo(uid) == "CN":
                await callback.message.edit_text(
                    LEXICON_CN["pay_no"],
                    reply_markup=ikb_back_cn()
                )
    except KeyError:
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                LEXICON_RU["pay_no"],
                reply_markup=ikb_back_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                LEXICON_ENG["pay_no"],
                reply_markup=ikb_back_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                LEXICON_ES["pay_no"],
                reply_markup=ikb_back_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                LEXICON_CN["pay_no"],
                reply_markup=ikb_back_cn()
            )
    await state.set_state(FSMForm.pre_menu)

@router.callback_query(F.data == "check", StateFilter(FSMForm.tokens))
async def check(callback: CallbackQuery, state: FSMContext): 
    uid = callback.from_user.id
    token = tokens[callback.from_user.id]["buy_token"]
    try:
        history = client.operation_history(label = user_do_buy[callback.from_user.id]["labl"])
        for operation in history.operations:
            stata = operation.status
        try:
            if stata == "success":
                tokens_plus_update(uid, token)
                if lingo(uid) == "RU":
                    await callback.message.edit_text(
                        LEXICON_RU["pay_tokens_yes"]
                    )
                elif lingo(uid) == "ENG":
                    await callback.message.edit_text(
                        LEXICON_ENG["pay_tokens_yes"]
                    )
                elif lingo(uid) == "ES":
                    await callback.message.edit_text(
                        LEXICON_ES["pay_tokens_yes"]
                    )
                elif lingo(uid) == "CN":
                    await callback.message.edit_text(
                        LEXICON_CN["pay_tokens_yes"]
                    )
        except UnboundLocalError:
            if lingo(uid) == "RU":
                await callback.message.edit_text(
                    LEXICON_RU["pay_no"],
                    reply_markup=ikb_back_ru()
                )
            elif lingo(uid) == "ENG":
                await callback.message.edit_text(
                    LEXICON_ENG["pay_no"],
                    reply_markup=ikb_back_eng()
                )
            elif lingo(uid) == "ES":
                await callback.message.edit_text(
                    LEXICON_ES["pay_no"],
                    reply_markup=ikb_back_es()
                )
            elif lingo(uid) == "CN":
                await callback.message.edit_text(
                    LEXICON_CN["pay_no"],
                    reply_markup=ikb_back_cn()
                )
    except KeyError:
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                LEXICON_RU["pay_no"],
                reply_markup=ikb_back_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                LEXICON_ENG["pay_no"],
                reply_markup=ikb_back_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                LEXICON_ES["pay_no"],
                reply_markup=ikb_back_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                LEXICON_CN["pay_no"],
                reply_markup=ikb_back_cn()
            )
    await state.set_state(FSMForm.tokens)

@router.callback_query(F.data == "check")
async def check(callback: CallbackQuery, state: FSMContext): 
    uid = callback.from_user.id
    try:
        history = client.operation_history(label = user_do_buy[callback.from_user.id]["labl"])
        for operation in history.operations:
            stata = operation.status
        try:
            if stata == "success":
                if lingo(uid) == "RU":
                    await callback.message.edit_text(
                        LEXICON_RU["pay_yes"]
                    )
                elif lingo(uid) == "ENG":
                    await callback.message.edit_text(
                        LEXICON_ENG["pay_yes"]
                    )
                elif lingo(uid) == "ES":
                    await callback.message.edit_text(
                        LEXICON_ES["pay_yes"]
                    )
                elif lingo(uid) == "CN":
                    await callback.message.edit_text(
                        LEXICON_CN["pay_yes"]
                    )
        except UnboundLocalError:
            if lingo(uid) == "RU":
                await callback.message.edit_text(
                    LEXICON_RU["pay_no"],
                    reply_markup=ikb_back_ru()
                )
            elif lingo(uid) == "ENG":
                await callback.message.edit_text(
                    LEXICON_ENG["pay_no"],
                    reply_markup=ikb_back_eng()
                )
            elif lingo(uid) == "ES":
                await callback.message.edit_text(
                    LEXICON_ES["pay_no"],
                    reply_markup=ikb_back_es()
                )
            elif lingo(uid) == "CN":
                await callback.message.edit_text(
                    LEXICON_CN["pay_no"],
                    reply_markup=ikb_back_cn()
                )
    except KeyError:
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                LEXICON_RU["pay_no"],
                reply_markup=ikb_back_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                LEXICON_ENG["pay_no"],
                reply_markup=ikb_back_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                LEXICON_ES["pay_no"],
                reply_markup=ikb_back_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                LEXICON_CN["pay_no"],
                reply_markup=ikb_back_cn()
            )

@router.callback_query(F.data == "kling")
async def kling(callback: CallbackQuery):
    video_pro = FSInputFile("C:\\Users\\user\\Desktop\\projects\\local\\AI-Bot\\chat_gpt\\kling_PRO.mp4", filename="kling_PRO.mp4")
    video_standard = FSInputFile("C:\\Users\\user\\Desktop\\projects\\local\\AI-Bot\\chat_gpt\\kling_STANDARD.mp4", filename="kling_STANDARD.mp4")
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.answer_video(
            video=video_pro,
            caption="👑<b>Kling Pro</b>\n\n🗓Срок подписки: <b>7 дней</b>\n\nДоступные тарифы👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_ru_pro()
        )
        await callback.message.answer_video(
            video=video_standard,
            caption="🚀<b>Kling Standard</b>\n\n🗓Срок подписки: <b>7 дней</b>\n\nДоступные тарифы👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_ru_standard()
        )
    elif lingo(uid) == "ENG":
        await callback.message.answer_video(
            media=video_pro,
            caption="<b>Kling Pro</b>\n\n🗓Subscription period: <b>7 days</b>\n\nAvailable tariffs👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_eng_pro()
        )
        await callback.message.answer_video(
            media=video_standard,
            caption="<b>Kling Standard</b>\n\n🗓Subscription period: <b>7 days</b>\n\nAvailable tariffs👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_eng_standard()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer_video(
            media=video_pro,
            caption="<b>Kling Pro</b>\n\n🗓Periodo de suscripción: <b>7 días</b>\n\nTarifas disponibles👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_es_pro()
        )
        await callback.message.answer_video(
            media=video_standard,
            caption="<b>Kling Standard</b>\n\n🗓Periodo de suscripción: <b>7 días</b>\n\nTarifas disponibles👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_es_standard()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer_video(
            media=video_pro,
            caption="<b>Kling Pro</b>\n\n🗓订阅期限：<b>7 天</b>\n\n 可用关税👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_cn_pro()
        )
        await callback.message.answer_video(
            media=video_standard,
            caption="<b>Kling Standard</b>\n\n🗓订阅期限：<b>7 天</b>\n\n 可用关税👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_luma_ikb_cn_standard()
        )

@router.callback_query(F.data == "udio")
async def udio(callback: CallbackQuery):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.answer(
            text="🎧<b>Udio</b>\n\n🗓Срок подписки: <b>7 дней</b>\n\nДоступные тарифы👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_udio_ikb_ru()
        )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            text="🎧<b>Udio</b>\n\n🗓Subscription period: <b>7 days</b>\n\nAvailable tariffs👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_udio_ikb_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            text="🎧<b>Udio</b>\n\n🗓Periodo de suscripción: <b>7 días</b>\n\nTarifas disponibles👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_udio_ikb_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            text="🎧<b>Udio</b>\n\n🗓订阅期限：<b>7 天</b>\n\n 可用关税👇",
            parse_mode=ParseMode.HTML,
            reply_markup=choose_udio_ikb_cn()
        )

#Покупка токенов

@router.callback_query(F.data == "udio_10")
async def week(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    days = 7
    times = 10
    await state.update_data(days = days)
    days_luma[callback.from_user.id] = await state.get_data()
    await state.update_data(times = times)
    luma_times[callback.from_user.id] = await state.get_data()
    num3 = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    await state.update_data(labl = num3)
    invoice = Quickpay(
            receiver="410012465765599",
            quickpay_form="shop",
            targets="Sponsor",
            paymentType="SB",
            sum=499,
            label=num3
        )
    if lingo(uid) == "RU":
        await callback.message.answer(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=ikb_premium_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(FSMForm.udio)

@router.callback_query(F.data == "week_standard_5")
async def week(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    days = 7
    times = 5
    mode = "standard"
    seconds = 5
    await state.update_data(days = days)
    days_luma[callback.from_user.id] = await state.get_data()
    await state.update_data(times = times)
    luma_times[callback.from_user.id] = await state.get_data()
    num3 = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    await state.update_data(version = mode)
    kling_version[callback.from_user.id] = await state.get_data()
    await state.update_data(sec = seconds)
    invoice = Quickpay(
            receiver="410012465765599",
            quickpay_form="shop",
            targets="Sponsor",
            paymentType="SB",
            sum=399,
            label=num3
        )
    if lingo(uid) == "RU":
        await callback.message.answer(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=ikb_premium_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(FSMForm.luma)

@router.callback_query(F.data == "week_standard_10")
async def week(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    days = 7
    times = 10
    mode = "standard"
    seconds = 10
    await state.update_data(days = days)
    days_luma[callback.from_user.id] = await state.get_data()
    await state.update_data(times = times)
    luma_times[callback.from_user.id] = await state.get_data()
    num3 = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    await state.update_data(version = mode)
    kling_version[callback.from_user.id] = await state.get_data()
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    await state.update_data(sec = seconds)
    invoice = Quickpay(
            receiver="410012465765599",
            quickpay_form="shop",
            targets="Sponsor",
            paymentType="SB",
            sum=659,
            label=num3
        )
    if lingo(uid) == "RU":
        await callback.message.answer(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=ikb_premium_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(FSMForm.luma)

@router.callback_query(F.data == "week_pro_5")
async def week(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    days = 7
    times = 5
    mode = "pro"
    seconds = 5
    await state.update_data(days = days)
    days_luma[callback.from_user.id] = await state.get_data()
    await state.update_data(times = times)
    luma_times[callback.from_user.id] = await state.get_data()
    num3 = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    await state.update_data(version = mode)
    kling_version[callback.from_user.id] = await state.get_data()
    await state.update_data(sec = seconds)
    invoice = Quickpay(
            receiver="410012465765599",
            quickpay_form="shop",
            targets="Sponsor",
            paymentType="SB",
            sum=899,
            label=num3
        )
    if lingo(uid) == "RU":
        await callback.message.answer(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=ikb_premium_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(FSMForm.luma)

@router.callback_query(F.data == "week_pro_10")
async def week(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    days = 7
    times = 10
    mode = "pro"
    seconds = 10
    await state.update_data(days = days)
    days_luma[callback.from_user.id] = await state.get_data()
    await state.update_data(times = times)
    luma_times[callback.from_user.id] = await state.get_data()
    num3 = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    await state.update_data(version = mode)
    kling_version[callback.from_user.id] = await state.get_data()
    await state.update_data(sec = seconds)
    kling_sec[callback.from_user.id] = await state.get_data()
    invoice = Quickpay(
            receiver="410012465765599",
            quickpay_form="shop",
            targets="Sponsor",
            paymentType="SB",
            sum=1699,
            label=num3
        )
    if lingo(uid) == "RU":
        await callback.message.answer(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=ikb_premium_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(FSMForm.luma)

@router.callback_query(F.data == "check", StateFilter(FSMForm.luma))
async def check(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    luma_days = days_luma[callback.from_user.id]["days"]
    times = luma_times[callback.from_user.id]["times"]
    mode = kling_version[callback.from_user.id]["version"]
    sec = kling_sec[callback.from_user.id]["sec"]
    try:
        history = client.operation_history(label = user_do_buy[callback.from_user.id]["labl"])
        for operation in history.operations:
            stata = operation.status
        try:
            if stata == "success":
                if check_user_in_luma(uid) == False:
                    add_user_in_luma(user_id = uid, days = luma_days, times=times, mode=mode, seconds=sec)
                    if lingo(uid) == "RU":
                        await callback.message.edit_text(
                            LEXICON_RU["pay_yes"]
                        )
                    elif lingo(uid) == "ENG":
                        await callback.message.edit_text(
                            LEXICON_ENG["pay_yes"]
                        )
                    elif lingo(uid) == "ES":
                        await callback.message.edit_text(
                            LEXICON_ES["pay_yes"]
                        )
                    elif lingo(uid) == "CN":
                        await callback.message.edit_text(
                            LEXICON_CN["pay_yes"]
                        )
            else:
                    if lingo(uid) == "RU":
                        await callback.message.edit_text(
                            LEXICON_RU["pay_yes"]
                        )
                    elif lingo(uid) == "ENG":
                        await callback.message.edit_text(
                            LEXICON_ENG["pay_yes"]
                        )
                    elif lingo(uid) == "ES":
                        await callback.message.edit_text(
                            LEXICON_ES["pay_yes"]
                        )
                    elif lingo(uid) == "CN":
                        await callback.message.edit_text(
                            LEXICON_CN["pay_yes"]
                        )
        except UnboundLocalError:
            if lingo(uid) == "RU":
                await callback.message.edit_text(
                    LEXICON_RU["pay_no"],
                    reply_markup=ikb_back_ru()
                )
            elif lingo(uid) == "ENG":
                await callback.message.edit_text(
                    LEXICON_ENG["pay_no"],
                    reply_markup=ikb_back_eng()
                )
            elif lingo(uid) == "ES":
                await callback.message.edit_text(
                    LEXICON_ES["pay_no"],
                    reply_markup=ikb_back_es()
                )
            elif lingo(uid) == "CN":
                await callback.message.edit_text(
                    LEXICON_CN["pay_no"],
                    reply_markup=ikb_back_cn()
                )
    except KeyError:
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                LEXICON_RU["pay_no"],
                reply_markup=ikb_back_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                LEXICON_ENG["pay_no"],
                reply_markup=ikb_back_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                LEXICON_ES["pay_no"],
                reply_markup=ikb_back_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                LEXICON_CN["pay_no"],
                reply_markup=ikb_back_cn()
            )
    await state.set_state(default_state)

@router.callback_query(F.data == "check", StateFilter(FSMForm.udio))
async def check(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    luma_days = days_luma[callback.from_user.id]["days"]
    times = luma_times[callback.from_user.id]["times"]
    try:
        history = client.operation_history(label = user_do_buy[callback.from_user.id]["labl"])
        for operation in history.operations:
            stata = operation.status
        try:
            if stata == "success":
                if check_user_in_udio(uid) == False:
                    add_user_in_udio(user_id = uid, days = luma_days, times=times)
                    if lingo(uid) == "RU":
                        await callback.message.edit_text(
                            LEXICON_RU["pay_yes"]
                        )
                    elif lingo(uid) == "ENG":
                        await callback.message.edit_text(
                            LEXICON_ENG["pay_yes"]
                        )
                    elif lingo(uid) == "ES":
                        await callback.message.edit_text(
                            LEXICON_ES["pay_yes"]
                        )
                    elif lingo(uid) == "CN":
                        await callback.message.edit_text(
                            LEXICON_CN["pay_yes"]
                        )
            else:
                    if lingo(uid) == "RU":
                        await callback.message.edit_text(
                            LEXICON_RU["pay_yes"]
                        )
                    elif lingo(uid) == "ENG":
                        await callback.message.edit_text(
                            LEXICON_ENG["pay_yes"]
                        )
                    elif lingo(uid) == "ES":
                        await callback.message.edit_text(
                            LEXICON_ES["pay_yes"]
                        )
                    elif lingo(uid) == "CN":
                        await callback.message.edit_text(
                            LEXICON_CN["pay_yes"]
                        )
        except UnboundLocalError:
            if lingo(uid) == "RU":
                await callback.message.edit_text(
                    LEXICON_RU["pay_no"],
                    reply_markup=ikb_back_ru()
                )
            elif lingo(uid) == "ENG":
                await callback.message.edit_text(
                    LEXICON_ENG["pay_no"],
                    reply_markup=ikb_back_eng()
                )
            elif lingo(uid) == "ES":
                await callback.message.edit_text(
                    LEXICON_ES["pay_no"],
                    reply_markup=ikb_back_es()
                )
            elif lingo(uid) == "CN":
                await callback.message.edit_text(
                    LEXICON_CN["pay_no"],
                    reply_markup=ikb_back_cn()
                )
    except KeyError:
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                LEXICON_RU["pay_no"],
                reply_markup=ikb_back_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                LEXICON_ENG["pay_no"],
                reply_markup=ikb_back_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                LEXICON_ES["pay_no"],
                reply_markup=ikb_back_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                LEXICON_CN["pay_no"],
                reply_markup=ikb_back_cn()
            )
    await state.set_state(default_state)

@router.callback_query(F.data == "10k")
async def tokens_10(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    token = 10000
    await state.update_data(buy_token = token)
    tokens[callback.from_user.id] = await state.get_data()
    num1 = random.randint(1, 2147483647)
    num2 = random.randint(-2147483647, -1)
    num3 = (num1 + num2) * 3
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    if check_user_prem(uid) == True:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=49,
                label=num3
            )
    else:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=99,
                label=num3
            )
    if lingo(uid) == "RU":
        await callback.message.edit_text(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_cn()
        )
    await state.set_state(FSMForm.tokens)

@router.callback_query(F.data == "20k")
async def tokens_10(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    token = 20000
    await state.update_data(buy_token = token)
    tokens[callback.from_user.id] = await state.get_data()
    num1 = random.randint(1, 2147483647)
    num2 = random.randint(-2147483647, -1)
    num3 = (num1 + num2) * 3
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    if check_user_prem(uid) == False:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=199,
                label=num3
            )
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                    text = hlink(
                        title="Ваша ссылка для оплаты сгенерирована 👈",
                        url=invoice.base_url
                     ),
                    parse_mode=ParseMode.HTML,
                    reply_markup=buy_tokens_ru()
                )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                text = hlink(
                    title="Your payment link has been generated 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                text = hlink(
                    title="Se ha generado tu enlace de pago 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                text = hlink(
                    title="您的付款链接已生成 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_cn()
            )
    else:
        invoice = Quickpay(
            receiver="410012465765599",
            quickpay_form="shop",
            targets="Sponsor",
            paymentType="SB",
            sum=99,
            label=num3
                )
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                    text = hlink(
                        title="Ваша ссылка для оплаты сгенерирована 👈",
                        url=invoice.base_url
                     ),
                    parse_mode=ParseMode.HTML,
                    reply_markup=buy_tokens_ru()
                )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                text = hlink(
                    title="Your payment link has been generated 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                text = hlink(
                    title="Se ha generado tu enlace de pago 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                text = hlink(
                    title="您的付款链接已生成 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_cn()
            )
    await state.set_state(FSMForm.tokens)

@router.callback_query(F.data == "30k")
async def tokens_10(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    token = 30000
    await state.update_data(buy_token = token)
    tokens[callback.from_user.id] = await state.get_data()
    num1 = random.randint(1, 2147483647)
    num2 = random.randint(-2147483647, -1)
    num3 = (num1 + num2) * 3
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    if check_user_prem(uid) == True:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=159,
                label=num3
            )
    else:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=299,
                label=num3
            )
    if lingo(uid) == "RU":
        await callback.message.edit_text(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_cn()
        )
    await state.set_state(FSMForm.tokens)

@router.callback_query(F.data == "150k")
async def tokens_10(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    token = 150000
    await state.update_data(buy_token = token)
    tokens[callback.from_user.id] = await state.get_data()
    num1 = random.randint(1, 2147483647)
    num2 = random.randint(-2147483647, -1)
    num3 = (num1 + num2) * 3
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    if check_user_prem(uid) == True:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=459,
                label=num3
            )
    else:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=999,
                label=num3
            )
    if lingo(uid) == "RU":
        await callback.message.edit_text(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_cn()
        )
    await state.set_state(FSMForm.tokens)

@router.callback_query(F.data == "500k")
async def tokens_10(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    token = 500000
    await state.update_data(buy_token = token)
    tokens[callback.from_user.id] = await state.get_data()
    num1 = random.randint(1, 2147483647)
    num2 = random.randint(-2147483647, -1)
    num3 = (num1 + num2) * 3
    await state.update_data(labl = num3)
    user_do_buy[callback.from_user.id] = await state.get_data()
    if check_user_prem(uid) == True:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=1399,
                label=num3
            )
    else:
        invoice = Quickpay(
                receiver="410012465765599",
                quickpay_form="shop",
                targets="Sponsor",
                paymentType="SB",
                sum=2699,
                label=num3
            )
    if lingo(uid) == "RU":
        await callback.message.edit_text(
                text = hlink(
                    title="Ваша ссылка для оплаты сгенерирована 👈",
                    url=invoice.base_url
                 ),
                parse_mode=ParseMode.HTML,
                reply_markup=buy_tokens_ru()
            )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            text = hlink(
                title="Your payment link has been generated 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            text = hlink(
                title="Se ha generado tu enlace de pago 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            text = hlink(
                title="您的付款链接已生成 👈",
                url=invoice.base_url
             ),
            parse_mode=ParseMode.HTML,
            reply_markup=buy_tokens_cn()
        )
    await state.set_state(FSMForm.tokens)

#Кнопка назад (в меню премиум после оплаты)
@router.callback_query(F.data == "back", StateFilter(FSMForm.pre_menu))
async def back(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.edit_text(
            LEXICON_RU["premium"],
            reply_markup=ikb_premium_ru()
        )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            LEXICON_ENG["premium"],
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            LEXICON_ES["premium"],
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            LEXICON_CN["premium"],
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(default_state)

#Кнопка в меню с токенами
@router.callback_query(F.data == "back", StateFilter(FSMForm.tokens))
async def back_tokens(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.edit_text(
            "Выберите желаемое количество токенов",
            reply_markup=tokens_ikb_ru()
        )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            "Выберите желаемое количество токенов",
            reply_markup=tokens_ikb_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            "Выберите желаемое количество токенов",
            reply_markup=tokens_ikb_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            "Выберите желаемое количество токенов",
            reply_markup=tokens_ikb_cn()
        )

#Кнопка назад (в главное меню)
@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.edit_text(
            LEXICON_RU["menu"]
        )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            LEXICON_ENG["menu"]
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            LEXICON_ES["menu"]
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            LEXICON_CN["menu"]
        )
    await state.set_state(default_state)


#Кнопка-соло назад (в меню премиум после оплаты)
@router.callback_query(F.data == "back_one", StateFilter(FSMForm.pre_menu))
async def back(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.edit_text(
            LEXICON_RU["premium"],
            reply_markup=ikb_premium_ru()
        )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            LEXICON_ENG["premium"],
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            LEXICON_ES["premium"],
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            LEXICON_CN["premium"],
            reply_markup=ikb_premium_cn()
        )
    await state.set_state(default_state)

#Кнопка-соло назад (в меню токенов)
@router.callback_query(F.data == "back_one", StateFilter(FSMForm.tokens))
async def back(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.edit_text(
           "LEX['tokens']",
            reply_markup=tokens_ikb_ru()
        )
    elif lingo(uid) == "ENG":
        await callback.message.edit_text(
            "LEX['tokens']",
            reply_markup=tokens_ikb_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.edit_text(
            "LEX['tokens']",
            reply_markup=tokens_ikb_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.edit_text(
            "LEX['tokens']",
            reply_markup=tokens_ikb_cn()
        )

#Меню premium
@router.callback_query(F.data =="premium")
async def buy_premium(callback: CallbackQuery):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.answer(
            LEXICON_RU["premium"],
            reply_markup=ikb_premium_ru()
        )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            LEXICON_ENG["premium"],
            reply_markup=ikb_premium_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            LEXICON_ES["premium"],
            reply_markup=ikb_premium_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            LEXICON_CN["premium"],
            reply_markup=ikb_premium_cn()
        )

#Токены из ikb
@router.callback_query(F.data == "tokens")
async def tokens_from_ikb(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    if lingo(uid) == "RU":
        await callback.message.answer(
            "Выберите желаемое количество токенов",
            reply_markup=tokens_ikb_ru()
        )
    elif lingo(uid) == "ENG":
        await callback.message.answer(
            "Select the desired number of tokens",
            reply_markup=tokens_ikb_eng()
        )
    elif lingo(uid) == "ES":
        await callback.message.answer(
            "Seleccione el número de fichas deseado",
            reply_markup=tokens_ikb_es()
        )
    elif lingo(uid) == "CN":
        await callback.message.answer(
            "選擇所需的代幣數量",
            reply_markup=tokens_ikb_cn()
        )
    await state.set_state(FSMForm.tokens)

@router.callback_query(F.data == "help")
async def help_callback(callback: CallbackQuery):
    if lingo(callback.from_user.id) == "RU":
        await callback.message.answer(
            "❗️Если бот завис, нажмите /start для того что бы перезапустить бота❗️"
        )
    elif lingo(callback.from_user.id) == "ENG":
        await callback.message.answer(
            "❗️Если bot hangs, press /start to restart бота❗️"
        )
    elif lingo(callback.from_user.id) == "ES":
        await callback.message.answer(
            "❗️Si el bot se cuelga, pulsa /start para reiniciarlo❗️"
        )
    elif lingo(callback.from_user.id) == "CN":
        await callback.message.answer(
            "❗️如果机器人挂起，按 /start 重启机器人❗️"
        )

#Вызова пагинации текст
@router.callback_query(F.data == "text_ru")
async def pag_text(callback: CallbackQuery):
    page = 1
    await callback.message.edit_text(
        f"🔹Выберите нейросеть!\n\n✅Выбранная вами модель будет использоваться до тех пор, пока вы не выберете новую!\n\n👾Нейросеть: {title(page)}\n\n💎Расход: {stat(page)}",
        reply_markup=get_paginated_kb_ru()
    )

@router.callback_query(F.data == "text_eng")
async def pag_text(callback: CallbackQuery):
    page = 1
    await callback.message.edit_text(
        f"🔹Choose a AI!\n\n✅The model you have selected will be used until you choose a new one!\n\n👾AI: {title(page)}\n\n💎Flow rate: {stat_eng(page)}",
        reply_markup=get_paginated_kb_eng()
    )

@router.callback_query(F.data == "text_es")
async def pag_text(callback: CallbackQuery):
    page = 1
    await callback.message.edit_text(
        f"🔹¡Elige IA!\n\n✅El modelo elegido se utilizará hasta que elija uno nuevo\n\n👾AI: {title(page)}\n\n💎Gastos: {stat_es(page)}",
        reply_markup=get_paginated_kb_es()
    )

@router.callback_query(F.data == "text_cn")
async def pag_text(callback: CallbackQuery, state: FSMContext):
    page = 1
    await callback.message.edit_text(
        f"🔹选择人工智能!\n\n✅您选择的模型将一直使用，直到您选择新的模型!\n\n🔥新神经网络: {title(page)}\n\n💎流量: {stat_cn(page)}",
        reply_markup=get_paginated_kb_cn()
    )

@router.callback_query(F.data == "photo_ru")
async def pag_text(callback: CallbackQuery):
    uid = callback.from_user.id
    ai = "DALL-E 3"
    await callback.message.answer(
        f"🔹Для генирации фото используется DALL-E 3\n\n✅Что бы сгенирировать фото, просто введите текст! \n\n✨Для повторной генерации просто нажмите кнопку\n'🔁Повторить генерацию' и введите желаемый запрос!\n\n👾Нейросеть: DALL-E 3\n\n💎Расход: 1000 токенов",
        update_ai(uid, ai)
    )

@router.callback_query(F.data == "photo_eng")
async def pag_text(callback: CallbackQuery):
    uid = callback.from_user.id
    ai = "DALL-E 3"
    await callback.message.answer(
        f"🔹The DALL-E 3 is used for photo generation!\n\n✅To generate a photo, just enter the text!\n\n✨To re-generate, simply click\n'🔁Re-generate' and enter your desired request!\n\n👾AI: DALL-E 3 3\n\n💎Flow rate: 1000 tokens",
        update_ai(uid, ai)
    )

@router.callback_query(F.data == "photo_es")
async def pag_text(callback: CallbackQuery):
    uid = callback.from_user.id
    ai = "DALL-E 3"
    await callback.message.answer(
        f"🔹 El DALL-E 3 se utiliza para la generación de fotos\n\n✅¡Para generar una foto, basta con introducir el texto!\n\n✨Para volver a generar, simplemente haz clic en\n'🔁Re-generar' e introduce la solicitud que desee\n\n👾AI: DALL-E 3 3\n\n💎Gastos: 1000 tokens",
        update_ai(uid, ai)
    )

@router.callback_query(F.data == "photo_cn")
async def pag_text(callback: CallbackQuery):
    uid = callback.from_user.id
    ai = "DALL-E 3"
    await callback.message.answer(
        f"🔹《DALL-E 3》用于生成照片\n\n✅要生成照片，只需输入文字!\n\n✨要重新生成，只需单击“🔁重新生成 ”并输入所需的请求!\n\n👾神经网络：DALL-E 3 3\n\n💎费用：1000 代币",
        update_ai(uid, ai)
    )


#Выбор нейронок
@router.callback_query(Pagination_ru.filter())
async def neuro_ru(callback: CallbackQuery, callback_data: Pagination_ru):
    uid = callback.from_user.id
    page = callback_data.page
    neuro = title(page)
    update_ai(uid, neuro)
    await callback.message.edit_text(
            f"🔹Выберите нейросеть!\n\n✅Выбранная вами модель будет использоваться до тех пор, пока вы не выберете новую!\n\n👾Нейросеть: {title(page)}\n\n💎Расход: {stat(page)}",
            reply_markup=get_paginated_kb_ru(page=page) 
        )

@router.callback_query(Pagination_eng.filter())
async def neuro_eng(callback: CallbackQuery, callback_data: Pagination_eng):
    uid = callback.from_user.id
    page = callback_data.page
    neuro = title(page)
    update_ai(uid, neuro)
    await callback.message.edit_text(
            f"🔹Choose a AI!\n\n✅The model you have selected will be used until you choose a new one!\n\n👾Model of AI: {title(page)}\n\n💎Flow rate: {stat_eng(page)}",
            reply_markup=get_paginated_kb_eng(page=page) 
        )

@router.callback_query(Pagination_es.filter())
async def neuro_es(callback: CallbackQuery, callback_data: Pagination_es):
    uid = callback.from_user.id
    page = callback_data.page
    neuro = title(page)
    update_ai(uid, neuro)
    await callback.message.edit_text(
            f"🔹¡Elige IA!\n\n✅El modelo elegido se utilizará hasta que elija uno nuevo\n\n👾AI: {title(page)}\n\n💎Gastos: {stat_es(page)}",
            reply_markup=get_paginated_kb_es(page=page) 
        )

@router.callback_query(Pagination_cn.filter())
async def neuro_cn(callback: CallbackQuery, callback_data: Pagination_cn):
    uid = callback.from_user.id
    page = callback_data.page
    neuro = title(page)
    update_ai(uid, neuro)
    await callback.message.edit_text(
            f"🔹选择人工智能!\n\n✅您选择的模型将一直使用，直到您选择新的模型!\n\n👾神经网络: {title(page)}\n\n💎流量: {stat_cn(page)}",
            reply_markup=get_paginated_kb_cn(page=page) 
        )
    
@router.callback_query(F.data == "1")
async def service_1(callback: CallbackQuery):
    uid = callback.from_user.id
    num = "1"
    if check_user_prem(uid) == True:
        set_mode(uid, num)
        if lingo(uid) == "RU":
            await callback.message.edit_text(
            "✅Вы включили режим без задач"
                )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                "✅You have enabled the no-task mode"
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                "✅Has cambiado al modo sin tareas"
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                "✅您已切换到无任务模式"
            )

    else:
        if lingo(uid) == "RU":
            await callback.message.edit_text(
                "💎Для использования данных функций приобретите премиум!",
                reply_markup=ikb_premium_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.edit_text(
                "💎To use these features, purchase premium!",
                reply_markup=ikb_premium_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.edit_text(
                "💎Para utilizar estas funciones, ¡compra Premium!",
                reply_markup=ikb_premium_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.edit_text(
                "💎要使用这些功能，请购买高级版!",
                reply_markup=ikb_premium_cn()
            )

@router.callback_query(F.data == "2")
async def service_1(callback: CallbackQuery):
    uid = callback.from_user.id
    num = "2"
    if check_user_prem(uid) == True:
        set_mode(uid, num)
        if lingo(uid) == "RU":
            await callback.message.answer(
            "✅Напишите вашу тему для эссе"
                )
        elif lingo(uid) == "ENG":
            await callback.message.answer(
                "✅Write your essay topic",
            )
        elif lingo(uid) == "ES":
            await callback.message.answer(
                "✅Escriba el tema de su ensayo",
            )
        elif lingo(uid) == "CN":
            await callback.message.answer(
                "✅撰写论文题目",
            )

    else:
        if lingo(uid) == "RU":
            await callback.message.answer(
                "💎Для использования данных функций приобретите премиум!",
                reply_markup=ikb_premium_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.answer(
                "💎To use these features, purchase premium!",
                reply_markup=ikb_premium_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.answer(
                "💎Para utilizar estas funciones, ¡compra Premium!",
                reply_markup=ikb_premium_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.answer(
                "💎要使用这些功能，请购买高级版!",
                reply_markup=ikb_premium_cn()
            )

@router.callback_query(F.data == "3")
async def service_1(callback: CallbackQuery):
    uid = callback.from_user.id
    num = "3"
    if check_user_prem(uid) == True:
        if lingo(uid) == "RU":
            set_mode(uid, num)
            await callback.message.answer(
            "✅Напишите тему вашей курсовой работы"
                )
        elif lingo(uid) == "ENG":
            await callback.message.answer(
                "✅Write the topic of your term paper",
            )
        elif lingo(uid) == "ES":
            await callback.message.answer(
                "✅Escribe el tema de tu trabajo trimestral",
            )
        elif lingo(uid) == "CN":
            callback.message.answer(
                "✅写出学期论文的题目",
            )

    else:
        if lingo(uid) == "RU":
            await callback.message.answer(
                "💎Для использования данных функций приобретите премиум!",
                reply_markup=ikb_premium_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.answer(
                "💎To use these features, purchase premium!",
                reply_markup=ikb_premium_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.answer(
                "💎Para utilizar estas funciones, ¡compra Premium!",
                reply_markup=ikb_premium_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.answer(
                "💎要使用这些功能，请购买高级版!",
                reply_markup=ikb_premium_cn()
            )

@router.callback_query(F.data == "4")
async def service_1(callback: CallbackQuery):
    uid = callback.from_user.id
    num = "4"
    if check_user_prem(uid) == True:
        set_mode(uid, num)
        if lingo(uid) == "RU":
            await callback.message.answer(
            "✅Напишите тему для вашей Seo статьи"
                )
        elif lingo(uid) == "ENG":
            await callback.message.answer(
                "✅Escribe un tema para tu artículo seo",
            )
        elif lingo(uid) == "ES":
            await callback.message.answer(
                "✅Escriba el tema de su ensayo",
            )
        elif lingo(uid) == "CN":
            await callback.message.answer(
                "✅为你的搜索引擎优化文章写一个主题",
            )

    else:
        if lingo(uid) == "RU":
            await callback.message.answer(
                "💎Для использования данных функций приобретите премиум!",
                reply_markup=ikb_premium_ru()
            )
        elif lingo(uid) == "ENG":
            await callback.message.answer(
                "💎To use these features, purchase premium!",
                reply_markup=ikb_premium_eng()
            )
        elif lingo(uid) == "ES":
            await callback.message.answer(
                "💎Para utilizar estas funciones, ¡compra Premium!",
                reply_markup=ikb_premium_es()
            )
        elif lingo(uid) == "CN":
            await callback.message.answer(
                "💎要使用这些功能，请购买高级版!",
                reply_markup=ikb_premium_cn()
            )