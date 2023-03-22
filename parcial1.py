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
    def __init__(self, lista, N):
        self.N = N
        self.k_b = float(1.38 * 10 **-23)
        if len(lista) == 3 and lista[2].lower() == 'pv':
            self.P = lista[0]
            self.V = lista[1]
            self.T = self.obtener_temperatura()
        
        elif len(lista) == 3 and lista[2].lower == 'pt':
            self.P = lista[0]
            self.T = lista[1]
            self.V = self.obtener_volumen()

        elif len(lista) == 3 and lista[2].lower == 'vt':
            self.V = lista[0]
            self.T = lista[1]
            self.P= self.obtener_presion()

    def obtener_temperatura(self):
        return (self.P * self.V)/ (self.N * self.k_b)
    
    def obtener_presion(self):
        return (self.N * self.k_b * self.T) / self.V
    
    def obtener_volumen(self):
        return (self.N * self.k_b * self.T) / self.P

a = input('Escriba un arreglo pv, pt, vt: ').lower()
b = float(input('valor de la primera variable de estado: '))
c = float(input('valor de la segunda variable de estado: '))

termodinamica = [ b, c, a]
print(termodinamica)

N = float(input('numero de particulas de la sustancia: '))

sistem = termo(termodinamica, N)

if  a== 'pv':
    temperatura = sistem.obtener_temperatura()
    print('la temperatura es:', temperatura)

if a == 'pt':
    volumen = sistem.obtener_volumen()
    print('El volumen es:', volumen)

if a == 'vt':
    presion = sistem.obtener_presion()
    print('La presión es:', presion)