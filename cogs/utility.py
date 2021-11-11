from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option
from PyDictionary import PyDictionary
from googlesearch import search

dictionary=PyDictionary()

class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    #hello command
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Says hi to you or someone else!")
    async def hello(self, ctx, name: Option(str, "The person you want to say hello to.", required=False,default="friend")):
        await ctx.respond(f"Hello, {name}!")

        #thesaurus series
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Defines the word.")
    async def define(self,ctx,word: Option(str,"The word you want to define.",required=True)):
        await ctx.respond(dictionary.meaning(word))

    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Defines the word.")
    async def synonym(self,ctx,word: Option(str,"The word you want the synonym.",required=True)):
        await ctx.respond(dictionary.synonym(word))

    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Defines the word.")
    async def antonym(self,ctx,word: Option(str,"The word you want the opposite of.",required=True)):
        await ctx.respond(dictionary.antonym(word))

    #google search command
    #find command
    @slash_command(guild_ids=[866756514996158474,899047123415343114],description="Searches Google.",alias=["search","google"])
    async def search(self,ctx,searchEntry: Option(str, "What you want to search for.",required=True,default='test'),amount: Option(int, "The amount of results you want.", required=False,default=2)):
        author = ctx.author.mention
        query = searchEntry
        await ctx.respond(f"Here are the links related to your question!") 
        async with ctx.typing(): 
            for j in search(query, tld="co.in", num=amount, stop=amount, pause=2):
                await ctx.send(f"\n:point_right: {j}")


def setup(bot):
    bot.add_cog(Utility(bot))