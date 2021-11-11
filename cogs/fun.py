from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option
from random import *

class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    #yourmom command
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="What does Marlene say?")
    async def yourmom(self, ctx):
        choiceyourmom = ["Your mother.","ur mum","haha L","https://tenor.com/bID8C.gif"]
        responseyourmom = randint(0,len(choiceyourmom))
        resultyourmom=choiceyourmom[responseyourmom]
        ctx.respond(resultyourmom)

    #8ball command
    @slash_command(name='fortune',guild_ids=[866756514996158474,899047123415343114],description="Asks the Magic 8 Ball a question.")
    async def eightBall(ctx,question: Option(str,"What you want to ask the 8ball.")):
        response8ball =['Without a doubt.','Outlook good.','Better not tell you now.','Cannot predict now.','My reply is no.','Outlook not so good.']
        choice=randint(0,len(response8ball))
        result=response8ball[choice]
        await ctx.respond(result)

    #yeetsleep
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Makes the person go to bed.")
    async def yeetsleep(self,ctx,name: Option(str, "The person who needs to go to sleep.",required=True)):
        await ctx.respond(f"Sleep is good and important, {name}.")

    #ping command
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Tells the ping of the bot.")
    async def ping(self,ctx,bot):
        await ctx.respond(f'Pong! The bot is currently running {bot.latency} behind.')

    #eye command
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Replies with the Eye emoji!")
    async def eye(ctx):
        await ctx.respond(":eye:")

    #invicta's marlene command
    @slash_command(guild_ids=[866756514996158474],description="What does have the team enjoy saying?")
    async def marlene(ctx):
        await ctx.respond(":skull:")

    #help command
    @slash_command(guild_ids=[866756514996158474], description="Calls Kevin for help.")
    async def help(ctx, need: Option(str, "What you need help with.",required=False,default="with life")):
        await ctx.respond(f"<@242490141309009920> we need help {need}!")


def setup(bot):
    bot.add_cog(Fun(bot))