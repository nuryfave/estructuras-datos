import math  
def comb_sort(vector):
    permutación = True
    gap = len(vector)
    while (permutación == True) or  (gap>1):
        permutación = False
        gap = math.floor(gap / 1.3)
        if gap<1: gap = 1
        for actual in range(0, len(vector) - gap):
            if vector[actual] > vector[actual + gap]:
                permutación = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + gap] = \
                vector[actual + gap],vector[actual]
    return vector 
