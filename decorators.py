from datetime import datetime
def execution_time(func):
    def wrapper(*args,**kwards):
        initial_time = datetime.now()
        func(*args,**kwards) # ejecutar la funcion
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print('Pasaron ' + str(time_elapse.total_seconds()) + ' segundos')
    return wrapper # se debe retornar el decorador

@execution_time # se llama la funcion
def random_func():
    for _ in range(1,100000): # for con _ para que no muestre lo que va recorriendo
        pass


## Otros ejemplos de funciones utilizando el decorador

@execution_time
def suma(a: int,b: int)-> int:
    return print(a+b)

@execution_time
def saludo(nombre="Marcela"):
    print('Hola ' + nombre)

random_func()
suma(5,5)
saludo()










