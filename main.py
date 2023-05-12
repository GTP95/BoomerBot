import sys
import argparse
from BoomerBot import BoomerBot

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('nick', help='Nickname to use', type=str)
    parser.add_argument('-r', '--realname', help='Real name to use', type=str)
    parser.add_argument('server', help='Server to connect to', type=str)
    parser.add_argument('channels', nargs='+',
                        help='Space-separated list of channels to join. If you are on Bash, remeber to escape the "#"',
                        type=str)

    args = parser.parse_args()

    if not args.realname:
        args.realname = args.nick

    client = BoomerBot(args.nick, realname=args.realname, listOfChannels=args.channels)
    client.run(args.server, tls=True, tls_verify=False)
