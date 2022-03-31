from discord import Intents
from discord.ext import commands
import logging

class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        default_intents = Intents.default()
        default_intents.members = True
        super().__init__(command_prefix="!", intents=default_intents)
        
    async def on_ready(self):
        msg = f"(connection) -- {self.user.display_name} est connecté au serveur."
        print(msg)
        logging.warning(msg)
        
    async def on_member_join(self, member):
        logging.warning("Un nouveau membre à rejoint le serveur")
        general_channel = self.get_channel(958704849304834111)
        msg = f"Bienvenue sur le serveur {member.display_name} !"
        await general_channel.send(content=msg)        
        
    async def on_message(self, message):
        logging.warning(f"(Sent message) : {message.content} -- [{message.author.display_name}]")