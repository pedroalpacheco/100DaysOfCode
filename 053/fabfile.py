from fabric.api import run


def host_type():
    run('uname -a')


def ver_apache_debian():
    run('dpkg -l | grep apache2')

def ver_apache_rhn():
    run('rpm -qa | grep http')