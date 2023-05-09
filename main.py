import sys
from BoomerBot import BoomerBot

if __name__ == '__main__':
    client = BoomerBot(sys.argv[1], realname='Boomer', listOfChannels=sys.argv[2:])
    client.run('raccooncity.azzurra.org', tls=True, tls_verify=False)
