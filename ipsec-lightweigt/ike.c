#include <stdio.h>

typedef struct
{
  unsigned char Next_payload;
  unsigned char Critical_bit_Reserved;
  unsigned short int Payload_length;
  unsigned char Transform_Type;
  unsigned char Reserved;
  unsigned short int Transform_ID;
  unsigned char Authentication_Attribute[32];
}SECURITY_ASSOCIATION_PROPOSAL_TRANSFORM;

typedef struct
{
  unsigned char Next_payload;
  unsigned char Critical_bit_Reserved;
  unsigned short int Payload_length;
  unsigned char Proposal_number;
  unsigned char Protocol_ID;
  unsigned char SPI_Size;
  unsigned char Proposal_transform;
  SECURITY_ASSOCIATION_PROPOSAL_TRANSFORM Proposal_transforms;
}SECURITY_ASSOCIATION_PROPOSAL;

typedef struct
{
  unsigned char Next_payload;
  unsigned char Critical_bit_Reserved;
  unsigned short int Payload_length;
  SECURITY_ASSOCIATION_PROPOSAL proposal;
}SECURITY_ASSOCIATION_PAYLOAD;

typedef struct
{
  unsigned char Next_payload;
  unsigned char Critical_bit_Reserved;
  unsigned short int Payload_length;
  unsigned short int DH_Group_number;
  unsigned short int Reserved;
  unsigned long int Key_Exchange_Data[64];
}KEY_EXCHANGE_PAYLOAD;

typedef struct
{
  unsigned long long int Initiator_SPI;
  unsigned long long int Responder_SPI;
  unsigned char Next_payload;
  unsigned char Version;
  unsigned char Exchange_type;
  unsigned char Flags;
  unsigned long int Message_ID;
  unsigned long int Length;
}ISAKMP_HEADER;

typedef struct
{
  ISAKMP_HEADER header;
  SECURITY_ASSOCIATION_PAYLOAD sa_payload;
  KEY_EXCHANGE_PAYLOAD key_exchange_payload;
}ISAKMP_DATAGRAM;


#define security_association_proposal_transform_default \
{\
    0,\
    0x00,\
    sizeof(SECURITY_ASSOCIATION_PROPOSAL_TRANSFORM),\
    1,\
    0x00,\
    23,\
    {0}\
}

#define security_association_proposal_default \
{\
    0,\
    0x00,\
    sizeof(SECURITY_ASSOCIATION_PROPOSAL),\
    1,\
    1,\
    0,\
    1,\
    security_association_proposal_transform_default\
}

#define security_association_payload_default \
{\
    34,\
    0x00,\
    sizeof(SECURITY_ASSOCIATION_PAYLOAD),\
    security_association_proposal_default\
}

#define isakmp_header_default \
{\
    0x0000000000000000,\
    0x0000000000000000,\
    33,\
    0x20,\
    34,\
    0x08,\
    0x00000000,\
    sizeof(ISAKMP_DATAGRAM)\
}

#define key_exchange_default \
{\
    0,\
    0x00,\
    sizeof(KEY_EXCHANGE_PAYLOAD),\
    0x0e00,\
    0x0000,\
    {0}\
}

#define isakmp_datagram_default \
{\
    isakmp_header_default,\
    security_association_payload_default,\
    key_exchange_default\
}


int main()
{
    ISAKMP_DATAGRAM d = isakmp_datagram_default;
    printf("%ld\n",sizeof(ISAKMP_DATAGRAM));
    return 0;
}
