import numpy as np
from math import *
from time import sleep

i = np.array([1, 0, 0], float)
j = np.array([0, 1, 0], float)
k = np.array([0, 0, 1], float)

basis = np.array([i, j, k], float)

def pivot(vec, basis, angle):
    match vec:
        case "i":
            matrice = np.array([[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]], float)
            return np.matmul(basis, matrice)
        case "j":
            matrice = np.array([[cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]], float)
            return np.matmul(basis, matrice)
        case "k":
            matrice = np.array([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]], float)
            return np.matmul(basis, matrice)
        case _:
            return 0
        
def main_1(e1, angle1, e2, angle2):
    #e1 = str(input("Введите e1\n"))
    #angle1 = float(input("Введите угол для e1\n"))*pi/180
    #e2 = str(input("Введите e2\n"))
    #angle2 = float(input("Введите угол для e2\n"))*pi/180

    print("Матрица поворота для e1\n")
    print(pivot(e1, basis, angle1))
    print("Матрица поворота для e2\n")
    print(pivot(e2, basis, angle2))
    print("Итоговая матрица\n")
    print(np.matmul(pivot(e1, basis, angle1), pivot(e2, basis, angle2)))
    
    #match str(input("Введите r чтобы начать заново\nВведите любую клавишу для выхода\n")):
    #    case "r": main_1()
    #    case _: return

def solve(e1, angle1, e2, angle2):
    return [pivot(e1, basis, angle1*pi/180), pivot(e2, basis, angle2*pi/180), np.matmul(pivot(e1, basis, angle1*pi/180), pivot(e2, basis, angle2*pi/180))]
                


if __name__ == "__main__":
    input_data = '''i
45
k
135
j
135
i
30
i
30
j
135
j
150
i
60
i
60
j
150
j
-45
i
150
i
150
j
-45
i
-45
k
60
k
60
i
-45
j
60
k
150
k
150
j
60
i
30
j
45
j
30
k
45
k
30
i
45
i
45
j
60
i
-45
j
-60
k
-15
i
30
k
-45
i
75
j
30
k
150
i
120
k
150
i
-60
k
15
k
30
i
120
j
120
k
45
k
-135
j
60
j
60
i
150
i
135
k
240
j
30
k
-120
k
-135
j
30
i
60
j
-120
k
-150
i
45
j
120
k
-150
i
-45
j
-120'''.split('\n')
    print(len(input_data))
    for i in range(0, len(input_data), 4):
        print("Вариант " + str(i/4 + 1))
        print(input_data[i:i+4:])
        vxod = input_data[i:i+4:]
        main_1(vxod[0],int(vxod[1])*pi/180,vxod[2],int(vxod[3])*pi/180)
        print('------------------------------------------------------------')
    #main_1()
    
