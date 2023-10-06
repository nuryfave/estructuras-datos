typedef int bool;
enum { false, true };
 
void comb_sort(int* vector)
{
    int gap = 20;
    bool permutación = true;
    int actual;
   
    while (( permutación) || (gap>1)) {
        permutación = false;
        gap = gap / 1.3;
        if (gap<1) gap=1;
        for (actual=0;actual<20-gap;actual++) {
            if (vector[actual]>vector[actual+gap]){
                permutación = true;
                // Intercambiamos los dos elementos
                int temp = vector[actual];
                vector[actual] = vector[actual+gap];
                vector[actual+gap] = temp;
            }
        }
    }
}
