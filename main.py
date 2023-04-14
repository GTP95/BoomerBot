# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from BoomerBot import BoomerBot


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = BoomerBot('Boomer', realname='Boomer')
    client.run('raccooncity.azzurra.org', tls=True, tls_verify=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
