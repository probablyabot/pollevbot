# pollevbot

**pollevbot** is a bot that automatically responds to polls on [pollev.com](https://pollev.com/). 
It continually checks if a specified host has opened any polls. Once a poll has been opened, 
it submits a random response. 

Requires Python 3.7 or later.
## Dependencies

[Requests](https://pypi.org/project/requests/), 
[BeautifulSoup](https://pypi.org/project/beautifulsoup4/). 

[APScheduler](https://pypi.org/project/APScheduler/) to deploy to Heroku.

## Usage

Install `pollevbot`:
```
pip install pollevbot
```

Set your username, password, and desired poll host (for example, using `input()`):
```python
user = input('username: ')
password = input('password: ')
host = input('pollev.com url extension: ')
```

And run the script.
```python
from pollevbot import PollBot

user = input('username: ')
password = input('password: ')
host = input('pollev.com url extension: ')

# If you're not using a UW or Stanford PollEv account,
# add the argument "login_type='pollev'"
with PollBot(user, password, host) as bot:
    bot.run()
```
Alternatively, you can clone this repo and run [pollevbot/main.py](pollevbot/main.py),
which will read username, password, and host from `input()`. The input for
password will be hidden.

**Note:** To hide password input, make sure you are running the program from a
terminal window and not an IDE. If you run from an IDE, you will see
```
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
```
and your password will **not** be hidden.

### Usage for macOS with daily start/end time feature:
In [main.py](pollevbot/main.py), use the optional `daily_start` and
`daily_end` arguments in `PollBot()` to set the desired daily start and end
time. Format using 24 hour time, HH:MM:SS. Then run
```bash
caffeinate python -m pollevbot.main
```
This will suspend the python program from running outside the specified times,
while also preventing the computer from sleeping. To stop the program, simply
Ctrl-C. Note that `caffeinate` only prevents idle sleep, so make sure you
don't close the lid or manually put the computer to sleep.

The purpose of this feature, as opposed to deploying via Heroku (detailed
below), is to avoid having to authenticate with Duo every time the program
runs. With this feature, one can schedule the program to run, log in
beforehand, and forget about it.

## Heroku

**pollevbot** can be scheduled to run at specific dates/times (UTC timezone) using [Heroku](http://heroku.com/):

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/danielqiang/pollevbot)

Required configuration variables:

* `DAY_OF_WEEK`: [cron](https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html) string
specifying weekdays to run pollevbot (e.g. `mon,wed` is Monday and Wednesday).
* `HOUR`: [cron](https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html) string
(UTC time) specifying which hours to run pollevbot.
* `LIFETIME`: Time to run pollevbot before terminating (in seconds). Set to `inf` to run forever.
* `LOGIN_TYPE`: Login protocol to use (either `uw` or `pollev`).
* `MINUTE`: [cron](https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html) string
specifying what minutes to run pollevbot.
* `PASSWORD`: PollEv account password.
* `POLLHOST`: PollEv host name.
* `USERNAME`: PollEv account username.

**Example**

Suppose you want to answer polls made by poll host `teacher123` every Monday and Wednesday 
from 11:30 AM to 12:30 PM PST (6:30 PM to 7:30 PM UTC) in your timezone on your UW account. To do this, set the config 
variables as follows:

* `DAY_OF_WEEK`: `mon,wed`
* `HOUR`: `18`
* `LIFETIME`: `3600`
* `LOGIN_TYPE`: `uw`
* `MINUTE`: `30`
* `PASSWORD`: `yourpassword`
* `POLLHOST`: `teacher123`
* `USERNAME`: `yourusername`

Then click `Deploy App` and wait for the app to finish building. 
**pollevbot** is now deployed to Heroku! 

## Disclaimer

I do not promote or condone the usage of this script for any kind of academic misconduct 
or dishonesty. I wrote this script for the sole purpose of educating myself on cybersecurity 
and web protocol automation, and cannot be held liable for any indirect, incidental, consequential, 
special, or exemplary damages arising out of or in connection with the usage of this script.
