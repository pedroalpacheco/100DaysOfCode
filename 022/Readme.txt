Como usar:

http://www.fabfile.org/

No diretorio corresponente criar arquivo:
>fabfile.py

Conforme exemplo, o conteúdo de fabfile.py:

from fabric.api import run
def host_type():
    run('uname -a')

Executando:
No shell executar o comando:

fab --port 10022 -u pop -H servidor.algumlugar host_type(comando criado na função no arquivo fabfile.py)
fab --port 10022 -u pop -p ******** -H medusa.furb.br regras_firewall


Comandos:
fab --list = Lista os comandos disponíveis

Detalhes:
Para Fabric funcionar com python3 é necessário instalar:
>pip3 install fabric3

def regras_firewall():
    run('sudo /sbin/iptables -nvL')
#Colocar comando no sudoers do servidor"pop    ALL=NOPASSWD: /sbin/iptables -nvL , /bin/su - pop"