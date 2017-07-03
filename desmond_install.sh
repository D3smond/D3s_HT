#!/bin/bash

#estou aqui so te observando e hackeando sua conexao '-'

echo """

██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
                                                          
 +--------------------------------------------------+
 | [+] instalando dependecias para uso do script... |
 +--------------------------------------------------+
 | [+] version 0.0.1 | Telegram: @desmondelite      |
 ====================================================
 + [-] support pentest: linux && windows(bash_ubuntu)   +
 ----------------------------------------------------                                                                                                                  
                                                         """

apt-get update
apt-get install python
apt-get install python-pip
apt-get install python-mechanize
apt-get install git
apt-get install build-essential libssl-dev libffi-dev python-dev
apt-get install libbind9-90 libdns100 libisc95 libisccc90 libisccfg90 liblwres90
apt-get install hydra
apt-get install medusa
easy_install zoomeye-SDK
git clone https://github.com/s0m30ne/zoomeye.git
cd zoomeye/
python setup.py install
cd ..
pip install python-whois
pip install pexpect
pip install shodan
pip install argparse
pip install -U cryptography
pip install --upgrade setupext-pip
easy_install shodan
easy_install -U shodan
pip install twilio
pip install argcomplete
pip -v install pycurl --upgrade
pip install paramiko
#wget https://www.dropbox.com/s/gje56ma6jocc3l0/pxssh.py
#wget https://www.dropbox.com/s/74oyw83rggqfdet/des_ht.py

python des_ht.py --help
