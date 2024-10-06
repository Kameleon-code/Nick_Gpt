from aiogram import Bot
from bot_settings import config
from aiogram.client.default import DefaultBotProperties

BOT = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties()
)