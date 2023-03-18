# PARCIAL 1 DE PROGRAMACIÓN😒

Estudiante G: En termodinámica las variables de presión (P), temperatura (T), volumen (V), número de particulas (N) y constante de Boltzman (ks) se relacionan (para gas ideal) por: PV=NkT. Dependiendo de como cambien estas variables
se dice que se tiene un proceso termodinámico particular. Los más importantes son el adiabático, isobarico, isocórico e isotermo. Dependiendo de como sea este cambio se va a tener un calor y una energia asociados al proceso. 
   
## Cree una clase que:

    1. Al definiria reciba dos argumentos, el primero el número de particulas (Por ejemplo "1 x 10e24") y el segundo argumento una lista 
    de cuatro filas y tres columnas en donde en las dos primeras columnas se encuentra el valor numérico que de las variables termodinámicas 
    que se especifica en la tercera.
     Ejemplo:
        [[1,2,"PV"],[3,4,"PT],[7,8,"TV"],[5,6,"PT"]] Lo cual indicaría que en un primer momento P=1 y V=2 luego P=3 y V=4, luego T=7 
        y V=8, luego P=5 y T=6.
		El programa debe calcular la variable que falta y calcularla. Esto para guardar en un atributo los valores de  presión, temperatura
        y volumen en cada caso (Lista de cuatro columnas por tres filas donde todas las entradas ya son números).


    2. Método __getitem__ implementado para que al preguntar por el i-ésimo elemento diga  los valores de la i-ésima presión, temperatura
    y volumen. Es decir, si en el caso anterior se le pide el elemento (3) el programa debe retornar una cadena en donde diga que la presión es 5,
    la temperatura 6 y el volumen el valor calculado.


    3. Método que reciba dos números enteros ny m entre 0 y 3 y diga si de nam se tiene un proceso isobárico (La presión no cambia), isocoro (El volumen no cambia), 
    isotermo (La temperatura no cambia), adiabático (la cantidad {k_b N ln(V_m/V_n)  +  3 k_b N ln(T_m/T_n)  =  0  }), o ninguno de los anteriores.