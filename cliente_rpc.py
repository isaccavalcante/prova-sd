#!/usr/bin/env python
#-*-coding: utf-8-*-
#Autor: Isac Cavalcante <isaccavalcante@alu.ufc.br>
import sys
import xmlrpclib
  
def main(servidor):
    opcoes = ("1. Consultar endereços IP do servidor.",
            "2. Consultar informações sobre a máquina do servidor.",
            "3. Pingar a partir do servidor.",
            "4. Consultar processos de uma aplicacao do servidor." ,
            "5. Sair" )
    servidor = xmlrpclib.ServerProxy(str(servidor)) #Conexao RPC com o Servidor

    while True:
        for opcao in opcoes:
            print opcao
        entrada = raw_input("Digite a opcão: ", )
        
        if entrada == "1":
            interface = raw_input("Digite a interface que deseja consultar (wlan0, eth0, externa): ")
            ip = servidor.obter_ip(interface)
            print "Endereço ip da interface %s: " % interface
            print ip

        elif entrada == "2":
            print "Informações sobre servidor: "
            teste = servidor.obter_info()
	    print teste

        elif entrada == "3":
            site = raw_input("Digite um site para pingar: ")
            resultado = servidor.ping(site)
            print "Resultado do ping do servidor: "
            print resultado
        
        elif entrada == "4":
            aplicacao = raw_input("Digite o nome da aplicacao referente ao processo: ")
            resultado = servidor.obter_processos(aplicacao)
            print "Processos de %s" % aplicacao
            print resultado

        elif entrada == "5":
            print "Saindo..."
            break

if __name__ == "__main__":
        if len(sys.argv) == 2:
                    main(sys.argv[1])
        else:
                    print "Uso: %s host\nExemplo: %s http://localhost:1000" % (sys.argv[0], sys.argv[0])
