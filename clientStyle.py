#this class is imported into main to reduce clutter, might make it alternatively run as a role bot later, we will see!
import discord

class Salticidae(discord.Client):
  #runs the discord.Client init function passing through any arguments
  #this creates our own client object essentially, named Salticidae
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
  async def on_ready(self):
    print(f'Ready as: {client.user}')

  async def on_message(self, message):
    if message.author == client.user:
      return
    if message.content.startswith("yo"):
      await message.channel.send("yo")

intent = discord.Intents.default()
client = Salticidae(intents=intent)
