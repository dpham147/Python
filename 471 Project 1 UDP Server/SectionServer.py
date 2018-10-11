#!/usr/bin/env python3

import sys
from socket import *
import hashlib

serverPort = 7037


def md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def retrieve_section_list(socket, client):
    returnMessage = bytes('Section List', 'utf-8')
    socket.sendto(returnMessage, client)


def retrieve_section_content(section_num, socket, client):
    returnMessage = bytes('Section Contents of ' + str(section_num), 'utf-8')
    socket.sendto(returnMessage, client)


# def usage(program):
#    sys.exit(f'Usage: python3 {program} [FILE] ')


serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = str(message.upper())
    print(message[2:-1])

    if message[2:-1] == 'LIST':
        retrieve_section_list(serverSocket, clientAddress)
    elif message[2:9] == 'SECTION':
        if int(message[10:-1]):
            retrieve_section_content(int(message[10:-1]), serverSocket, clientAddress)
    else:
        returnMessage = bytes('Invalid Request', 'utf-8')
        serverSocket.sendto(returnMessage, clientAddress)

'''
if __name__ == '__main__':
    if len(sys.argv) != 1:
        usage(sys.argv[0])
    sys.exit(main(*sys.argv[1:]))
'''
