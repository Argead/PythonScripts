#!/usr/bin.pthon3
"""
Command Line IRC chat bot.
"""
import argparse
import socket


parser = argparse.ArgumentParser(description='Basic IRC chat bot')
parser.add_argument('server', type=int, help='Name of IRC server to connect to')
parser.add_argument('channel', type=int, help='Name of IRC channel to use')
parser.add_argument('botname', type=int, help='Nickname for bot to use on the channel')
parser.add_argument('-a', '--admin', type=int, default='admin', help='Name to use for admin; defaults to "admin"')
args = parser.parse_args()


IRC_PORT = 6667
EXITCODE = 'bye {}'.format(args.botname)


def join_channel(target_channel):
    ircsock.send('JOIN {}\n'.format(target_channel).encode('UTF-8'))
    ircmsg = ''
    while ircmsg.find('End of /NAMES list.') == -1:
        ircmsg = sock.recv(2048).decode('UTF-8')
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

def ping():
    ping_msg = 'PONG :pingis\n'
    ircsock.send(ping_msg.encode('UTF-8'))

def sendmsg(msg, target=args.channel):
    private_msg = 'PRIVMSG {} :{}\n'.format(target, msg)
    ircsock.send(private_msg.encode('utf-8'))    
    
def start_server():
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((args.server, IRC_PORT))
    ircsock.send('USER {} {} {} {}\n').format(args.botname, args.botname, args.botname, args.botname).encode('UTF-8')
    ircsock.send('NICK {}\n'.format(args.botname).encode('UTF-8'))
    join_channel(args.channel)
    while True:
        ircmsg = ircsock.recv(2048).decode('UTF-8')
        ircmsg = ircmsg.strip('\r\n')
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!', 1)[0][1:]
            message = ircmsg.split('PRIVMAG',1)[1].split(':', 1)[1]
            
            if len(name) < 17:
                if message.find('Hi ' + botnick) != -1:
                    sendmsg('Hello {}!'.format(name))
                if message[:5].find('.tell') != -1:
                    target = message.split(' ', 1)[1]
                    if target.find(' ') != -1:
                        message = target.split(' ', 1)[1]
                        target = target.split(' ')[0]
                    else:
                        target = name
                        message = 'Error. Msg format must be [target] [message].'
                    sendmsg(message, target)

                if name.lower() == args.admin.lower() and message.rstrip() == exitcode:
                    ircsock.send(bytes("QUIT \n", "UTF-8"))
                    ircsock.close()
                    return
            else:
                if ircmsg.find('PING :'):
                    ping()
                    
                    
if __name__ == '__main__':
    start_server()
