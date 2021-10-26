from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option

class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    #hello command
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Says hi to you or someone else!")
    async def hello(ctx): #, name: Option(str, "The person you want to say hello to.", required=False,default="friend")
        await ctx.respond(f"Hello, {ctx.author.mention}!")


def setup(bot):
    bot.add_cog(Utility(bot))