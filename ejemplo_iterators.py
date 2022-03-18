## Iteradores son una estructura de datos para guardar datos INFINITOS
## iterables: Son objetos que podemos recorrer en un cliclo, lista, string... 
# estructuras divisibles en elementos unicos que puedo recorrer en un ciclo
## El iterador si puede recorrerse dentro del lenguaje

### Ejemplo guia

# Creando un iterador
from xml.dom.minidom import Element


my_list = [1,2,3,4,5]
my_iter = iter(my_list)

## Iterando un iterador
# con True se ejecuta el while infinitamente
#while True:
#    try:
#        element = next(my_iter)
#        print(element)
#    except StopIteration:
#        break 

##Para construir un iterador se construyen dos clases clase con dos metodos 


### Una clas que guarde todos los numeros pares (infinotos pares) o numeros pares hasta un maximo
class EvenNumber:
    """clase que implementa un iterador de todos los numeros pares, 
    o los numeros pares hasta un maximo"""

    def __init__(self, max=None):
        self.max = max

# contiene atributos para que el iterador funcione y retornar el objeto en si mismo
# convierte un iterable en iterador
    def __iter__(self):
        self.num =0 
        return self

# este metodo permite extraer cada elemento del iterador
# extraer todos los numeros pares 
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


EvenNumber(4)