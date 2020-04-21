#!/usr/bin/env python3

import sys
import socket
import hashlib
import time

DEFAULT_PORT = 7037

SIZE_1_KiB = 1024
SIZE_32_KiB = 32 * SIZE_1_KiB

# per <https://en.wikipedia.org/wiki/User_Datagram_Protocol>
MAX_TCP_PAYLOAD = 65535


class Section:
    MAX_SECTION_SIZE = SIZE_32_KiB

    def __init__(self, num, size, digest):
        self.num = int(num)
        self.size = int(size)
        self.digest = digest
        self.from_byte = self.num * self.MAX_SECTION_SIZE
        self.to_byte = (self.num + 1) * self.MAX_SECTION_SIZE


def md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def parse_address(addr):
    components = addr.split(':', maxsplit=1)
    hostname = components[0]
    port = DEFAULT_PORT if len(components) == 1 else int(components[1])

    return hostname, port


def myreceive(sock, message, messageLen, hostname, port):
    chunks = []
    bytes_recd = 0
    print(f'\nOpen socket for { message }')

    if not sock.send(message.encode()): # Connection Shut down
        sock.connect((hostname, port))
        sock.send(message.encode())
    i
    while bytes_recd < messageLen:

        chunk = sock.recv(min(messageLen - bytes_recd, 2048))
        print('here')
        if chunk == b'':
            print('DISCONNECTED')
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)

    sock.close()
    print('Closing socket')

    return b''.join(chunks)


def send_message(sock, message, hostname, port, size):
    data = myreceive(sock, message, size, hostname, port)
    return data


def list_sections(sock, hostname, port):
    message = 'LIST'
    sock.send(message.encode())

    chunks = []
    bytes_recd = 0
    chunk = sock.recv(2048)
    chunks.append(chunk)
    bytes_recd = bytes_recd + len(chunk)
    while True:
        if chunk == b'':
            break
        chunk = sock.recv(2048)
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    response = b''.join(chunks)

    print(response.decode(), end="\n\n")
    lines = response.decode().splitlines()

    file_digest = lines.pop(0)
    sections = set()
    total_size = 0

    for line in lines:
        columns = line.split(maxsplit=2)

        sec = Section(*columns)
        sections.add(sec)
        total_size += sec.size

    sock.close()

    return file_digest, sections, total_size


def download_section(sock, section, hostname, port):
    response = send_message(sock, f'SECTION {section.num}', hostname, port, section.size)
    return response


def usage(program):
    sys.exit(f'Usage: python3 {program} HOST[:PORT] FILE')


def main(address, filename):
    hostname, port = parse_address(address)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
    print("RETRIEVING LIST...")
    expected_file_digest, sections, total_size = list_sections(sock, hostname, port)
    file_contents = bytearray(total_size)
    progress_counter = 0.0

    for section in sections:
        print(f'section {section.num}...', end='')

        data = download_section(sock, section, hostname, port)
        size = len(data)
        digest = md5(data)
        corruption = True

        while(corruption == True):
            if size != section.size:
                progress = (progress_counter/ (len(sections))) * 100
                print(f'size {size}, expected {section.size}, \nRetrying section {section.num}... {progress:.2f} %')
                data = download_section(section, hostname, port)
                size = len(data)
                digest = md5(data)
            elif digest != section.digest:
                progress = (progress_counter/ (len(sections))) * 100
                print(f'digest {digest}, expected {section.digest}, \nRetrying section {section.num}... {progress:.2f} %')
                data = download_section(section, hostname, port)
                size = len(data)
                digest = md5(data)
            else:#No Corruption
                progress_counter += 1.0
                file_contents[section.from_byte:section.to_byte] = data
                progress = (progress_counter/ (len(sections))) * 100
                print(f'section {section.num}... ok {progress:.2f} %')
                corruption = False


    file_digest = md5(file_contents)
    if file_digest != expected_file_digest:
        print(f'{filename}: digest {file_digest}, expected {expected_file_digest}')
    else:
        with open(filename, 'wb') as f:
            f.write(file_contents)
            print("File Received.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage(sys.argv[0])

    sys.exit(main(*sys.argv[1:]))
