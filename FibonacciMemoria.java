/**
 * Creado por Eder Yañez Díaz
 * Lenguaje: Java
 * Versión de Java: 25 (Asumida por el contexto de la tarea)
 * Fecha de Creación: 10 de Noviembre de 2025
 * * Tema: Fibonacci Recursivo con Memoización (Hashtable)
 * Objetivo: Análogo del fibonacci-MemDic1.py de Python.
 * * NOTA IMPORTANTE: Esta implementación recursiva, aunque es O(n), 
 * causará un 'StackOverflowError' para valores de 'n' muy grandes (e.g., n > 7000) 
 * debido a la limitación de la Pila de Llamadas de Java (Call Stack).
 */
import java.math.BigInteger;
import java.util.Hashtable;

public class FibonacciMemoria {

    // Hashtable es la estructura de datos para la MEMOIZACIÓN (el "Diccionario" de Python)
    // Clave (Integer): La posición 'n' de Fibonacci.
    // Valor (BigInteger): El valor de F(n), usando BigInteger por si n es muy grande.
    private static final Hashtable<Integer, BigInteger> cache = new Hashtable<>();

    // Bloque estático para inicializar el cache con los casos base
    static {
        cache.put(0, BigInteger.ZERO); // F(0) = 0
        cache.put(1, BigInteger.ONE);  // F(1) = 1
    }

    /**
     * Función Fibonacci Recursiva con Memoización (O(n)).
     * @param n La posición a calcular.
     * @return El valor de Fibonacci en la posición n.
     */
    public static BigInteger fibonacci(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("La posición debe ser no negativa.");
        }

        // 1. MEJORA: Checar si el resultado ya está en el cache
        if (cache.containsKey(n)) {
            // Si ya se calculó, se devuelve inmediatamente.
            return cache.get(n);
        }

        // 2. Si no está en el cache, se calcula recursivamente: F(n) = F(n-1) + F(n-2)
        // La complejidad O(2^n) se transforma en O(n) porque el resultado de 
        // cada subproblema (fibonacci(n-1) y fibonacci(n-2)) se guarda
        BigInteger resultado = fibonacci(n - 1).add(fibonacci(n - 2));

        // 3. MEJORA: Guardar el resultado en el cache antes de devolverlo
        cache.put(n, resultado);

        return resultado;
    }

    // Adaptación del main de los códigos originales para demostrar la eficiencia
    public static void main(String[] args) {
        // Prueba con una posición grande que fallaría instantáneamente en los códigos originales.
        int posicionAProbar = 1000; 

        System.out.println("--- Fibonacci con Memoización (Hashtable y BigInteger) ---");
        System.out.println("Calculando F(" + posicionAProbar + ") de forma O(n)...");

        long startTime = System.currentTimeMillis();
        BigInteger resultado = fibonacci(posicionAProbar);
        long endTime = System.currentTimeMillis();

        System.out.println("F(" + posicionAProbar + ") = " + resultado);
        System.out.println("Tiempo de ejecución: " + (endTime - startTime) + " ms");
    }
}