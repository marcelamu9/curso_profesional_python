def esprimo(n: int)-> bool:
    cantidad = 0
    if n <= 1: return False
    if n == 2: return True
 #   if n == 3: return True
    for i in range(2,n):
        print('esta recorriendo el numero ', i)
        modulo = n%i
        if modulo==0:
            print('no es primo')
            return False
    return True
    

def run():
    print(esprimo(271))


if __name__ == '__main__':
    run()