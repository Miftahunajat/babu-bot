class Util:

  def seconds_to_hour_minute(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60
    return [int(hours), int(minutes)]

  def hour_minute_tostring(hours_minute):
    if (hours_minute[0] == 0):
      return "{0}m".format(hours_minute[1])
    else:
      return "{0}h{1}m".format(hours_minute[0], hours_minute[1])