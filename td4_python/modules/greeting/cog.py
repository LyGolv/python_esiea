import discord
from discord.ext import commands
import logging
import random

class Greetings(commands.Cog, name="greeting"):
    """Greet the people who greet him"""
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        logging.warning("Un nouveau membre à rejoint le serveur")
        general_channel = member.guild.system_channel
        msg = "Bienvenue sur le serveur {0.mention} ! 🥳🥳".format(member)
        await general_channel.send(content=msg)   

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """Says hello"""
        list_ = [
            "😊","😊","😇","🙂","😁","😉",
            "😒","😒","🙈","🙉","🙂","😇",
            "😋","😎","🥰","😚","🤗","🤗"
        ]
        random.shuffle(list_)
        msg = f"Hello {ctx.author.mention} !, {list_[0]}  {list_[1]}"
        await ctx.send(msg)


def setup(bot: commands.Bot):
    bot.add_cog(Greetings(bot))