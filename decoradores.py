def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura 



@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))

### Ejemplo decorador
def decorador(func):
    def envoltura():
        print('Esto se aniade a mi funcion orgiginal')
        func()
    return envoltura

def saludo():
    print('Hola!')


saludo()
# output Hola!

saludo = decorador(saludo)
saludo()