import discord
from discord.ext import commands
import logging

from pydantic import EnumMemberError

class HelpCommand(commands.Cog, name="helpcommand"):
    """Show the help command to user"""
    
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx: commands.Context):
        """Help User"""
        await ctx.send("I'm gonna help you!")
        embed : discord.Embed = discord.Embed(
            title = "# Help Commands",
            description = 'List of all available commands',
            colour = discord.Colour.blue()     
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name= "!hello", value='say hello', inline=True)
        embed.add_field(name= "!help", value='ask help', inline=True)
        embed.set_footer(text="Don't forget to add a reaction if this message help u :)")
        logging.warning("[!Help message send for user]")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(HelpCommand(bot))