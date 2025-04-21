#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
        if (ac == 2)
        {
                char* ptr = getenv(av[1]);
                printf("%p\n", ptr);
        }
}