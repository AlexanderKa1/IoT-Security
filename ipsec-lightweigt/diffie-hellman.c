#include <stdio.h>
#include "diffie-hellman.h"

struct int4096
{
	unsigned long int n[128];//32bits*128
};

struct int4096 add_int4096_int4096(struct int4096 a,struct int4096 b)
{
	struct int4096 tmp = { {0} };
	for(int n=0;n != 128;++n)
	{
		unsigned long long int tmp1 = a.n[n];
		unsigned long long int tmp2 = b.n[n];
		tmp1 = tmp1 + tmp2;
		if(n < 127)tmp.n[n+1] = (tmp1 >> 32) + tmp.n[n+1];
		tmp.n[n] = (tmp1 << 32) >> 32 + tmp.n[n];
	}
	return tmp;
}


struct int4096 sub_int4096_int4096(struct int4096 a,struct int4096 b)
{
	struct int4096 tmp = { {0} };
	for(int n=0;n != 128;++n)
	{
		unsigned long long int tmp1 = a.n[n];
		unsigned long long int tmp2 = b.n[n];
		unsigned long long int tmp3 = tmp.n[n];
		if(tmp3 >> 31 == 1)tmp3+=0xFFFFFFFF00000000; 
		tmp1 = tmp1 - tmp2 + tmp3;
		if(n < 127)tmp.n[n+1] = (tmp1 >> 32);
		tmp.n[n] = (tmp1 << 32) >> 32;
	}
	return tmp;
}



struct int4096 mul_int4096_int4096(struct int4096 a,struct int4096 b)
{
	struct int4096 tmp = { {0} };
	for(int n=0;n != 128;++n)
	{
		for(int j=0;j != 128;++j)
		{
			if(n+j<128)
			{
				unsigned long long int tmp1;
				struct int4096 tmp2 = { {0} };
				tmp1 = a.n[n] * b.n[j];
				tmp2.n[n+j+1] = (tmp1 >> 32) + tmp2.n[n+j+1];
				tmp2.n[n+j] = (tmp1 << 32) >> 32 + tmp2.n[n+j];
				tmp = add_int4096_int4096(tmp,tmp2);
			}
		}
	}
	return tmp;
}

struct int4096 mod_int4096_int4096(struct int4096 a,struct int4096 b)
{
	struct int4096 tmp = { {0} };
	for(int i = 0;i != 4096;++i)
	{
		struct int4096 tmp2 = {{a.n[4095-n]}};
		tmp = add_int4096_int4096(tmp,tmp2);

	}
}

void printf_int4096(struct int4096 a)
{
	for(int i=127;i >= 0;--i)
	{
		printf("%08X",a.n[i]);
	}
	printf("\n");
}

struct int4096 step_mul(unsigned int n)
{
	if(n > 1)
	{
		struct int4096 a = { {n} };
		return mul_int4096_int4096(step_mul(n - 1),a);
	}
	else
	{
		struct int4096 a = { {1} };
		return a;
	}
}



int main()
{
	struct int4096 a = { {60} };
	struct int4096 b = { {55} };
	printf_int4096(sub_int4096_int4096(a,b));
	return 0;
}







