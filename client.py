import sqlite3
import pandas as pd
import time
from util import Util
from datetime import datetime

class Client:


  def create_db(self):
    conn = sqlite3.connect('nrk.sqlite')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE PLAYERS
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AV          INT     NOT NULL,
            ROLE        TEXT     NOT NULL,
            HEALING        INT     NOT NULL,
            HEAL        INT     NOT NULL,
            BOT1        INT     NOT NULL,
            BOT2        INT     NOT NULL,
            BOT3        INT     NOT NULL,
            UPDATED_AT        INT     NOT NULL);''')
    cursor.close()

  def new_war(self):
    conn = sqlite3.connect('nrk.sqlite')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM PLAYERS')
    players = pd.read_csv('data.csv')

    for index, row in players.iterrows():
      name = row.loc['NAME']
      av = 3
      role = row.loc['ROLE']
      healing = 0
      heal = 2
      bot1 = 0
      bot2 = 0
      bot3 = 0
      updated = int(time.time())
      cursor.execute('''INSERT INTO PLAYERS (ID, NAME,AV,ROLE,HEALING,HEAL,BOT1,BOT2,BOT3,UPDATED_AT) \
        VALUES ({0}, '{1}', {2}, '{3}', {4}, {5}, {6}, {7}, {8}, {9})'''.format(index, name, av, role, healing, heal, bot1, bot2, bot3, updated))
      conn.commit()

    cursor.close()

  def bot_list(self):
    conn = sqlite3.connect('nrk.sqlite')
    cursor = conn.cursor()
    sb = "```"
    sb += "\n"
    sb += "Senopati\n"
    sb += "Av: H: FH: Update: Name\n"
    current_role = 'Senopati'
    total_ready = 0
    total_healing = 0
    for row in cursor.execute("SELECT ROLE, AV, HEALING, HEAL, UPDATED_AT, NAME from PLAYERS"):
      print(row[5])
      if (row[0] == current_role):
        first = datetime.fromtimestamp(row[4])
        second = datetime.today()
        diff = Util.hour_minute_tostring(Util.seconds_to_hour_minute((second - first).total_seconds()))
        total_ready += row[1]
        total_healing += row[2]
        sb += '''{0}   {1}  {2}   {3}\t{4}\n'''.format(row[1], row[2], row[3], diff, row[5])
      else:
        first = datetime.fromtimestamp(row[4])
        second = datetime.today()
        diff = Util.hour_minute_tostring(Util.seconds_to_hour_minute((second - first).total_seconds()))
        sb +="=====================================\n"
        sb += '''{0} Ready\n'''.format(total_ready)
        sb += '''{0} Healing\n'''.format(total_healing)
        sb += "\n"
        sb += "{0}\n".format(row[0])
        current_role = row[0]
        total_ready = row[1]
        total_healing = row[2]
        sb += '''{0}   {1}  {2}   {3}\t{4}\n'''.format(row[1], row[2], row[3], diff, row[5])
    sb +="=====================================\n"
    sb += '''{0} Ready\n'''.format(total_ready)
    sb += '''{0} Healing\n'''.format(total_healing)
    sb += "```"
    conn.commit()
    conn.close()
    return sb

  def update_bot(self, name, status):
    conn = sqlite3.connect('nrk.sqlite')
    cursor = conn.cursor()
    updated = int(time.time())
    sts = list(status)
    print(name)
    print(status)
    cursor.execute("UPDATE PLAYERS set AV = {0}, HEALING = {1}, HEAL = {2}, UPDATED_AT = {3} where NAME = '{4}'".format(sts[0], sts[1], sts[2], updated, name))
    conn.commit()
    retval = cursor.rowcount
    conn.close()
    return retval == 1

  def update_heal_bot(self, name):
    conn = sqlite3.connect('nrk.sqlite')
    cursor = conn.cursor()
    updated = int(time.time())
    for row in cursor.execute("SELECT HEALING from PLAYERS where NAME = '{0}'".format(name)):
      if (row[0] == 0):
        return
    conn.execute("UPDATE PLAYERS set AV = AV + 1, HEALING = HEALING - 1, UPDATED_AT = {0} where NAME = '{1}'".format( updated, name))
    conn.commit()
    conn.close()