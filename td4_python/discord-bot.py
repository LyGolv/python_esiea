import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="td4_python/config")

class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        default_intents = Intents.default()
        default_intents.members = True
        super().__init__(command_prefix="!", intents=default_intents)
        
    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")
        
    async def on_member_join(self, member):
        general_channel = bot.get_channel(958704849304834111)
        await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")
        
if __name__ == "__main__":
    bot = DiscordBot()
    bot.run(os.getenv("TOKEN")) # éxécution du bot