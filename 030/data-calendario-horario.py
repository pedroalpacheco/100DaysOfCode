from datetime import datetime

import time

now_1 = datetime.now()
print (" Horario agora", now_1)
time.sleep(5)
now_2 = datetime.now()
print (" Horario depois de 5 segundos", now_2)
print (" A diferença é :", (now_2 - now_1).seconds)