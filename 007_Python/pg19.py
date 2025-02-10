# import datetime
# print(dir(datetime))

import pytz

from datetime import datetime
now=datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.min
second = now.second

new=datetime.now(pytz.timezone('US/EASTERN'))

# print(now ,"\n",day,"\n",month,"\n",year,"\n",hour,"\n",minute,"\n",second) 

print(new)