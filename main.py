#!/usr/local/bin/python

import sys
from BoomerBot import BoomerBot
import argparse

if __name__ == '__main__':
    #parse command line arguments
    parser = argparse.ArgumentParser(prog='BoomerBot', description='BoomerBot is a Python IRC bot that makes fun of a certain other bot')
    parser.add_argument('nickname', type=str, help='nickname to use')
    parser.add_argument('realname', type=str, help='realname to use')
    parser.add_argument('listOfChannels', nargs='+', help='list of channels to join')
    parser.add_argument('-s', '--server', type=str, default='raccooncity.azzurra.org', help='server to connect to')
    parser.add_argument('-p', '--password', type=str, default=None, help='password to use')
    args = parser.parse_args()

    client = BoomerBot(args.nickname, realname=args.realname, listOfChannels=args.listOfChannels, password=args.password)
    client.run(args.server, tls=True, tls_verify=False)
