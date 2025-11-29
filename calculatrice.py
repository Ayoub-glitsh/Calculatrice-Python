def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"

# Exemple d'utilisation
print(addition(10, 5))
print(soustraction(10, 5))
print(multiplication(10, 5))
print(division(10, 5))
