

------------

<h1 align="center"> PARCIAL 1 DE PROGRAMACIÓN😒</h1>

------------
##### Hecho por: *Juan jose paz hormiga*

Estudiante G: En termodinámica las variables de presión (P), temperatura (T), volumen (V),
número de particulas (N) y constante de Boltzman (ks) se relacionan (para gas ideal) por:
PV=NkT. Dependiendo de como cambien estas variables
se dice que se tiene un proceso termodinámico particular. Los más importantes son el
adiabático, isobarico, isocórico e isotermo. Dependiendo de como sea este cambio se va
a tener un calor y una energia asociados al proceso. 

#### Cree una clase que:

1. Al definiria reciba dos argumentos, el primero el número de particulas (Por ejemplo "1
x 10e24") y el segundo argumento una lista de cuatro filas y tres columnas en donde en
las dos primeras columnas se encuentra el valor numérico que de las variables
termodinámicas que se especifica en la tercera.
     Ejemplo:
      [[1,2,"PV"],[3,4,"PT],[7,8,"TV"],[5,6,"PT"]] Lo cual indicaría que en un primer momento P=1 y V=2 luego P=3 y V=4, luego T=7 
      y V=8, luego P=5 y T=6.
	El programa debe calcular la variable que falta y calcularla. Esto para guardar en un atributo los valores de  presión, temperatura
      y volumen en cada caso (Lista de cuatro columnas por tres filas donde todas las entradas ya son números).

2. Método __getitem__ implementado para que al preguntar por el i-ésimo elemento
diga  los valores de la i-ésima presión, temperatura y volumen. Es decir, si en el caso
anterior se le pide el elemento (3) el programa debe retornar una cadena en donde diga
que la presión es 5,  la temperatura 6 y el volumen el valor calculado.

3. Método que reciba dos números enteros ny m entre 0 y 3 y diga si de nam se tiene un
proceso isobárico (La presión no cambia), isocoro (El volumen no cambia), isotermo (La
temperatura no cambia), adiabático (la cantidad {k_b N ln(V_m/V_n)  +  3 k_b N
ln(T_m/T_n)  =  0  }), o ninguno de los anteriores.

------------


primero para tener nocion de lo que se iba a hacer se uso:

	class termo:
    	def __init__(self, P, V, T, N):

Esto para hacer de forma gradual un programa mas tecnico y apto para el calculo de la variable
de estado faltante.

posteriormente se pretende crear una clase que use el numero de particulas y una lista con parametros *pv*, *pt* o *vt*.

Posteriormente se redefinen los parametros que definen la clase de forma que ahora todo queda en un lista de forma tal que esta lista tiene a (P, V, T)

	class termo:
    	def __init__(self, lista, N):

con esto fue posible realizar condiciones cada que el usuario usara un arreglo (pv,pt, vt).

Luego de usar las lista se uso 'matri' en lugar de lista en el constructor de la clase termodinamica, con el fin de formar una matriz que recibiera los datos de P, V, T correspondientes, esto con el fin de efectuar las operaciones:

	class termo:
    	def __init__(self, matri, N):

Al crear objetos de la clase termi se enuncia por defecto que:   N = 6*10^-23. Se crearon 
estos objetos con el fin de acceder a ellos mediante los métodos:
calculo de temperatura, calculo de presion y calculo de volumen.

    def obtener_temperatura(self):
        return (self.P * self.V)/ (self.N * self.k_b)
    
    def obtener_presion(self):
        return (self.N * self.k_b * self.T) / (self.V)
    
    def obtener_volumen(self):
        return (self.N * self.k_b * self.T) / (self.P)

y calcular los valores respectivos, ejemplo:

	v_t = termo(VT,  N = 6*10**-23)
   	p = v_t.obtener_presion()
	print('la presion es: ', p)

- calculo de temperatura
- calculo de presion
- calculo de volumen

El resultado esperado es una matriz de 3x4, de esta forma se realizo una clase para esta
matriz descrita en termino de sus elementos a00, a01,...

	class Matriz:
		def __init__(self, lista, n, m):

en esta se agrego la funcion __getitem__ para aceder a un objeto específico 
 de la matriz (elemento [i][j]), tambien se agrego una funcion  __iso__ que permite
 saber para dos filas, que variables se mantienen constantes o no.
 
 Se uso el metodo iso para verificar si hay una variable constante en la transicion de 
 estado(y /0 sistema).
 
     def iso(self):
        if self.a00 == self.a10 or self.a10 == self.a20 or self.a00 == self.a20:
            respuesta = 'hay un proceso isobarico'
            return respuesta
        
        elif self.a01 == self.a11 or self.a11 == self.a21 or self.a01 == self.a21:
            respuesta = 'hay un proceso isocorico'
        
        elif self.a02 == self.a12 or self.a12 == self.a22 or self.a02 == self.a22:
            respuesta = 'hay un proceso isocorico'
            return respuesta

        else:
            respuesta = 'no hay una transicion de estado con variables contantes.'
            return respuesta

este es usado de la siguiente forma:

        sistemas = [[b, c, t, "PVT"], [e, v, f, 'PVT'], [p, h, i, 'PVT']]
        sist = Matriz(lista=sistemas)
        print(sist)

        peguelo = sist.iso()

        print(peguelo)

Antes de usar un método __iso__ se uso:

        desicion = float(input('hay 3 sistemas distintos, sobra cual sistema desea indagar? '))

        if desicion == 1:
            print('la presion del sistema es ', sist[0,0], 'su volumen es ', sist[0,1], 'su temperatura es ', sist[0,2] )

        elif desicion == 2:
            print('la presion del sistema es ', sist[1,0], 'su volumen es ', sist[1,1], 'su temperatura es ', sist[1,2] )

        elif desicion == 3:
            print('la presion del sistema es ', sist[2,0], 'su volumen es ', sist[2,1], 'su temperatura es ', sist[2,2] )

        print('que elementos quiere comparar? escriba el sistema(corresponde a fila de la matriz) y la variable(columna).') 
        n = int(input('sistema(0, 1, 2): '))
        m = int(input('presion(0), volumen(1), temperatura(2): '))
        
        print('con que sistema desea comparar a la variable ', m, ' ? ')

        n1 = int(input('sistema: '))

        if sist[n, m] == sist[n1, m]:
            if m == 2:
                print('significa que al pasar del estado', n, 'al estado', n1,' la temperatura se mantuvo constante, esto es un proceso isotermico')
            
            elif m == 1:
                print('significa que al pasar del estado', n, 'al estado', n1,' el volumen se mantuvo constante, esto es un proceso isocorico')

            elif m == 0:
                print('significa que al pasar del estado', n, 'al estado', n1,' la presion se mantuvo constante, esto es un proceso isobarico')
        
        elif sist[n, m] != sist[n1, m]:
            print('del estado ', n, ' al estado ', n1, ' no hubo un proceso en el cual alguna variable de estado termodinamica se mantuviera constante.')

esta parte del codigo no es un método, sin embargo permite saber que pasa si dos
determinados elementos de la matriz son iguales que proceso iso hay (isocorico,
isobarico, isotermico).

para acceder a una fila especifico de la matriz no se uno un getitem, se uso un
metodo __iesima__ para que se imprima una fila de la columna con su respectiva cadena
que especifica que significa cada elemento:


	def iesima(self, i, j):
			if i == 0 and j==0:
				return ('la entrada corresponde la presion ', self.a00, ' la temperatura es ', self.a01, ' el volumen es ', self.a02)
	...

Los problemas  con este codigo se presentaron debido a que  hay tres configuraciones 
*PV, PT, VT*, al escoges que se va a ingresar un aconfiguracion, quedan dos
configuraciones mas que se escoja primero una de las dos restantes o que se escoja
primero la otra, lo que indica que hay muchas posibilidades a la hora de escojer el orden
 en el que se van a ingresar los datos la matriz, lo que se puede solucionar de forma
 manual alargando el codigo o usando ciclos, sin embargo por cuestiones de tiempo no
 se realizo de esta segunda forma.



