typedef struct
{
    unsigned long int n[4];
}
key_128b;

typedef struct
{
    unsigned long int n[64];
}
dh_res;


dh_res generate_origin_key(key_128b key);//128bits key
key_128b diffie_hellman(dh_res a,key_128b key);//2048bits key
