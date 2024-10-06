import logging
import asyncio
import schedule
import threading

from aiogram import Dispatcher, Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext


from handlers import handlers
from handlers import callback_handlers
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_eng import LEXICON_ENG
from lexicon.lexicon_es import LEXICON_ES
from lexicon.lexicon_cn import LEXICON_CN
from ikb.ikb import sub_ikb_ru, sub_ikb_eng, sub_ikb_esp, sub_ikb_cn
from keyboard.kb import menu_kb_ru, menu_kb_eng, menu_kb_es, menu_kb_cn
from db.db_premium import days, u_in, days_update, delete_user
from db.db import premium_days_set, tokens_plus_update
from chat_gpt import chat_gpt
from supa import BOT

logging.basicConfig(level=logging.INFO)

bot = BOT

dp = Dispatcher()

router = Router()

def premium_counter():
    list_ = []
    list_days = {}

    massive_big = u_in()
    for z in range(len(massive_big)):
        list_.append(massive_big[z][0])
    for m in list_:
        tokens_plus_update(m, 500)
        days_update(m)
        premium_days_set(m, days(m))
        if days(m) < 1:
            delete_user(m)
        else:
            key = m
            value = days(m)
            list_days[key] = value

def sched():
        schedule.every().day.at("00:00").do(premium_counter)

        while True:
            schedule.run_pending()

@router.callback_query(F.data == "check_ru")
async def check_subs(callback: CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id=-1002194126037, user_id=callback.from_user.id)

    if user_channel_status.status != 'left':
        await callback.message.edit_text(
            text=LEXICON_RU["menu"]
        )
        await callback.message.answer(
        "Ознакомься с командами в главном меню👆",
        reply_markup=menu_kb_ru())
    else:
        await callback.message.edit_text(
            text = LEXICON_RU["sub_no"],
            reply_markup=sub_ikb_ru()
        )

@router.callback_query(F.data == "check_eng")
async def check_subs(callback: CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id="-1002194126037", user_id=callback.from_user.id)

    if user_channel_status.status != 'left':
        await callback.message.edit_text(
            text=LEXICON_ENG["menu"]
        )
        await callback.message.answer(
        "Get familiar with the main menu commands👆",
        reply_markup=menu_kb_eng())
    else:
        await callback.message.edit_text( 
            text = LEXICON_ENG["sub_no"],
            reply_markup=sub_ikb_eng()
        )

@router.callback_query(F.data == "check_esp")
async def check_subs(callback: CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id="-1002194126037", user_id=callback.from_user.id)

    if user_channel_status.status != 'left':
        await callback.message.edit_text(
            text=LEXICON_ES["menu"]
        )
        await callback.message.answer(
        "Familiarízate con los comandos del menú principal👆",
        reply_markup=menu_kb_es())
    else:
        await callback.message.edit_text(
            text = LEXICON_ES["sub_no"],
            reply_markup=sub_ikb_esp()
        )

@router.callback_query(F.data == "check_cn")
async def check_subs(callback: CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id="-1002194126037", user_id=callback.from_user.id)

    if user_channel_status.status != 'left':
        await callback.message.edit_text(
            text=LEXICON_CN["menu"]
        )
        await callback.message.answer(
        "熟悉主功能表命令👆",
        reply_markup=menu_kb_cn())
    else:
        await callback.message.edit_text(
            text = LEXICON_CN["sub_no"],
            reply_markup=sub_ikb_cn()
        )

async def main():

    dp.include_router(router)
    dp.include_routers(handlers.router, callback_handlers.router, chat_gpt.router)

    t2 = threading.Thread(target=sched)
    t2.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot,skip_updates=False)

if __name__ == "__main__":
    asyncio.run(main())