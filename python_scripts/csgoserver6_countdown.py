"""
Automate to update every day.
"""
from datetime import date
from dateutil.relativedelta import relativedelta

d = datetime.date.today()
n = d + relativedelta(months=1)

EVENT = 'teamturtle_betalning'
YEAR = n.year
MONTH = n.month
DAY = 15
day_of_interest = datetime.date(YEAR, MONTH, DAY)
diff =DAY - d.day

if diff >=0:
           hass.states.set('sensor.' + EVENT, diff.days,{
               'unit_of_measurement': 'days',
               'friendly_name': 'Dagar till betalning Team Turtle',
               'icon': 'mdi:calendar'
           })
 
else:
    diff = day_of_interest - d

    hass.states.set('sensor.' + EVENT, diff.days,{
        'unit_of_measurement': 'days',
        'friendly_name': 'Dagar till betalning Team Turtle',
        'icon': 'mdi:calendar'
    })
