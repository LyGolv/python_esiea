import discord
from discord.ext import commands
import logging
from datetime import datetime

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
            colour = discord.Colour.blue(),
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name= "!hello", value='say hello', inline=False)
        embed.add_field(name= "!help", value='ask help', inline=False)
        embed.add_field(name= "!clear NUMBER", value='deletes the specified number of messages ', inline=False)
        embed.add_field(name= "!ban @USER REASON", value='Use to ban user of channel', inline=False)
        embed.add_field(name= "!unban UserID REASON", value='Use to unban user', inline=False)
        embed.add_field(name= "!banlsId", value='List all of banned users', inline=False)
        embed.set_footer(text="U_U is useful?? :)")
        logging.warning("[!Help message send for user]")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(HelpCommand(bot))