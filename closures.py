## Reglas para encontrar un Closure
# Debemos tener una Nested function (funciones anidadas)
# La Nested function debe referecniar un valor de la Scope superior
# La funcion que envuelve la Nested function debe retornarla tambien.

def make_division(n: int) -> int:
    def division_by(x):
        return x/n
    return division_by



division_by_3 = make_division(3)
print(division_by_3(18))
division_by_5 = make_division(5)
print(division_by_5(100))
division_by_18 = make_division(18)
print(division_by_3(54))



