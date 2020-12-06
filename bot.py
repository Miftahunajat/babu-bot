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

    async def hitung_draw(self, message):
      content = message.content
      messages = content.split(' ')
      if (len(messages) < 5):
        response = 'Lakukan hitung dengan command `hitungdraw [skor saat ini] [gain point] [skor musuh saat ini] [gain point] [jam menit xhym (opsional)]`'
        await message.add_reaction(self.cross)
        await message.channel.send(response.format(message))
      elif (len(messages) == 5):
        skor_kita = int(messages[1])
        gp_kita = int(messages[2])
        skor_musuh = int(messages[3])
        gp_musuh = int(messages[4])
        diff = int(abs(skor_kita - skor_musuh))
        diff_gp = int(abs(gp_kita - gp_musuh))
        hasil_menit = diff // diff_gp
        jam = int(hasil_menit // 60)
        menit = int(hasil_menit % 60)
        skor_kita_sekarang = skor_kita + gp_kita*hasil_menit
        skor_musuh_sekarang = skor_musuh + gp_musuh*hasil_menit
        
        response = '''Kemungkinan pada saat {0}h{1}m skor kita {2} dan skor musuh {3}'''.format(jam, menit, skor_kita_sekarang, skor_musuh_sekarang)

        await message.add_reaction(self.check)
        await message.channel.send(response.format(message))
      else:
        skor_kita = int(messages[1])
        gp_kita = int(messages[2])
        skor_musuh = int(messages[3])
        gp_musuh = int(messages[4])
        hour = int(messages[5].split('h')[0])
        minute = int(messages[5].split('h')[1].split('m')[0])
        minute = minute + hour*60
        skor_kita += gp_kita*minute
        skor_musuh += gp_musuh*minute
        str_jm = messages[5]

        response = '''Skor kita pada saat {0} adalah {1} dan skor musuh adalah {2}'''.format(str_jm, skor_kita, skor_musuh)

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
          elif (inps[0] == "hitungdraw"):
            await self.hitung_draw(message)

client = MyClient()
client.run(os.getenv("TOKEN"))