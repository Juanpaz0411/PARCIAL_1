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

primero para tener nocion de lo que se iba a hacer se uso:


class termo:
    def __init__(self, P, V, T, N):
        self.N = N
        self.V = V
        self.P = P
        self.T = T
        self.k_b = float(1.38 * 10 **-23)

    def obtener_temperatura(self):
        return (self.P * self.V)/ (self.N * self.k_b)
    
    def obtener_presion(self):
        return (self.N * self.k_b * self.T) / self.V
    
    def obtener_volumen(self):
        return (self.N * self.k_b * self.T) / self.P
    
print('en caso de no tener una variable escribin <0>, minimo ingresar dos variables.')
a = float(input('Presion: ' ))
b = float(input('Volumen: '))
c = float(input('Temperatura: '))
d = float (input('numero de moles de sustancia: '))

arreglo_termod = termo(a, b, c, d)

if a==0:
    print('la presion a partir de la ecuacion de gas ideal es:', arreglo_termod.obtener_presion())
elif b==0:
    print('el volumen a partir de la ecuacion de gas ideal es:', arreglo_termod.obtener_volumen())
elif c==0:
    print('la temperatura1 a partir de la ecuacion de gas ideal es:', arreglo_termod.obtener_temperatura())

posteriormente se pretende crear una clase que use el numero de particulas y una lista con parametros *pv*, *pt* o *vt*