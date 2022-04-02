from discord import Intents
from discord.ext import commands
from filefinder import getfile
import logging
import os

class DiscordBot(commands.Bot):
    def __init__(self, command_prefix) -> None:
        default_intents = Intents.default()
        default_intents.members = True
        super().__init__(command_prefix=command_prefix, intents=default_intents,  help_command=None)     
        
    async def on_ready(self):
        msg = f"(connection) -- {self.user.display_name} est connecté au serveur."
        print(msg)
        logging.warning(msg)
        
    async def on_message(self, message):
        logging.warning(f"(Sent message) -- {message.content} -- [{message.author.display_name}]")  
        # always still at the end 
        await self.process_commands(message)  
        
    def load_cogs(self):
        for folder in os.listdir(getfile("modules")):
            filepath = os.path.join(getfile("modules"), folder, "cog.py")
            print(filepath)
            if os.path.exists(filepath):
                self.load_extension(f"modules.{folder}.cog") 
        