import pandas as pd

data = {
  'name': ['Bart', 'Lisa', 'Homer', 'Marge'],
  'age': [10, 8, 39, 36],
  'phone_number': ['555212231', '788222111', '242152423', '567890432'],
  'astrological_sign': ['capricorn', 'taurus', 'pisces', 'aquarius']
}

contacts = pd.DataFrame(data)
contacts