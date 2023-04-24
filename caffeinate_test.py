from time import sleep
from datetime import datetime

for i in range(12):
    print('Current datetime: ', datetime.now())
    print('Sleeping for 1 hour.')
    sleep(3600)
