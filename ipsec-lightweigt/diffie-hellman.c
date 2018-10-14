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
		unsigned long long int tmp1 = a.n[0];
		unsigned long long int tmp2 = b.n[0];
		tmp1 = tmp1 + tmp2;
		if(n < 127)tmp[n+1] = (tmp1 >> 32) + tmp[n];
		tmp[n] = (tmp1 << 32) >> 32;
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
			if(n+j>=128)
			{
				unsigned long long int tmp1;
				struct int4096 tmp2 = { {0} };
				tmp1 = a.n[n] * b.n[j];
				tmp2.n[n+j+1] = (tmp1 >> 32);
				tmp2.n[n+j] = (tmp1 << 32) >> 32;
				tmp = add_int4096_int4096(tmp,tmp2);
			}
		}
	}
	return tmp;
}

