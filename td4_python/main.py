import os
import logging
from dotenv import load_dotenv
from discordbot import DiscordBot
from parser import Parser
from filefinder import getfile

if __name__ == "__main__":
    parser: Parser = Parser().add_args().parse_args()
    config = getfile(parser.config)
    logfile = getfile(parser.logfile, "log")
    print("==>" + config)
    print("==>" + logfile)
    load_dotenv(dotenv_path=config)
    logging.basicConfig(
        filename=logfile,
        format='%(asctime)s -- %(message)s --',
        datefmt='%m/%d/%Y %I:%M:%S',
        encoding='utf-8', 
        level=logging.WARN
    )
    bot = DiscordBot(command_prefix="!")
    bot.load_cogs()
    
    bot.run(os.getenv("TOKEN"))