import re
from typing import Dict


def mayusculas(func):
    def wrapper(texto):
        result_dict = func(texto)
        if  len(result_dict['modulos'])==0:
            return {'que_es': result_dict['resultado'].upper(),'prom_mod': None } 
        return {'que_es': result_dict['resultado'].upper(),
        'prom_mod': sum(result_dict['modulos'])/len(result_dict['modulos']) }
       # print(result_dict)
    return wrapper 

@mayusculas
def esprimo(n: int)-> Dict[str,list] :
    lista = []
    result = ''
    result_noprimo = dict({'resultado': 'no es primo','modulos': []})
    if n <= 1: return result_noprimo 
    if n == 2: return dict({'resultado': 'Es primo','modulos': []})
 #   if n == 3: return True
    divisibles = list
    for i in range(2,n):
        #print('esta recorriendo el numero ', i)
        modulo = n%i
        if modulo==0:
            return result_noprimo
        lista.append(i)
    result_global = dict({'resultado': 'Es primo','modulos':lista})
   # print(result_global)
    return result_global

print(esprimo(2))
print(esprimo(12))
print(esprimo(271))
