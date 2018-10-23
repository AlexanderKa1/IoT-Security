//********************************************************************//
//                          Author:Ark Sun                            //
//                           2018-10-22                               //
//                      arksun9481@gmail.com                          //
//                                                                    //
//        A deffie-hellman implementation with pure C code            //
//********************************************************************//
#include <stdio.h>
#include "diffie-hellman.h"
#include "int4096.h"
#include "main.h"


int4096 modp2048 = 
{{
0xffffffff,0xffffffff,0x8aacaa68,0x15728e5a,
0x98fa0510,0x15d22618,0xea956ae5,0x3995497c,
0x95581718,0xde2bcbf6,0x6f4c52c9,0xb5c55df0,
0xec07a28f,0x9b2783a2,0x180e8603,0xe39e772c,
0x2e36ce3b,0x32905e46,0xca18217c,0xf1746c08,
0x4abc9804,0x670c354e,0x7096966d,0x9ed52907,
0x208552bb,0x1c62f356,0xdca3ad96,0x83655d23,
0xfd24cf5f,0x69163fa8,0x1c55d39a,0x98da4836,
0xa163bf05,0xc2007cb8,0xece45b3d,0x49286651,
0x7c4b1fe6,0xae9f2411,0x5a899fa5,0xee386bfb,
0xf406b7ed,0x0bff5cb6,0xa637ed6b,0xf44c42e9,
0x625e7ec6,0xe485b576,0x6d51c245,0x4fe1356d,
0xf25f1437,0x302b0a6d,0xcd3a431b,0xef9519b3,
0x8e3404dd,0x514a0879,0x3b139b22,0x020bbea6,
0x8a67cc74,0x29024e08,0x80dc1cd1,0xc4c6628b,
0x2168c234,0xc90fdaa2,0xffffffff,0xffffffff
}};


int4096 mod_fast(int4096 l,int4096 k,int4096 p)
{
    int4096 zero = {{0x0}};

    int4096 res = {{0x1}};
    int4096 tmp = l;
    for(int i=0;i!=128;++i)
    {
        int4096 tmp2 = {{0}};
        tmp2.n[(i/32)] = k.n[(i/32)] & (0x1<<(i%32));	
        
        if(!equal_int4096_int4096(tmp2,zero))
        {
            res = mod_int4096_int4096(mul_int4096_int4096(res, tmp), p);
        }
        tmp = mod_int4096_int4096(mul_int4096_int4096(tmp, tmp), p);
    }
    return res;
}

dh_res generate_origin_key(key_128b key)//128bits key
{
    int4096 l = {{2}};
    int4096 k = {{key.n[0],key.n[1],key.n[2],key.n[3]}};//128bits
    int4096 r = {{0}};
    dh_res res = {{0}};
    key.n[0] = k.n[0];
    key.n[1] = k.n[1];
    key.n[2] = k.n[2];
    key.n[3] = k.n[3];
    r = mod_fast(l,k,modp2048);//diffie-hellman modp2048
    for(int i=0;i!=64;++i)
    {
        res.n[i] = r.n[i];
    }
    return res;
}


key_128b diffie_hellman(dh_res a,key_128b key)//2048bits key
{
    int4096 l = {{0}};
    int4096 k = {{key.n[0],key.n[1],key.n[2],key.n[3]}};
    int4096 r = {{0}};
    key_128b final_key;
    for(int i=0;i!=64;++i)
    {
        l.n[i] = a.n[i];
    }
    r = mod_fast(l,k,modp2048);//diffie-hellman modp2048
    final_key.n[0] = r.n[0];
    final_key.n[1] = r.n[1];
    final_key.n[2] = r.n[2];
    final_key.n[3] = r.n[3];
    return final_key;
}

void printf_key(key_128b x)
{
    printf("%08lx%08lx%08lx%08lx",x.n[3],x.n[2],x.n[1],x.n[0]);
    printf("\n");
}

#ifdef TEST_DH
int main()
{
    key_128b keya = {{random_32b(),random_32b(),random_32b(),random_32b()}};
    key_128b keyb = {{4653324,random_32b(),35654564,random_32b()}};
    dh_res a = generate_origin_key(keya);
    dh_res b = generate_origin_key(keyb);
    key_128b _a = diffie_hellman(b,keya);
    key_128b _b = diffie_hellman(a,keyb);
    printf_key(_a);
    printf_key(_b);
    return 0;
}
#endif
