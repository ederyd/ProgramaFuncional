/**
Tema: Clase Hashtable<k,v>

Curso: MCA1 2026-1

Objetivo: Ver uso de Hashtable para posteriormente simular
   el diccionario que utilizamos en el programa
   fibonacci-MemDic1.py

Acciones: Crear: la tabla hash (fiboSuc = Suceción de fibonacci)
          Obtener datos dada una llave: método get(key)
          Modificar datos: método replace(key, valor)
          Recorrer la tabla hash mediante: foreach

Referencias:
* https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Hashtable.html
* https://www.geeksforgeeks.org/java/hashtable-foreach-method-in-java-with-examples/

Software: Java 25
          IDE IntelliJ 2025.2.4

Editor: Roberto Méndez Méndez
Editor: Eder Yañez Díaz
Created 1 Nov 2025
Edited: 9 Nov 2025
**/
import java.util.Hashtable;

public class A3_MainMiFiboHash {

   
    public static void main(String[] args) {
        
        System.out.println(String.format("Uso de la clase Hashtable<k, v>"));
        System.out.println("----------------------------------------");

        // Crear la tabla hash y añadir datos iniciales (F(0), F(1), F(2))
        Hashtable<Integer, Integer> fiboSuc
            = new Hashtable<Integer, Integer>();
        fiboSuc.put(0, 0);
        fiboSuc.put(1, 1);
        fiboSuc.put(2, 1);
        
        System.out.println("Tabla Hash inicializada con F(0)=0, F(1)=1, F(2)=1.");
        System.out.println();
        
        // =================================================================
        // Forma 1 de recorrer la tabla hash (mediante keySet y foreach mejorado)
        // Obtener datos: se usa fiboSuc.get(key)
        System.out.println("--- Forma 1: Recorrido mediante keySet ---");
        for (int key : fiboSuc.keySet()) {
            int val = fiboSuc.get(key);
            System.out.printf("El valor de fibonacci en la posición %d es %d %n",
                                key, val);
        }
        System.out.println();

        // =================================================================
        // Forma 2 de recorrer la tabla hash (mediante forEach)
        System.out.println("--- Forma 2: Recorrido mediante forEach con lambda ---");
        fiboSuc.forEach((key, value) ->
            System.out.println("Key: " + key + ", Value: " + value));
        System.out.println();

        // =================================================================
        // Forma 3: Recorrer la tabla hash y alterar el valor del registro
        // Modificar datos: se usa fiboSuc.replace(key, valor)
        System.out.println("--- Forma 3: Recorrido y Modificación (Fibonacci + 100) ---");
        
        // Se crea una referencia final para poder usar la tabla dentro de la expresión lambda forEach
        final Hashtable<Integer, Integer> fiboSucFinal = fiboSuc; 
        
        fiboSuc.forEach((k, v) -> {
            // Se calcula el nuevo valor
            int nuevoValor = v + 100;
            
            // Reemplazar el valor asociado a la clave
            fiboSucFinal.replace(k, nuevoValor); 
            
            System.out.println("Key: " + k + ", Valor Original: " + v + ", Nuevo Valor: " + nuevoValor);
        });

        System.out.println();
        System.out.println("--- Resultado Final en la Tabla Hash ---");
        // Verifica que los valores se hayan modificado
        fiboSucFinal.forEach((k, v) ->
            System.out.println("Key: " + k + ", Value: " + v));
    }
}