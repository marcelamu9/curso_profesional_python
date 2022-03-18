## Sucesion Fibonacci 0 1 1 2 3 5 8 13 21 34 55 89 144
## cada numero es el resultado de sumar los dos numeros anteriores
## se puede guardar esta sucesion completa ...

import time

class FiboIter():

    def __init__(self, max:int):
        self.max = max

    ## Esta clase va a tener dos metodos necesarios para crear iteradores __iter__
    ## todos los metodos de una clase necesitan el parametro self para poder existir __next__
    def __iter__(self):
        self.n1= 0
        self.n2 = 1
        self.counter = 0
        return self
        
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else: 
            if self.counter <= self.max:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration

# primera vuelta, self.counter=0 ==> fibo es 0
# segunda vuelta, self.counter = 1 ==> fibo es 1 
# tercera vuelta,  self.counter = 2, self.aux = 1, self.n1=1 y self.n2= 1  ==> fibo es 1 
# cuarta vuelta,  self.counter = 3, self.aux = 2, self.n1=1 y self.n2= 2  ==> fibo es 2
# quinta vuelta,  self.counter = 4, self.aux = 3, self.n1=2 y self.n2= 3  ==> fibo es 3

# instanciar la clase, apartir de la clase creo un iterador
if __name__ == '__main__':
    fibonacci = FiboIter

    for element in fibonacci(8):
        print(element)
        time.sleep(1) # pausar la impresion del for para alcanzar a ver los numeros
