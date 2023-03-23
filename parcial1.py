'''
PV= N K_b T = (n*N_a) k_b T, donde n es la cantidad de moles de sustancia.
'''
class termo:
    def __init__(self, matri, N):
        self.N = N
        self.k_b = float(1.38 * 10 **-23)

        if matri[0][2].lower() == 'pv':
            self.P = matri[0][0]
            self.V = matri[0][1]
            self.T = self.obtener_temperatura()
        
        elif matri[1][2].lower() == 'pt':
            self.P = matri[1][0]
            self.T = matri[1][1]
            self.V = self.obtener_volumen()

        elif matri[2][2].lower() == 'vt':
            self.V = matri[2][0]
            self.T = matri[2][1]
            self.P= self.obtener_presion()

    def obtener_temperatura(self):
        return (self.P * self.V/ (self.N * self.k_b))
    
    def obtener_presion(self):
        return ((self.N * self.k_b * self.T )/ self.V)
    
    def obtener_volumen(self):
        return ((self.N * self.k_b * self.T) / self.P)


class Matriz:
    def __init__(self, lista, n, m):
        self.a00=lista[0][0]
        self.a01=lista[0][1]
        self.a02=lista[0][2]
        self.a03=lista[0][3]
        self.a10=lista[1][0]
        self.a11=lista[1][1]
        self.a12=lista[1][2]
        self.a13=lista[1][3]
        self.a20=lista[2][0]
        self.a21=lista[2][1]
        self.a22=lista[2][2]
        self.a23=lista[2][3]
        self.n=n
        self.m=m 

    def __str__(self):
        return ("|{:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5}|".format(self.a00, self.a01, self.a02, self.a03, self.a10, self.a11, self.a12, self.a13, self.a20, self.a21, self.a22, self.a23))

    def iesima(self, i, j):
        if i == 0 and j==0:
            return ('la entrada corresponde la presion ', self.a00, ' la temperatura es ', self.a01, ' el volumen es ', self.a02)
        elif i == 0 and j == 1:
            return ('la entrada corresponde la temperatura ', self.a01, ' la presion es ', self.a00, ' el volumen es ', self.a02)
        elif i == 0 and j == 2:
            return('la entrada corresponde al volumen ', self.a02, ' la temperatura es ', self.a01, ' la presion es ', self.a00)
        elif i == 1 and j == 0:
            return('la entrada corresponde la presion ', self.a10, ' la temperatura es ', self.a11, ' el volumen es ', self.a12)
        elif i == 1 and j == 1:
            return('la entrada corresponde la temperatura ', self.a11, ' la presion es ', self.a10, ' el volumen es ', self.a12)
        elif i == 1 and j == 2:
            return('la entrada corresponde al volumen ', self.a12, ' la temperatura es ', self.a11, ' la presion es ', self.a10)
        elif i == 2 and j == 0:
            return('la entrada corresponde la presion ', self.a20, ' la temperatura es ', self.a21, ' el volumen es ', self.a22)
        elif i == 2 and j == 1:
            return('la entrada corresponde la temperatura ', self.a21, ' la presion es ', self.a20, ' el volumen es ', self.a22)
        elif i == 2 and j == 2:
            return('la entrada corresponde al volumen ', self.a12, ' la temperatura es ', self.a11, ' la presion es ', self.a10)

        else:
            return None

    def iso(self, n, m):
        if n == 1 and m == 0 or n==0 and m == 1:
            if self.a00 == self.a10:
                respuesta = 'hay un proceso isobarico'
                return respuesta
            
            elif self.a01 == self.a11:
                respuesta = 'hay un proceso isocorico'
            
            elif self.a02 == self.a12:
                respuesta = 'hay un proceso isocorico'
                return respuesta

            else:
                respuesta = 'no hay una transicion de estado con variables contantes.'
                return respuesta
        
        elif n == 0 and m == 2 or n == 2 and m == 0:
            if self.a00 == self.a20:
                respuesta = 'hay un proceso isobarico'
                return respuesta
            
            elif self.a01 == self.a21:
                respuesta = 'hay un proceso isocorico'
            
            elif self.a02 == self.a22:
                respuesta = 'hay un proceso isocorico'
                return respuesta

            else:
                respuesta = 'no hay una transicion de estado con variables contantes.'
                return respuesta

        elif n == 1 and m == 2 or n == 2 and m == 1:
            if self.a10 == self.a20:
                respuesta = 'hay un proceso isobarico'
                return respuesta
            
            elif self.a11 == self.a21:
                respuesta = 'hay un proceso isocorico'
            
            elif self.a12 == self.a22:
                respuesta = 'hay un proceso isocorico'
                return respuesta



            else:
                respuesta = 'no hay una transicion de estado con variables contantes.'
                return respuesta


N_a = 6*10**-23

print('ingrese las listas PV, PT, VT con sus datos correspondientes')
datos = input('que datos va a ingresar? PV, PT, VT: ')

if datos == 'pv':
    print('ingrese datos de configuracion Presión y volumen')
    a = 'PV'
    b = float(input('el valor de P es: '))
    c = float(input('el valor de V es: '))
    PV = [[b, c, a], [b, c, a], [b, c, a]]
    print(PV[0])  


    n=float(input('ingrese una cantidad de moles de sustancia: '))
    u = n*N_a
    p_v = termo(PV, u)
    t = p_v.obtener_temperatura()
    print('la temperatura es: ', t)


    datos_1 = input('que datos va a ingresar? PT, VT: ')
    if datos_1 == 'pt':
        print('ingrese los datos de PT')
        d ="PT"
        e = float(input('el valor de P es: '))
        f = float(input('el valor de T es: '))
        PT = [[e, f, d], [e, f, d], [e, f, d]]
        print(PT[1])

        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_t = termo(PT, u)
        v = p_t.obtener_volumen()
        print('el volumen es: ', v, 'Para N = 6*10**-23')


        print('ingrese los datos de VT')
        g ="VT" 
        h =float(input('el valor de V es: '))
        i =float(input('el valor de T es: '))
        VT = [[h, i, g], [h, i, g], [h, i, g]]
        print(VT[2])

        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        v_t = termo(VT, u)
        p = v_t.obtener_presion()
        print('la presion es: ', p)

        sistemas = [[b, c, t, "PVT"], [e, f, v, 'PTV'], [h, i, p, 'VTP']]
        sist = Matriz(lista = sistemas, n=3, m=4)
        
        sistemas = [[b, c, t, "PVT"], [e, v, f, 'PVT'], [p, h, i, 'PVT']]
        sist = Matriz(lista=sistemas, n=3, m=4)
        print(sist)   

        print('las filas corresponden a diferentes sistemas o estados, que estados desea comparar?')

        a=int(input('primer estado: '))
        b=int(input('segundo estado: '))
        peguelo = sist.iso(n=a, m=b)

        print(peguelo)


    elif datos_1 == 'vt':
        print('ingrese los datos de VT')
        g ="VT" 
        h =float(input('el valor de V es: '))
        i =float(input('el valor de T es: '))
        VT = [[h, i, g], [h, i, g], [h, i, g]]
        print(VT[2])


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a

        v_t = termo(VT, u)
        p = v_t.obtener_presion()
        print('la presion es: ', p)



        print('ingrese los datos de PT')
        d ="PT"
        e = float(input('el valor de P es: '))
        f = float(input('el valor de T es: '))
        PT = [[e, f, d], [e, f, d], [e, f, d]]
        print(PT[1])


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_t = termo(PT, u)
        v = p_t.obtener_volumen()
        print('el volumen es: ', v)

        sistemas = [[b, c, t, "PVT"], [e, f, v, 'PTV'], [h, i, p, 'VTP']]
        sist = Matriz(lista = sistemas,  n=3, m=4)
        
        sistemas = [[b, c, t, "PVT"], [e, v, f, 'PVT'], [p, h, i, 'PVT']]
        sist = Matriz(lista = sistemas, n=3, m=4)
        print(sist)

        print('las filas corresponden a diferentes sistemas o estados, que estados desea comparar?')

        a=int(input('primer estado: '))
        b=int(input('segundo estado: '))
        peguelo = sist.iso(n=a,m=b)

        print(peguelo)

    else:
        print('error, su respuesta no concuerda')


elif datos == 'pt':
    d ="PT"
    e = float(input('el valor de P es: '))
    f = float(input('el valor de T es: '))
    PT = [[e, f, d], [e, f, d], [e, f, d]]
    print(PT[1])


    n=float(input('ingrese una cantidad de moles de sustancia: '))
    u = n*N_a
    p_t = termo(PT, u)
    v = p_t.obtener_volumen()
    print('el volumen es: ', v)

    datos_2 = input('que datos va a ingresar? PV, VT: ')
    if datos_2 == 'pv': 
        print('ingrese los datos de PV')
        a = 'PV'
        b = float(input('el valor de P es: '))
        c = float(input('el valor de V es: '))
        PV = [[b, c, a], [b, c, a], [b, c, a]]
        print(PV[0])  


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_v = termo(PV, u)
        t = p_v.obtener_temperatura()
        print('la temperatura es: ', t)



        print('ingrese los datos de VT')
        g ="VT" 
        h =float(input('el valor de V es: '))
        i =float(input('el valor de T es: '))
        VT = [[h, i, g], [h, i, g], [h, i, g]]
        print(VT[2])


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        v_t = termo(VT, u)
        p = v_t.obtener_presion()
        print('la presion es: ', p)


        sistemas = [[b, c, t, "PVT"], [e, f, v, 'PTV'], [h, i, p, 'VTP']]
        sist = Matriz(lista = sistemas, n=3, m=4)
        
        sistemas = [[b, c, t, "PVT"], [e, v, f, 'PVT'], [p, h, i, 'PVT']]
        sist = Matriz(lista=sistemas, n=3, m=4)
        print(sist)

        print('las filas corresponden a diferentes sistemas o estados, que estados desea comparar?')

        a=int(input('primer estado: '))
        b=int(input('segundo estado: '))
        peguelo = sist.iso(n=a,m=b)

        print(peguelo)


    elif datos_2 == 'vt':
        print('ingrese los datos de VT')
        g ="VT" 
        h =float(input('el valor de V es: '))
        i =float(input('el valor de T es: '))
        VT = [[h, i, g], [h, i, g], [h, i, g]]
        print(VT[2])


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        v_t = termo(VT, u)
        p = v_t.obtener_presion()
        print('la presion es: ', p)



        print('ingrese los datos de PV')
        a = 'PV'
        b = float(input('el valor de P es: '))
        c = float(input('el valor de V es: '))
        PV = [[b, c, a], [b, c, a], [b, c, a]]
        print(PV[0])  



        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_v = termo(PV, u)
        t = p_v.obtener_temperatura()
        print('la temperatura es: ', t)

        sistemas = [[b, c, t, "PVT"], [e, f, v, 'PTV'], [h, i, p, 'VTP']]
        sist = Matriz(lista = sistemas, n=3, m=4)
        
        sistemas = [[b, c, t, "PVT"], [e, v, f, 'PVT'], [p, h, i, 'PVT']]
        sist = Matriz(lista=sistemas, n=3, m=4)
        print(sist)

        print('las filas corresponden a diferentes sistemas o estados, que estados desea comparar?')

        a=int(input('primer estado: '))
        b=int(input('segundo estado: '))
        peguelo = sist.iso(n=a,m=b)

        print(peguelo)
    else:
        print('error, su respuesta no concuerda')


elif datos == 'vt':
    print('ingrese los datos de VT')
    g ="VT" 
    h =float(input('el valor de V es: '))
    i =float(input('el valor de T es: '))
    VT = [[h, i, g], [h, i, g], [h, i, g]]
    print(VT[2])


    n=float(input('ingrese una cantidad de moles de sustancia: '))
    u = n*N_a
    v_t = termo(VT, u)
    p = v_t.obtener_presion()
    print('la presion es: ', p)

    datos_3 = input('que datos va a ingresar? PV, PT: ')
    if datos_3 == 'pv':
        print('ingrese los datos de PV')
        a = 'PV'
        b = float(input('el valor de P es: '))
        c = float(input('el valor de V es: '))
        PV = [[b, c, a], [b, c, a], [b, c, a]]
        print(PV[0])  


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_v = termo(PV, u)
        t = p_v.obtener_temperatura()
        print('la temperatura es: ', t)



        print('ingrese los datos de PT')
        d ="PT"
        e = float(input('el valor de P es: '))
        f = float(input('el valor de T es: '))
        PT = [[e, f, d], [e, f, d], [e, f, d]]
        print(PT[1])


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_t = termo(PT, u)
        v = p_t.obtener_volumen()
        print('el volumen es: ', v)


        sistemas = [[b, c, t, "PVT"], [e, f, v, 'PTV'], [h, i, p, 'VTP']]
        sist = Matriz(lista = sistemas, n=3, m=4)
        
        sistemas = [[b, c, t, "PVT"], [e, v, f, 'PVT'], [p, h, i, 'PVT']]
        sist = Matriz(lista=sistemas, n=3, m=4)
        print(sist)
        
        print('las filas corresponden a diferentes sistemas o estados, que estados desea comparar?')

        a=int(input('primer estado: '))
        b=int(input('segundo estado: '))
        peguelo = sist.iso(n=a,m=b)

        print(peguelo)



    elif datos_3 == 'pt':
        print('ingrese los datos de PT')
        d ="PT"
        e = float(input('el valor de P es: '))
        f = float(input('el valor de T es: '))
        PT = [[e, f, d], [e, f, d], [e, f, d]]
        print(PT[1])


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_t = termo(PT, u)
        v = p_t.obtener_volumen()
        print('el volumen es: ', v)



        print('ingrese los datos de PV')
        a = 'PV'
        b = float(input('el valor de P es: '))
        c = float(input('el valor de V es: '))
        PV = [[b, c, a], [b, c, a], [b, c, a]]
        print(PV[0])  


        n=float(input('ingrese una cantidad de moles de sustancia: '))
        u = n*N_a
        p_v = termo(PV, u)
        t = p_v.obtener_temperatura()
        print('la temperatura es: ', t)

        sistemas = [[b, c, t, "PVT"], [e, f, v, 'PTV'], [h, i, p, 'VTP']]
        sist = Matriz(lista = sistemas, n=3, m=4)
        
        
        sistemas = [[b, c, t, "PVT"], [e, v, f, 'PVT'], [p, h, i, 'PVT']]
        sist = Matriz(lista=sistemas, n=3, m=4)
        print(sist)
        
        print('las filas corresponden a diferentes sistemas o estados, que estados desea comparar?')

        a=int(input('primer estado: '))
        b=int(input('segundo estado: '))
        peguelo = sist.iso(n=a,m=b)

        print(peguelo)

    else:
        print('error, su respuesta no concuerda')


else:
    print('no corresponde con ningun par de variables de estado de la ecuacion de gas ideal. >:c')


print('que elementos de la matriz quieres que imprima? \n el estado y variable van de 0 a 2 ')

s = float(input('estado: '))
d = float(input('variable: '))

enesima = sist.iesima(i=s,j=d)

print(enesima)


