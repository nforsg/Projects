import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random as rnd

def randomwalk(coord1, coord2, potential, n, count_array):
    #init_coordinate = n // 2
    x = coord1
    y =  coord2 
    #count_array = np.zeros((n+1, n+1))
    #init_point = potential[mid, mid]
    #x_list = [x]
    #y_list = [y]
    #V_list = [0]
    #for i in range(n):
    while x > 0 and x < n and y > 0 and y < n:
        rand_float = rnd.random()
        step = int(4 * rand_float)
        if step == 0:
            x -= 1
        elif step == 1:
            x += 1
        elif step == 2:
            y -= 1
        elif step == 3:
            y += 1
        #print((x,y))
    count_array[x,y] += 1
    v_ij = potential[x,y]
    return v_ij

def potential(n, walks, coord1, coord2):

    v = np.zeros((n+1, n+1))
    for i in range(1,n):
        v[0,i] = 10
        v[n,i] = 10
        v[i,0] = 5
        v[i,n] = 5
    potential_list = []
    count_array = np.zeros((n+1, n+1))
    count_array[coord1, coord2] = 6
    for i in range(walks):
        #print(i)
        v_ij = randomwalk(coord1, coord2, v, n, count_array)
        potential_list.append(v_ij)
        #print(np.mean(potential_list))
    #print(count_array)
    V_final = np.mean(potential_list)
    return V_final, count_array


def heatmap(n, walks):
    #n = 10
    #walks = 500    
    coord1 = n - 7
    coord2 = n - 3
    v, count_array= potential(n, walks, coord1, coord2)
    #print(v)
    #print(count_array)
    plt.imshow(count_array)
    plt.title('G(' + str(coord2)+ ',' +str(coord1) + ',$x_b, y_b$)')
    plt.colorbar()
    plt.show()

def main():

    heatmap(10, 500)


        
#if __name__ == '_main_':
main()