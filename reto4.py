
"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""


def is_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_fibonacci(num):
    fibonacci = 0
    actual = 0
    anterior = 0
    while fibonacci <= num:
        fibonacci = anterior + actual
        anterior = fibonacci
        actual += 1
        if num == fibonacci:
            return True
        elif fibonacci > num:
            return False
        

def is_primo(num):
    cantidad = 0
    if num == 1:
        return True
    for i in range(1, num+1):
        if num % i == 0:
            cantidad += 1
    if cantidad == 2:
        return True
    else:
        return False
        
        




if __name__ == "__main__":

    number = int(input("Escriba un numero: "))
    
    primo = is_primo(number)
    fibonacci = is_fibonacci(number)
    par = is_par(number)

    print(primo, fibonacci, par)

    if primo and fibonacci and par:
        print (f"El numero {number} es primo, fibonacci y es par")
    elif primo and not fibonacci and not par:
        print (f"El numero {number} es primo, no es fibonacci y es impar")
    elif primo and fibonacci and not par:
        print(f"El numero {number} es primo, es fibonacci y es impar")
    elif primo and not fibonacci and par:
        print(f"El numero {number} es primo, no es fibonacci y es par")
    elif not primo and fibonacci and par:
        print(f"El numero {number}  no es primo, es fibonacci y es par")
    elif not primo and not fibonacci and par:
        print(f"El numero {number} no es primo, no es fibonacci y es par")
    elif not primo and fibonacci and not par:
        print(f"El numero {number} no es primo, es fibonacci y es impar")


