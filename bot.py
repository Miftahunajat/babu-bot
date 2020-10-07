from dotenv import load_dotenv
from pathlib import Path
import discord
import os
from datetime import datetime, timedelta

load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class MyClient(discord.Client):

    check = '✅'
    cross = '❌'
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def mirror(self, message):
        return message

    def hours_minute_from_now(self, hour, minute):
      hours_from_now = datetime.now() + timedelta(hours=hour) + timedelta(minutes=minute)
      return '{:%H :%M}'.format(hours_from_now)

    async def hitung_instant(self, message):
        content = message.content
        messages = content.split()
        if (len(messages) < 4):
          response = 'Lakukan hitung dengan command `hitung [skor saat ini] [gain point] [skor instant]`'
          await message.add_reaction(self.cross)
          await message.channel.send(response.format(message))
        else:
          perbedaan = int(messages[3]) - int(messages[1])
          hasil_menit = perbedaan / int(messages[2])
          jam = int(hasil_menit // 60)
          menit = int(hasil_menit % 60)

          response = '''Kemungkinan kita akan Instant dalam {0} Jam {1} Menit\natau dalam jam {2}
          '''.format(jam, menit, self.hours_minute_from_now(jam, menit))

          await message.add_reaction(self.check)
          await message.channel.send(response.format(message))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        else:
          inp = message.content
          inps = inp.split(" ")
          if (inps[0] == "hitung"):
              await self.hitung_instant(message)

client = MyClient()
client.run(os.getenv("TOKEN"))