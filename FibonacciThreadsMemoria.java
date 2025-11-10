/**
 * Curso: Programación / MCA 1
 * * Implementación Mejorada: Fibonacci con Threads y Memoización (Hashtable)
 * * Objetivo: Reducir la complejidad O(2^n) del código original a O(n) usando Memoización.
 * El límite de cálculo está impuesto por el tipo 'long' (F(92)).
 * * Editor: Roberto Méndez / Eder Yañez Díaz
 * Edición: 10/ Nov /25
 */
import java.util.Hashtable;

public class FibonacciThreadsMemoria implements Runnable{

    // 1. ESTRUCTURA DE MEMORIA: Hashtable para guardar los resultados (Memoización)
    // Clave: Posición (Long), Valor: Resultado F(n) (Long)
    private static final Hashtable<Long, Long> cache = new Hashtable<>();

    // Inicialización de la caché
    static {
        cache.put(0L, 0L); // F(0) = 0
        cache.put(1L, 1L); // F(1) = 1 (Ajuste para iniciar F(0)=0, F(1)=1)
    }

    long fi; // La posición que el thread va a calcular
    int num;

    public FibonacciThreadsMemoria(int n, long f){
        num = n;
        fi = f;
    }

    @Override
    public void run() {
        // En el main, el valor 'fi' que se pasa al constructor es la posición 'n', no F(n).
        System.out.println("Starte #" + num + " para calcular F(" + fi + ")"); 
        
        // El resultado es limitado al valor máximo que puede almacenar un 'long' (F(92))
        long res = fibonacci(fi); 
        
        System.out.println("Abschlussverfahren: " + num +
                             " - "+"fibonacci(" + fi + ") =" + res);
    }

    // 2. FUNCIÓN FIBONACCI CON MEMOIZACIÓN (O(n) - Recursivo Top-Down)
    long fibonacci(long f) {
        if (f < 0) {
            throw new IllegalArgumentException("La posición debe ser no negativa.");
        }

        // A) Verificar en el caché
        if (cache.containsKey(f)) {
            return cache.get(f);
        }
        
        // B) Si no está, calcular recursivamente
        long resultado = fibonacci(f - 1) + fibonacci(f - 2);

        // C) Guardar el resultado antes de devolverlo
        cache.put(f, resultado);

        return resultado;
    }

    public static void main(String[] args){
        Thread[] threads = new Thread[10];

        for (int i = 0; i < 10; i++) {
            // Se limita el valor a un máximo seguro para la demo, pero ahora puede ir hasta 92 sin lentitud
            long posicion = (long) (Math.random() * 100) + 1; 
            
            threads[i] = new Thread(new FibonacciThreadsMemoria(i, posicion));
        }

        for(int i = 0; i < 10; i++) threads[i].start();
    }
}