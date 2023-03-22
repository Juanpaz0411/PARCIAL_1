''' 
p*v = N*K_B*T =  n*R*T donde n es las moles de sustancia

1. cree una clase que al definiria reciba dos argumentos, el primero el número de particulas (Por ejemplo "1 x 10e24")
    y el segundo argumento una lista de cuatro filas y tres columnas en donde en las dos primeras columnas se 
    encuentra el valor numérico que de las variables termodinámicas que se especifica en la tercera.
     Ejemplo:
        [[1,2,"PV"],[3,4,"PT],[7,8,"TV"],[5,6,"PT"]] Lo cual indicaría que en un primer momento P=1 y V=2 luego P=3 
        y V=4, luego T=7 y V=8, luego P=5 y T=6.
		El programa debe calcular la variable que falta y calcularla. Esto para guardar en un atributo los valores 
        de  presión, temperatura y volumen en cada caso (Lista de cuatro columnas por tres filas donde todas las
        entradas ya son números).

'''

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

'como fue'