"""
Fibonacci con función Generator versión 2 - MEJORADO

Calcula hacia adelante

Tema: yield
       La sentencia yield suspende la ejecución de una función y devuelve 
       un valor al invocador, pero conserva suficiente estado para que la 
       función pueda reanudarse donde la dejó. Esto permite generar una serie 
       de valores a lo largo del tiempo, en lugar de calcularlos de una vez.
      
      if __name__ == "__main__":
       Sirve para ejecutar un bloque de código solo cuando el script se 
       ejecuta directamente.

Referencia: Classic Computer Science Problems with Python
            pag 12   fib9.py
            
            https://www.geeksforgeeks.org/python/use-yield-keyword-instead-return-keyword-python/

Editor: Roberto Méndez Méndez

Created on Fri Jun 14 2024
Edited: Apr 29 2025 (Versión Original)
Edited: Nov 9 2025 (Versión Mejorada) 
"""
from typing import Generator

def fibGen(n: int) -> Generator[int, None, None]:
    
    # ====================================================================
    # <<< MEJORA APLICADA (ACTIVIDAD 2, PUNTO V) >>>
    # 
    # Cambio Aplicado: 
    #   Se eliminaron las llamadas iniciales 'yield 0' y 'if n > 0: yield 1' 
    #   separadas del código original. La lógica se consolidó en un único 
    #   bucle 'for _ in range(n + 1):' para generar la secuencia.
    # 
    # Función del Cambio: 
    #   Simplificación y Robustez del Código: La nueva estructura maneja 
    #   los casos base (F(0) y F(1)) dentro del bucle principal de forma 
    #   elegante y concisa, sin lógica condicional externa.
    # 
    # Ventaja: 
    #   Mantiene la eficiencia de tiempo O(n) y la eficiencia de espacio O(1), 
    #   pero reduce las líneas de código y mejora la Calidad y Mantenibilidad.
    #   Se mantiene la esencia (cálculo iterativo 'hacia adelante' y uso de yield).
    # ====================================================================
    
    # 1. Validación de Entrada
    if n < 0:
        return # Si n es negativo, no genera nada.
    
    # 2. Inicialización de variables para el cálculo O(1) en espacio
    # 'a' guarda F(i-1) y 'b' guardará el siguiente F(i)
    a: int = 0
    b: int = 1
    
    # El bucle ahora corre n+1 veces para generar los números desde la posición 0 hasta n.
    for _ in range(n + 1): 
        
        # 3. Generación del valor actual
        # Se devuelve el F(i) actual (primero 0, luego 1, luego 1, luego 2...)
        yield a
        
        # 4. Actualización para el siguiente paso (F(i+1) = F(i) + F(i-1))
        # Esta es la esencia O(1) del cálculo iterativo.
        a, b = b, a + b
        

if __name__ == "__main__":
    n = int(input("¿Fibonacci hasta la posición?: "))
    for i in fibGen(n):    
        print(i)