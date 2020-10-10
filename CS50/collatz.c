#include <stdio.h>

int collatz(int n);

int main(void)
{
    int n = 27;
    printf("Colatz of %i = %i\n", n, collatz(n));
}

int collatz(int n)
{
    int steps;
    if (n == 1)
    {
        return 0;
    }

    if (n % 2 == 0) // n is even
    {
        return collatz(n/2) + 1;
    }

    if (n % 2 == 1) // n is odd
    {
        return collatz((3 * n) + 1 ) + 1;
    }
    return 0;
}