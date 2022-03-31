import os
import logging
from dotenv import load_dotenv
from discordbot import DiscordBot

if __name__ == "__main__":
    load_dotenv(dotenv_path="td4_python/config")
    logging.basicConfig(
        filename='discordbot.log',
        format='%(asctime)s -- %(message)s --',
        datefmt='%m/%d/%Y %I:%M:%S',
        encoding='utf-8', 
        level=logging.WARN
    )
    bot = DiscordBot()
    bot.run(os.getenv("TOKEN")) # éxécution du bot