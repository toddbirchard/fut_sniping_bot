from src import init_bot

bot = init_bot()

if __name__ == "__main__":
    bot.buy_player(PLAYER["name"], PLAYER["cost"])
