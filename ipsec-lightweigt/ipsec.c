#include "isakmp.h"
#include "diffie-hellman.h"
#include "aes.h"

volatile ISAKMP_DATAGRAM d = isakmp_datagram_default;
volatile key_128b key;

volatile unsigned long long SPI = 0x2976167890123456;

uint8_t key[] = {0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c};

void ipsec_init()
{

}

void ipsec_recv_filter(uint8_t* datagram)
{
    for(int i = 0;i != 5;++ i)
    {
        uint8_t buffer[16];
        AES_ECB_decrypt(datagram+(16*i), key,buffer , 16);
        for(int j = 0;j != 16;++ j)
        {
            datagram[16*i+j] = buffer[j];
        }
    }
}

void ipsec_send_filter(unsigned char* datagram)
{
    for(int i = 0;i != 5;++ i)
    {
        uint8_t buffer[16];
        AES_ECB_encrypt(datagram+(16*i), key,buffer , 16);
        for(int j = 0;j != 16;++ j)
        {
            datagram[16*i+j] = buffer[j];
        }
    }
}
