import slixmpp
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='XMPP client.')
    parser.add_argument('-s', dest='server', help='Server address')
    parser.add_argument('-j', dest='jid', help='JID to use')
    parser.add_argument('-p', dest='psw', help='Password')

    args = parser.parse_args()

    if args.server is None:
        args.server = input('Server address: ')
    if args.jid is None:
        args.jid = input('Username: ')
    if args.psw is None:
        args.psw = input('Password: ')

