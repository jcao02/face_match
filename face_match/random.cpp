#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

inline bool isInteger(const std::string & s)
{
    if(s.empty() || ((!isdigit(s[0])) && (s[0] != '-') && (s[0] != '+'))) return false ;

    char * p ;
    strtol(s.c_str(), &p, 10) ;

    return (*p == 0) ;
}

int main(int argc, const char *argv[])
{
    int num[10], seed, i;

    if (argc != 2) {
        cout << "Error" << endl;
    }

    if (!isInteger(argv[1])) return -1;

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



