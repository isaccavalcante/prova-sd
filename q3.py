#!/usr/bin/env python
#-*-coding: utf-8-*-
#Autor: Isac Cavalcante <isaccavalcante@alu.ufc.br>
import sys
from ftplib import FTP
from socket import *

if len(sys.argv) != 2:
    print "Uso: python %s <servidor_ftp>" % str(sys.argv[0])
    sys.exit()

servidor = str(sys.argv[1])
# ftp.br.debian.org

try:
    ftp = FTP(servidor)
    ip = gethostbyname(servidor)
    porta = ftp.port
    print ftp.login()
    print "Conectado com %s na porta %d" % (ip, porta)
except Exception, msg:
    print "Ocorreu o seguinte erro: "
    print msg[1]


