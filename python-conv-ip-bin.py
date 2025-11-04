#!/usr/bin/env python3
# Programação de redes com python3
# Converter endereços IP em números binários

def conv_ip_bin(add_ip):
    """Converte um endereço IP para sua representação binária"""
    parts = add_ip.split('.')
    bins = [format(int(part), '08b') for part in parts]
    return '.'.join(bins)

add_ip = input('Digite um endereço IP ex:192.168.1.1;')
binary = conv_ip_bin(add_ip)
print(f"IP: {add_ip} -> Binário: {binary}")
