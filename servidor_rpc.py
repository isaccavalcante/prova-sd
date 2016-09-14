#!/usr/bin/env python
#-*-coding: utf-8-*-
#Autor: Isac Cavalcante <isaccavalcante@alu.ufc.br>
import SimpleXMLRPCServer
import subprocess
import sys

class Funcoes(object):
    def obter_ip(self, interface):
        try:
            if interface == "externa":
                comando = subprocess.Popen(['curl icanhazip.com'], stdout=subprocess.PIPE, shell=True)
                ip, erro = comando.communicate()
            else:
                comando = subprocess.Popen(["ifconfig " + interface + " | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}' "], stdout=subprocess.PIPE, shell=True)
                ip, erro = comando.communicate()
            if ip == "":
                return "Não disponivel\n"
            else:
                return ip
        except Exception, msg:
            return "Ocorreu um erro.\n"

    def obter_info(self):
        try:
            comando = subprocess.Popen(["uname -a"], stdout=subprocess.PIPE, shell=True)
            info, erro = comando.communicate()
            return info
        except Exception, msg:
            return "Ocorreu um erro.\n"

    def ping(self, endereco):
        try:
            comando = subprocess.Popen(["ping -c 4 " + endereco], stdout=subprocess.PIPE, shell=True)
            estatisticas, erro = comando.communicate()
            return estatisticas
        except Exception, msg:
            return "Ocorreu um erro.\n"

    def obter_processos(self, aplicacao):
        try:
            comando = subprocess.Popen(["ps -aux | grep " + aplicacao], stdout=subprocess.PIPE, shell=True)
            processos, erro = comando.communicate()
            return processos
        except Exception, msg:
            return "Ocorreu um erro.\n"

def main(porta):
        funcoes = Funcoes()
        servidorRPC = SimpleXMLRPCServer.SimpleXMLRPCServer(('', porta))
        servidorRPC.register_instance(funcoes)
        servidorRPC.serve_forever()
  
if __name__ == "__main__":
    if len(sys.argv) == 2:
        porta = sys.argv[1]
        if porta.isdigit() == True:
            print "Servidor RPC iniciado..."
            main(int(porta))
            sys.exit(0)
    print "Uso: %s porta" % sys.argv[0]
