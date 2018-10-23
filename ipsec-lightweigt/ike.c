#include <stdio.h>
#include "ike.h"
#include "main.h"
#include "diffie-hellman.h"

unsigned long long isakmp_len()
{   
    return sizeof(ISAKMP_DATAGRAM);
}

unsigned char* isakmp()
{   
    return (unsigned char*)&d;
}

#ifdef TEST_IKE
int main()
{
    isakmp();
    return 0;
}
#endif
