
segundos = int(input())

hora = segundos / 3600
segundos %= 3600
minutes = segundos / 60
segundos %= 60
seconds = segundos
print("%d:%d:%d" % (hora, minutes, seconds))
