#!/usr/bin/env python3
# Programação de redes com python3
# https://pypi.org/project/dnspython/
# Consulta básica Servidores de DNS

import dns.resolver

add_name = input ('Digite o nome de um domínio Ex:www.example.com:')

# Loop para procurar diferentes registros DNS
def ns_lookup(name):
    for qtype in 'A', 'AAAA', 'CNAME', 'MX', 'NS' :
        answer = dns.resolver.resolve(name, qtype, raise_on_no_answer=False)
        if answer.rrset is not None:
            print (answer.rrset)

if __name__ == '__main__':
    ns_lookup(add_name)
