#include <stdbool.h>

typedef struct
{
	unsigned long int n[128];//32bits*128
}int4096;
bool equal_int4096_int4096(int4096 a,int4096 b);
int4096 and_int4096_int4096(int4096 a,int4096 b);
int4096 add_int4096_int4096(int4096 a,int4096 b);
int4096 sub_int4096_int4096(int4096 a,int4096 b);
int4096 mul_int4096_int4096(int4096 a,int4096 b);
int4096 left_one_int4096_int4096(int4096 n,bool tmp_bit);
int4096 div_int4096_int4096(int4096 a,int4096 b);
int4096 mod_int4096_int4096(int4096 a,int4096 b);
void printf_int4096(int4096 a,int bits);

