from Calculadora import Calculadora
class Main:
    def __init__(self):
        self.calculadora = Calculadora()
    
    def ejecutar_pruebas(self):
        """Ejecuta las pruebas de los métodos sumar y restar con valores por defecto"""
        print("=== PRUEBAS DE LA CALCULADORA ===")
        
        # Valores por defecto para las pruebas
        valores_prueba = [
            (10, 5),      # Enteros
            (15.5, 3.2),  # Flotantes
            (100, 25.5),  # Entero y flotante
            (0, 0),       # Ceros
            (-10, 5),     # Números negativos
        ]
        
        print("\n--- PRUEBAS DE SUMA ---")
        for i, (a, b) in enumerate(valores_prueba, 1):
            try:
                resultado = self.calculadora.sumar(a, b)
                print(f"Prueba {i}: {a} + {b} = {resultado}")
            except TypeError as e:
                print(f"Prueba {i}: Error en suma - {e}")
        
        print("\n--- PRUEBAS DE RESTA ---")
        for i, (a, b) in enumerate(valores_prueba, 1):
            try:
                resultado = self.calculadora.restar(a, b)
                print(f"Prueba {i}: {a} - {b} = {resultado}")
            except TypeError as e:
                print(f"Prueba {i}: Error en resta - {e}")
        
        print("\n--- PRUEBAS DE VALIDACIÓN (ERRORES ESPERADOS) ---")
        # Pruebas con tipos incorrectos para verificar validación
        try:
            self.calculadora.sumar("5", 3)
        except TypeError as e:
            print(f"Error esperado en suma con string: {e}")
        
        try:
            self.calculadora.restar(10, "abc")
        except TypeError as e:
            print(f"Error esperado en resta con string: {e}")


if __name__ == "__main__":
    main = Main()
    main.ejecutar_pruebas()