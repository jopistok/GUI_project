import numpy as np
from numpy import linalg as LA
from math import *
from time import sleep

def ortogonalization(f1, f2, f3, f4):
    g1 = f1
    e1 = g1/LA.norm(g1)
    g2 = f2 - np.dot(f2, e1)*e1
    e2 = g2/LA.norm(g2)
    g3 = f3 - np.dot(f3, e1)*e1 - np.dot(f3, e2)*e2
    e3 = g3/LA.norm(g3)
    g4 = f4 - np.dot(f4, e1)*e1 - np.dot(f4, e2)*e2 - np.dot(f4, e3)*e3
    e4 = g4/LA.norm(g4)
    return np.array([e1, e2, e3, e4], float)

def transition(a_basis, b_basis):
    a_basis = np.transpose(a_basis)
    #print(a_basis)
    b_basis = np.transpose(b_basis)
    #print(b_basis)
    return np.matmul(LA.inv(b_basis), a_basis)

def transit_from_A_to_B(b_to_a_transition, vec):
    return np.matmul(b_to_a_transition, np.transpose(vec))
        
def main_2(p, q, a1, a2, a3, a4):
    #print("Введите вектор p покоординатно")
    a_p = np.array(p, float)
    #print("Введите вектор q покоординатно")
    a_q = np.array(q, float)
    #print("Введите вектор a1 покоординатно")
    a1 = np.array(a1, float)
    #print("Введите вектор a2 покоординатно")
    a2 = np.array(a2, float)
    #print("Введите вектор a3 покоординатно")
    a3 = np.array(a3, float)
    #print("Введите вектор a4 покоординатно")
    a4 = np.array(a4, float)
    a_basis = np.array([a1, a2, a3, a4])
    b_basis = ortogonalization(a1, a2, a3, a4)
    print("Массив базисных векторов b_j(каждый массив -- это базисный вектор)")
    print(b_basis)
    print()
    b_to_a_transition = transition(a_basis, b_basis)
    np.set_printoptions(precision=8, suppress = True)
    print("Матрица перехода от {b_j} к {a_i}")
    print(b_to_a_transition)
    print()
    b_p = transit_from_A_to_B(b_to_a_transition, a_p)
    print("Вектор p в базисе {b_j}")
    print(b_p)
    print()
    b_q = transit_from_A_to_B(b_to_a_transition, a_q)
    print("Вектор q в базисе {b_j}")
    print(b_q)
    print()
    print("Скалярное произведение p на q")
    print(round(np.dot(b_q, b_p)))
    print()
    print("Угол между векторами p и q в градусах")
    print(acos((np.dot(b_q, b_p))/(LA.norm(b_q)*LA.norm(b_p)))*180/pi)

    #match str(input("Введите r чтобы начать заново\nВведите любую клавишу для выхода\n")):
    #    case "r": main_2()
    #    case _: return

def solve(inputData):

    answer = list()
    
    a_p = np.array(inputData[0:4:], float)
    #print(a_p)
    a_q = np.array(inputData[4:8:], float)
    #print(a_q)
    a1 = np.array(inputData[8:12:], float)
    #print(a1)
    a2 = np.array(inputData[12:16:], float)
    #print(a2)
    a3 = np.array(inputData[16:20:], float)
    #print(a3)
    a4 = np.array(inputData[20:24:], float)
    #print(a4)
    a_basis = np.array([a1, a2, a3, a4])
    b_basis = ortogonalization(a1, a2, a3, a4)

    answer.append(b_basis)

    b_to_a_transition = transition(a_basis, b_basis)

    answer.append(b_to_a_transition)

    b_p = transit_from_A_to_B(b_to_a_transition, a_p)

    b_q = transit_from_A_to_B(b_to_a_transition, a_q)

    answer.append([b_p, b_q])

    answer.append(round(np.dot(b_q, b_p)))
    answer.append(acos((np.dot(b_q, b_p))/(LA.norm(b_q)*LA.norm(b_p)))*180/pi)


    return answer
    
    

if __name__ == "__main__":
    input_data = '''5
-4
-1
-2
4
-2
0
2
4
1
2
2
6
-1
3
-2
5
3
5
-4
-2
-2
4
1

7
1
2
-2
4
2
2
1
2
-2
1
-4
2
3
1
6
-7
5
-1
0
-3
2
6
-1

-1
1
-1
1
-5
1
1
0
1
2
-1
0
3
4
-1
2
3
7
-1
5
1
6
1
2

2
0
1
1
-1
2
2
0
1
0
1
2
3
2
1
4
-4
-1
0
-1
-1
-4
3
-4

-8
-4
2
0
-18
-8
3
1
3
-1
-1
1
-5
5
3
-1
7
7
5
3
1
1
-1
-3

0
-1
1
2
0
1
-2
0
1
3
1
1
5
5
1
3
9
1
-5
5
1
1
-1
-3

1
3
-3
0
5
-2
2
0
2
3
2
1
3
1
5
-1
4
3
-2
5
-2
-1
2
3

1
1
1
2
3
3
3
1
1
-2
3
-2
1
5
-1
3
-4
-3
2
-5
-4
-4
0
2

-3
1
2
-1
0
1
-2
2
1
1
1
1
3
-1
3
-1
1
-1
3
1
1
-1
-1
1

6
2
-1
3
1
1
-1
-4
1
-1
1
-1
-1
3
-1
3
5
1
3
3
-1
-1
1
1

1
-1
1
1
3
1
-2
2
2
2
1
0
4
8
3
-1
-1
4
3
1
3
1
1
5

1
2
-1
5
1
-1
0
0
2
-2
0
1
4
0
1
1
3
10
1
-4
0
1
-2
2

7
-1
-2
1
5
-1
-1
0
3
5
1
1
11
7
3
1
15
11
1
7
-1
-1
5
3

7
-2
-1
3
10
-5
-2
1
5
-3
1
-1
13
-1
3
-1
-7
-11
3
1
1
-1
-3
5

1
2
-3
1
3
-1
0
1
1
4
4
4
5
3
0
8
9
-1
4
7
4
4
-1
-4

2
1
1
4
0
2
1
4
4
-1
-4
4
-3
5
8
0
1
9
7
-4
4
-4
4
-1

1
2
-1
-2
3
4
-5
0
5
4
2
2
-3
-6
-7
2
1
-11
-5
0
-2
-2
4
5

2
2
-4
1
1
-2
2
8
2
-2
-5
4
7
2
-3
6
5
0
1
11
4
-5
2
-2

1
7
-7
1
1
-2
1
7
8
4
1
0
8
3
5
8
7
3
13
4
-4
8
0
1

1
2
-3
5
7
-1
5
3
0
-1
4
8
8
5
-3
-8
4
13
-3
-7
1
0
-8
4

4
1
-1
2
-3
1
2
-1
7
4
4
0
7
8
0
7
11
8
-7
3
4
-7
0
4

6
3
3
1
7
1
-1
3
0
4
-4
7
7
0
8
-7
3
7
8
-11
4
0
-7
-4

1
1
-1
1
0
2
1
-1
5
6
4
2
9
4
-1
8
15
-1
1
4
-2
-4
6
5

0
-2
1
2
4
-3
1
-2
4
-2
-5
6
9
4
-1
8
19
-3
-4
10
2
4
-6
-5

0
1
-2
3
0
2
-2
1
7
7
1
1
15
13
9
-5
7
21
3
1
-1
-1
7
7

3
1
-2
0
1
-1
2
0
1
-1
7
-7
5
9
-13
15
9
7
1
-13
7
-7
-1
1

1
6
-6
0
-3
1
2
1
5
5
7
1
3
9
19
7
-1
-3
17
1
5
-5
-1
7

1
1
-1
1
1
2
-1
0
7
1
-5
-5
-9
3
17
11
3
-1
11
13
1
-7
5
-5

-1
2
-1
1
3
1
-1
1
-3
0
4
0
7
0
-1
0
-7
5
1
0
1
-5
7
5

1
0
3
3
0
1
2
2
4
0
3
0
1
0
7
0
-1
5
-7
0
1
5
7
5'''.split('\n\n')
    for i in range(len(input_data)):
        input_data[i] = list(map(int, input_data[i].split('\n')))
    print(input_data[0])
    for i in range(len(input_data)):
        input_data[i] = [input_data[i][0:4], input_data[i][4:8], input_data[i][8:12], input_data[i][12:16], input_data[i][16:20], input_data[i][20:24]]
    for i in range(len(input_data)):
        print("Вариант " + str(i + 1) + '\n')
        print("p = " + str(input_data[i][0]))
        print("q = " + str(input_data[i][1]))
        print("a1 = " + str(input_data[i][2]))
        print("a2 = " + str(input_data[i][3]))
        print("a3 = " + str(input_data[i][4]))
        print("a4 = " + str(input_data[i][5]) + '\n')
        main_2(input_data[i][0], input_data[i][1], input_data[i][2], input_data[i][3], input_data[i][4], input_data[i][5])
        print('-------------------------------------')
    #main_2()
    
