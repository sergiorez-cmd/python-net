#!/usr/bin/env python3
# Programação de redes com python3
# Resolver endereço IP e FQDN de um host na Internet

import socket

if __name__ == '__main__':
    hostname = input('Digite um endereço de host www.example.com:')
    address = socket.gethostbyname(hostname)
    fqdn = socket.getfqdn(hostname)
    print ('O endereço IP de {} é {} FQDN: {}'.format(hostname, address, fqdn))
