
### Ejemplo decorador
def decorador(func):
    def envoltura():
        print('Esto se aniade a mi funcion original')
        func()
    return envoltura

def saludo():
    print('Hola!')


saludo()
# output Hola!

saludo = decorador(saludo)
saludo()
