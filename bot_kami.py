import os

import discord
from discord.ext.commands import Bot

token = os.environ['TOKEN']


class Kami:
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

  def __init__(self, ) -> None:
    super().__init__()
  pass


def main():
  pass
