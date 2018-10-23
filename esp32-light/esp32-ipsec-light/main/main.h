
typedef struct
{

}IPv6_ADDR;

typedef struct
{
    unsigned short int ver;
    unsigned short int flags;
    unsigned int length;
    unsigned long long int datagram_id;
    unsigned long long int what;
    unsigned long long int when;
    unsigned long long int where;
    unsigned long long int which_who;
    unsigned long long int appendix;
}DATAGRAM;

#define datagram_default \
{\
    100,\
    0,\
    80,\
    0,\
    0,\
    0,\
    0,\
    0,\
    0\
}


void data_handler(char* data,int len);
