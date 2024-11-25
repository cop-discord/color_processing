from color_processing import ColorInfo
from discord.ext.commands import command, Context, Cog, CommandError
from discord import Color, Member, User, Client
from typing import Union, Optional
class Color(Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @command(name = "color", description = "get information on a color")
    async def color(self, ctx: Context, *, query: Optional[Union[str, Color, Member, User]] = None):
        if query is None:
            if len(ctx.message.attachments) > 0:
                query = ctx.message.attachments[0].url
            else:
                raise CommandError("you must provide a query or attachment")
        return await ColorInfo().convert(ctx, query)
    
async def setup(bot: Client):
    await bot.add_cog(Color(bot))