# LIBRERIA PARA OPERACIONES DE VECTORES Y MATRICES
import math
def sumacplx(a,b):
    # Suma de numeros complejos
    real = a[0]+b[0]
    img = a[1]+b[1]
    return real,img

def restacplx(a,b):
    # Resta de numeros complejos
    real = a[0]-b[0]
    img = a[1]-b[1]
    return real,img

def multcplx(a,b):
    # Multiplicacion de numeros complejos
    real = (a[0]*b[0])-(a[1]*b[1])
    img = (a[0]*b[1])+(b[0]*a[1])
    return real,img

def conjcplx(c):
    # Conjugado de numeros Complejos
    real = c[0]
    img = c[1] * -1
    return real, img

def sumaVector(v):
    # Suma Vector
    valorDevolver = v.pop(0)
    while len(v)!=0:
        valorDevolver = suma(valorDevolver,v.pop(0))
    return valorDevolver

def producto_vectores(v,w):
    # Producto vectores
    if(len(v)!=len(w)):
        raise "Estos vectores no se pueden multiplicar"
    vectorResultante = []
    for i in range(len(v)):
        vectorResultante.append(multcplx(v[i],w[i]))
    return vectorResultante

def transpuestaVector(vector1):
    matrizDevolver = []
    for x in vector1:
        if(type(x) is list):
            matrizDevolver.append(x[0])
        else:
            matrizDevolver.append([x])
    return matrizDevolver

# LIBRERIA
def sumavec(v,w):
    # Adicion vectores complejos
    tamano = len(v)
    suma = [(0,0)for i in range(tamano)]
    i = 0
    while i < tamano:
        suma[i] = sumacplx(v[i],w[i])
        i += 1
    return suma
#
def inveradicion(v):
    # Inverso aditivo de un vector complejo
    return multscalar([-1,0], v)
    
#
def multscalar(c,v):
    # Multiplicación de un escalar por un vector complejo
    tamano = len(v)
    mult = [(0,0)for i in range(tamano)]
    i = 0
    while i < tamano:
        mult[i] = multcplx(c,v[i])
        i += 1
    return mult
#
def sumaMatrices(m1,m2):
    # Adición de matrices complejas.
    SumaMatriz = [[[0,0] for j in range(len(m1))] for i in range(len(m2))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            SumaMatriz[i][j][0] = m1[i][j][0] + m2[i][j][0]
            SumaMatriz[i][j][1] = m1[i][j][1] + m2[i][j][1]
    return SumaMatriz
#
def inversaMatriz(mCompleja):
    # Inversa de una matriz
    n,m = len(mCompleja),len(mCompleja[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = multcplx(mCompleja[i][j],(-1,0))
    return c

#
def multmatrizescalar(matriz,num):
    # Multiplicacion de un escalar por una matriz compleja
    n,m = len(matriz), len(matriz[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = multcplx(matriz[i][j], num)
    return c

#
def transmatriz(a):
    # Transpuesta de una matriz
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[j][i]
    return c

#
def conjumatriz(m1):
    # Conjugada de una matriz/vector
    filas = len(m1)
    columnas = len(m1[0])
    for i in range(filas):
        for j in range(columnas):
            m1[i][j] = conjcplx(m1[i][j])
    return m1

#
def adjuntamatriz(matriz2):
    # Adjunta (daga) de una matriz/vector
    return conjumatriz(transmatriz(matriz2))

#
def matriz_Producto(m1,m2):
    # Producto de dos matrices (de tamaños compatibles)
    matrizProducto = [[[0,0] for j in range(len(m1))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1[0])):
                matrizProducto[i][j][0] = matrizProducto[i][j][0] + (m1[i][k][0] * m2[k][j][0] - m1[i][k][1]*m2[k][j][1])
                matrizProducto[i][j][1] = matrizProducto[i][j][1] + (m1[i][k][1] * m2[k][j][0] + m1[i][k][0]*m2[k][j][1])
    return matrizProducto
#
def productoInterno(a,b):
    # Producto Interno de dos vectores
    vector = (0,0)
    m,n = len(a),len(b)
    for i in range(m):
        resp1 = conjcplx(a[i])
        respuesta2 = multcplx(resp1,b[i])
        respuesta = sumacplx(vector,respuesta2)
    return respuesta

#
def norma_vector(a):
    # Norma de un vector
    e = productoInterno(a,a)
    c = (e[0]) ** (1/2)
    c = round(c,2)
    return c
#
def matrizHermitania(m1):
    # Revisar si una matriz es Hermitiana
    filas = len(m1)
    columnas = len(m1[0])
    m2 = [[[0,0]]*filas for i in range(columnas)]
    for i in range(filas):
            for j in range(columnas):
                m2[i][j] = m1[i][j]
    return adjuntamatriz(m2) == m1
    
#
def productotensor(a,b):
    # Producto tensor de dos matrices/vectores
    arreglo = []
    posi = 0
    posj = 0
    while posi < (len(a)-1)*2:
        fila1 = a[posi]
        fila2 = b[posj]
        fila3 = []
        for i in fila1:
            for j in fila2:
                fila3 = fila3 + [multcplx(i,j)]
        posj = posj + 1
        fila2 = b[posj]
        arreglo.append(fila3)
        fila = []
        for i in fila1:
            for j in fila2:
                fila.append(multcplx(i,j))
        posi = posi + 1
        posj = posj - 1
        arreglo.append(fila)
    return arreglo

#
def main():
    """ Funcion Principal """
    a = (2,13)
    b = (34,56)
    c = (2,1)
    v = [(3,7),(8,9),(3.4,-7,8)]
    w = [(5,6),(6,8),(0,0)]
    m1 = [[(2,5),(1,0)],[(4,3),(0,0)]]
    m2 = [[(1,1),(7,2)],[(0,0),(1,-1)]]
    vector1 = [(3,7),(8,9)]
    vector2 = [(2,7),(4,6)]
    matriz1 = [(7,0),(4,2)], [(2,3),(2,3)]
    matriz2 = [(3,4),(2,2)], [(5,7),(1,9)]
    num = (3,0)
    print(sumavec(v,w))
    print(multscalar((2,1),w))
    print(inveradicion(v))
    print(sumaMatrices(m1,m2))
    print(inversaMatriz(matriz1))
    print(multmatrizescalar(matriz1,num))
    print(transmatriz(matriz2))
    print(conjumatriz(matriz2))
    print(adjuntamatriz(matriz2))
    print(matriz_Producto(m1,m2))
    print(productoInterno(vector1,vector2))
    print(norma_vector(vector1))
    print(matrizHermitania(m1))
    print(productotensor(matriz1,matriz2))
    
main()
