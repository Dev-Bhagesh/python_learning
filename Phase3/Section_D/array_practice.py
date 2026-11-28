import numpy as np

num1 = np.arange(1,11)
num2 = np.zeros(5)
num3 = np.ones(4)
num2d = np.array([[[10,20,30],[40,50,60]],[[70,80,90],[0,0,0]]])

valiables = [num1,num2,num3,num2d]

for vars in valiables:
    print(f'The Variable value : {vars}')
    print(f'The Dimention of the variable : {vars.ndim}')
    print(f'The Shape of the variable : {vars.shape}')
    print(f'The Size of the variable : {vars.size}')
    print(f'The Datatype of the variable : {vars.dtype}')
    print('-'*30)
