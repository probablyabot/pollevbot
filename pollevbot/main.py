from pollevbot import PollBot
from getpass import getpass


def main():
    user = input('username: ')
    password = getpass('password: ')
    host = input('pollev host name: ')

    # If you're not using a UW or Stanford PollEv account,
    # add the argument "login_type='pollev'"
    with PollBot(user, password, host, login_type='stanford', closed_wait=10,
                 daily_start='11:30:00', daily_end='12:20:00') as bot:
        bot.run()


if __name__ == '__main__':
    main()
