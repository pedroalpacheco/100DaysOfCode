#!/usr/bin/python
# -*- coding: utf-8 -*-

import commands
from datetime import datetime
import time

try:
    x = 0

    log = open('CONEXOES.txt', "a+")

    while (x < 1):
        time.sleep(12)
        agora = datetime.now()
        hoje = str(agora)
        porta = commands.getoutput("netstat  -n | grep :80 | wc -l")
        print("Conexoes:" + porta, "--" + hoje)
        registro = "Conexoes:" + porta
        log.writelines('\n' + registro + "-->" + hoje)

except KeyboardInterrupt:
    print('Encerrando o monitoramento!')

