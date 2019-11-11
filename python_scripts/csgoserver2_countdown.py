"""
Script to create a sensor displaying the number of days until some event.
Automate to update every day.
"""

EVENT = 'thorax_betalning'
DAY = 1

day_of_interest = datetime.datetime(DAY)
now = datetime.datetime.now()
diff = day_of_interest - now

hass.states.set('sensor.' + EVENT, diff.days,{
    'unit_of_measurement': 'days',
    'friendly_name': 'Dagar till betalning Thorax',
    'icon': 'mdi:calendar'
})
