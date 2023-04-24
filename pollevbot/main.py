from pollevbot import PollBot
from getpass import getpass


def main():
    user = input('username: ')
    password = getpass('password: ')
    host = input('pollev host name: ')

    # If you're using not using a UW or Stanford PollEv account,
    # use argument "login_type='pollev'"
    with PollBot(user, password, host, login_type='stanford', closed_wait=15) as bot:
        bot.run(daily_start='11:30:00', daily_end='12:20:00')


if __name__ == '__main__':
    main()
