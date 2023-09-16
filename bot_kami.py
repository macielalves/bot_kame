import os
from typing import ParamSpecArgs

import discord
from discord.ext.commands import Bot, when_mentioned_or

from keepAlive import keep_alive

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.bans = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = True
intents.emojis = True
intents.emojis_and_stickers = True
intents.guild_messages = True
intents.guild_reactions = True
intents.guild_scheduled_events = True
intents.guild_typing = True
intents.guilds = True
intents.integrations = True
intents.invites = True
intents.messages = True
intents.reactions = True
intents.typing = True
intents.voice_states = True
intents.webhooks = True
intents.message_content = True
intents.presences = True
bot = Bot(when_mentioned_or('!'), intents=intents, description="Cuidado!")


@bot.event
async def on_ready():
  print(f"Logado como {bot.user.name}")


def run():
  try:
    keep_alive()
    bot.run(token)
  except Exception:
    if token:
      run()
    else:
      bot.run(str(token))
  print('Teminou a execução')
