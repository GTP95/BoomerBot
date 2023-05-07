import sys
from BoomerBot import BoomerBot

if __name__ == '__main__':
    client = BoomerBot('Boomer', realname='Boomer', listOfChannels=sys.argv[1:])
    client.run('raccooncity.azzurra.org', tls=True, tls_verify=False)
