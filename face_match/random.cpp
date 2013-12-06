#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main(int argc, const char *argv[])
{
    int num[10], seed, i;

    if (argc != 2) {
        cout << "Error" << endl;
    }

    seed = atoi(argv[1]);

    srand(seed);

    for (i = 0; i < 10; ++i) {
        num[i] = rand() % 1000000;
    }

    for (i = 0; i < 10; ++i) {
        cout << num[i] << endl;
    
    }



    return 0;
}
