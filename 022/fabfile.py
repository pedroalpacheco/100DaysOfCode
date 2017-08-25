from fabric.api import run

def host_type():#aqui é o comando que será executado na linha de comando
    run('uname -a')

def horas():
    run('date')

def regras_firewall():
    run('sudo /sbin/iptables -nvL ')

def log_erro():
    run('cat /var/log/apache2/erro.log')