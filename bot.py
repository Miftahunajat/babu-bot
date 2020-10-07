from dotenv import load_dotenv
from pathlib import Path
import discord
import os

load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def mirror(self, message):
        return message

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        else:
          inp = message.content
          await message.channel.send(self.mirror(inp).format(message))

client = MyClient()
client.run(os.getenv("TOKEN"))