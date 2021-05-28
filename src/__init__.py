from src.bot import Bot
from config import USER, PLAYER, LOGIN_MANUALLY


def init_bot():
    fut_bot = Bot()
    if LOGIN_MANUALLY:
        fut_bot.login_manually()
    else:
        fut_bot.login(USER)
    return fut_bot
