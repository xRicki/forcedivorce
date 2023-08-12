import selfcord
import asyncio
import random
import datetime
import time
from selfcord.ext import commands
from selfcord.ext.commands.context import Context

token = "token"
channels_id = [channelid1, channelid2]
char_name = "Char Name"
user_id = 1111111111111111




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
