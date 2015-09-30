__author__ = 'Aitor'
import os

def limpiar():
    sist = os.name
    c = str("nt")


    if sist == c:
        os.system('cls')
        #print("cls")
    else:
        os.system('clear')
        #print("clear")

def area(x,y):
    '''
    (number, number) -> number
    Devuelve el area de un rectangulo pasandole el alto y el ancho.
    >area(5,7)
    35
    '''

    area = x * y
    print(area)

def otradef (c):
    '''
    Texto de ayuda
    dato 1
    dato 2
    ejemplo 1
    ejemplo 2
    '''

    if c == 1 :
        limpiar()
        help(area)
    elif c == 2:
        limpiar()
        help(otradef)
    else:
        limpiar()
        print("no hay ayuda")

limpiar()


print("=" * 10)
print("=" * 10)
print("=" * 10)
print("=" * 10)
print("=" * 10)
print("Introduce comando:\n ")

o = int (input())
print (o)
c = o
otradef(c)

