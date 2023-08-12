import selfcord
import asyncio
import random
import datetime
import time
from selfcord.ext import commands
from selfcord.ext.commands.context import Context

token = "OTQxODE3MzQxNDkzMjc2NzM0.G6nd6Z.pJqt2jRlgUKb3GJU1ukJYGR725_W8Y1e20x35s"
channels_id = [1056687422697644043, 1106746211521794158, 1052408373775179846, 1104596203565494453, 1115443611606200370]
char_name = "Zero Two"
user_id = 941817341493276734




class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix = commands.when_mentioned, user_bot = True, case_insensitive = True)

    async def on_ready(self) -> None:
        print(f"Bot funcionando e atuando na conta {self.user}")

        self.owner_ids = [self.user.id]

        await self.add_cog(Cog(self))

    async def on_message(self, message) -> None:
        await super().on_message(message)

        if message.content == f"<@{user_id}> fd" and message.channel.id in channels_id:
            current_time = time.strftime(r"%d.%m.%Y %H:%M:%S", time.localtime())
            name_log = message.author

            print(str(name_log) + " usou fd " +  current_time)
class Cog(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

        self.is_running = False
    
    @commands.command()
    async def fd(self, ctx: Context, *args: str) -> None:
        await ctx.message.add_reaction('✅')
        await ctx.send('$forcedivorce ' + str(char_name))
        await asyncio.sleep(2)
        await ctx.send('y')

        await asyncio.sleep(1)
        await ctx.send("O personagem " + str(char_name) + " foi divorciado.")

bot = Bot()
bot.run(token)
