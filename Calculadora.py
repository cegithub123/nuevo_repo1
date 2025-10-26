class Calculadora:
    def sumar(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError('Ambos parámetros deben ser números enteros o flotantes.')
        return a + b

    def restar(self, a, b):
        # Comentario 1
        # Comentario 2
        # comentario 3
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError('Ambos parámetros deben ser números enteros o flotantes.')
        return a - b


