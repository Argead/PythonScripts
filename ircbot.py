#!/usr/bin.pthon3
"""
IRC chat bot.
"""

import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'chat.freenode.net' #TODO:replace this with user input.
channel = '##bot-testing' #TODO" replace this with user input.
botnick = 'pythonBot' #TODO: replace this with user input.
adminName = 'admin' #TODO: replace this with user input.
exitcode = 'bye {}'.format(botnick)

ircsock.connect((server, 6667)) #TODO: replace magic number 6667 with const.
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8"))
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot

def join_channel(target_channel):
    ircsock.send(bytes("JOIN " + target_channel + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find('End of /NAMES list.') == -1:
        ircmsg = sock.recv(2048).decode('UTF-8')
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

def ping():
    ircsock.send(bytes("PONG :pingis\n", "UTF-8"))

def sendmsg(msg, target=target_channel):
    ircsock.send(bytes("PRIVMSG " + target + " :" + "\n", "UTF-8"))

def main():
    join_channel(chanel)
    while True:
        ircmsg = ircsock.recv(2048).decode('UTF-8')
        ircmsg = ircmsg.strip('\r\n')
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!', 1)[0][1:]
            message = ircmsg.split('PRIVMAG',1)[1].split(':', 1)[1]
            
            if len(name) < 17:
                if message.find('Hi ' + botnick) != -1:
                    sendmsg("Hello " + name + "!")
                
                if message[:5].find('.tell') != -1:
                    target = message.split(' ', 1)[1]
                    if target.find(' ') != -1:
                        message = target.split(' ', 1)[1]
                        target = target.split(' ')[0]
                    else:
                        target = name
                        message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."
                    sendmsg(message, target)

                if name.lower() == adminname.lower() and message.rstrip() == exitcode:
                    sendmsg("oh...okay. :'(")
                    ircsock.send(bytes("QUIT \n", "UTF-8"))
                    return
            else:
                if ircmsg.find('PING :') != -1:
                    ping()
                    
                    
 main()
