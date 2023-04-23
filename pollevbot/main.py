from pollevbot import PollBot
from getpass import getpass


def main():
    user = input('username: ')
    password = getpass('password: ')
    host = 'johnousterhout268'

    # If you're using not using a UW or Stanford PollEv account,
    # use argument "login_type='pollev'"
    with PollBot(user, password, host, login_type='stanford', closed_wait=15) as bot:
        bot.run(daily_start='01:48:00', daily_end='01:50:00')


if __name__ == '__main__':
    main()
