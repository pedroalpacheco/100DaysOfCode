"""
Principio de teste

def calc(a, b):
    return a + b

resultado = calc(1,4)

print(resultado)
"""
def calc(a):
    return '1'

#print(calc(1,4))


if __name__ == '__main__':
    assert calc(1) == '1'
