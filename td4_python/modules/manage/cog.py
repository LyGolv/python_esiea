import discord
from discord.ext import commands

class ManageCommand(commands.Cog, name="helpcommand"):
    """Command to manage channel"""
    
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def clear(self, ctx: commands.Context, nombre: int):
        """Clear message on channel"""
        messages = await ctx.channel.history(limit = nombre + 1).flatten()
        for message in messages:
            await message.delete()
    
    @commands.command()
    async def ban(self, ctx: commands.Context, user : discord.User, *reason):
        """use to ban user"""
        reason = " ".join(reason)
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")

    @commands.command()
    async def unban(self, ctx: commands.Context, id, *reason):
        """Use to unban user"""
        reason = " ".join(reason)
        banned_users = await ctx.guild.bans()
        for i in banned_users:
            if str(i.user.id) == str(id):
                await ctx.guild.unban(i.user, reason=reason)
                await ctx.send(f"{i.user.mention} à été unban")
                return
        await ctx.send(f"{id} n'est pas dans la liste des bannis")
        
    @commands.command()
    async def banlsId(self, ctx: commands.Context):
        """list all ban users"""
        bans = "La liste des utilisateurs banni du serveur sont: \n"
        banned_users = await ctx.guild.bans()
        test = 0
        for i in banned_users:
            test = 1
            bans += f"--> {i.user.name} : {i.user.id}\n"
        if test == 0:
            bans = "<-----Aucun utilisateur n'a été bannis----->"
        await ctx.send(bans)

def setup(bot: commands.Bot):
    bot.add_cog(ManageCommand(bot))