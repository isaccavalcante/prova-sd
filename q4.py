#!/usr/bin/env python
#-*-coding: utf-8-*-
#Autor: Isac Cavalcante <isaccavalcante@alu.ufc.br>
import socket
import sys
import time

if len(sys.argv) != 2:
    print "Uso: python %s <arquivo>" % sys.argv[0]
    sys.exit()

try:
    arquivo = open(str(sys.argv[1]), 'r')
    for linha in arquivo:
        try:
            site = linha.split('\n')[0]
            ip = socket.gethostbyname(site)
            print "Endereço IP de %s: %s" % (site, ip)
        except socket.gaierror:
            time.sleep(5)
            print "DNS Timeout para %s" % site
    arquivo.close()
except IOError:
    print "Arquivo não encontrado."
