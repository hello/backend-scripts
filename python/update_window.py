import datetime
from pytz import timezone
from pytz import common_timezones
import pytz
import operator

"""
This script displays the rolling window for OTA updates. The display shows time remaining in each
timezone that currently exists in the update window.

"""

updateZones = {}
pacific = timezone('US/Pacific')
loc_dt = pacific.localize(datetime.datetime.now())
today = datetime.date.today()
window_end = pacific.localize(datetime.datetime.combine(today, datetime.time(20, 0, 0)))

for tz in common_timezones:
    zone = timezone(tz)
    newTime = loc_dt.astimezone(zone)
    if 11 <= newTime.hour < 20:
        offset = datetime.datetime.now(pytz.timezone(str(newTime.tzinfo))).strftime('%z')
        tzNow = datetime.datetime.now(zone)
        endTime = zone.localize(datetime.datetime.combine(tzNow.date(), datetime.time(20, 0, 0)))
        delta = (endTime - tzNow)
        total_seconds = int(delta.total_seconds())
        hours, remainder = divmod(total_seconds,60*60)
        minutes, seconds = divmod(remainder,60)
        updateZones[str(hours) + str(minutes).zfill(2)] = newTime.tzinfo

for index, tzone in iter(sorted(updateZones.iteritems(), key=operator.itemgetter(0))):
    tztime = datetime.datetime.now(tzone)
    closeTime = tzone.localize(datetime.datetime.combine(tztime.date(), datetime.time(20, 0, 0)))
    timeleft = (closeTime - tztime)
    total_seconds = int(timeleft.total_seconds())
    hours, remainder = divmod(total_seconds,60*60)
    minutes, seconds = divmod(remainder,60)
    print('{}:{}:{}\t{}'.format(str(hours).zfill(2),str(minutes).zfill(2),str(seconds).zfill(2),str(tzone)))