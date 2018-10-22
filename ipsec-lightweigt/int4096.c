#include <stdio.h>
#include "main.h"
#include "int4096.h"
//*******************************************************//
//return = a == b
bool equal_int4096_int4096(int4096 a,int4096 b)
{
	for(int i=0;i != 128;++i)
	{
		if(a.n[i] != b.n[i])
                {
			return 0;
		}
	}
	return 1;
}
//*******************************************************//
//return = a & b
int4096 and_int4096_int4096(int4096 a,int4096 b)
{
	int4096 tmp = { {0} };
	for(int i=0;i != 128;++i)
	{
		tmp.n[i] = a.n[i] & b.n[i];
	}
	return tmp;
}
//*******************************************************//
//return = a + b
int4096 add_int4096_int4096(int4096 a,int4096 b)
{
	int4096 tmp = { {0} };
	for(int n=0;n != 128;++n)
	{
		unsigned long long int tmp1 = a.n[n];
		unsigned long long int tmp2 = b.n[n];
		unsigned long long int tmp3 = tmp.n[n];
		tmp1 = tmp1 + tmp2 + tmp3;
		if(n+1 < 128)tmp.n[n+1] = (tmp1 >> 32);
		tmp.n[n] = tmp1 & 0xFFFFFFFF;
	}
	return tmp;
}
//*******************************************************//
//return = a - b
int4096 sub_int4096_int4096(int4096 a,int4096 b)
{
	int4096 tmp = { {0} };
	for(int n=0;n != 128;++n)
	{
		unsigned long long int tmp1 = a.n[n];
		unsigned long long int tmp2 = b.n[n];
		unsigned long long int tmp3 = tmp.n[n];
		if(tmp3 >> 31 == 1)tmp3+=0xFFFFFFFF00000000; 
		tmp1 = tmp1 - tmp2 + tmp3;
		if(n < 127)tmp.n[n+1] = (tmp1 >> 32);
		tmp.n[n] = tmp1 & 0xFFFFFFFF;
	}
	return tmp;
}
//*******************************************************//
//return = a * b
int4096 mul_int4096_int4096(int4096 a,int4096 b)
{
	int4096 tmp = { {0} };
	for(int n=0;n != 128;++n)
	{
		for(int j=0;j != 127-n;++j)
		{
			int4096 tmp3 = { {0} };
			unsigned long long int tmp1 = (unsigned long long int)b.n[n] * (unsigned long long int)a.n[j];
			tmp3.n[n+j] = (unsigned long int)(tmp1 & 0xFFFFFFFFULL);
			if((n+j+1)<128)
			{
				tmp3.n[n+j+1] = (unsigned long int)(tmp1 >> 32);
			}
			tmp = add_int4096_int4096(tmp,tmp3);
		}
	}
	return tmp;
}
//**************************************************************
int4096 left_one_int4096_int4096(int4096 n,bool tmp_bit)
{
	for(int i=0;i != 128;++i)
	{
		unsigned long long int tmp1 = n.n[i];
		tmp1 = tmp1 << 1;
		tmp1 += tmp_bit;
		tmp_bit = (bool)(tmp1&0x100000000ULL);
		n.n[i] = (unsigned long long int)(tmp1&0xFFFFFFFFULL);
	}
	return n;
}
//*******************************************************//
//return = a / b
int4096 div_int4096_int4096(int4096 a,int4096 b)
{
	int4096 tmp = { {0} };
	int4096 res = { {0} };
	
	for(int i = 4095;i >= 0;--i)
	{
		tmp = left_one_int4096_int4096(tmp,(bool)((0x1<<(i&0x1F))&a.n[(i&0xFE0)>>5]));
		if(sub_int4096_int4096(tmp,b).n[127]&0x80000000)//-
		{
			res.n[(i&0xFE0)>>5] = res.n[(i&0xFE0)>>5] & ~(0x1<<(i&0x1F));
		}
		else//+
		{
			tmp = sub_int4096_int4096(tmp,b);
			res.n[(i&0xFE0)>>5] = res.n[(i&0xFE0)>>5] | (0x1<<(i&0x1F));
		}
	}
	return res;
}
//*******************************************************//
//return = a % b
int4096 mod_int4096_int4096(int4096 a,int4096 b)
{
	int4096 tmp = { {0} };
	//printf("enter\n");
	
	for(int i = 4095;i >= 0;--i)
	{
		//printf("%d\n",i);
		tmp = left_one_int4096_int4096(tmp,(bool)((0x1<<(i&0x1F))&a.n[(i&0xFE0)>>5]));
		if(!(sub_int4096_int4096(tmp,b).n[127]&0x80000000))//+
		{
			tmp = sub_int4096_int4096(tmp,b);
		}
	}
	return tmp;
}
//********************************************************//
//print a
void printf_int4096(int4096 a,int bits)
{
	for(int i=127-(4096-bits)/32;i >= 0;--i)
	{
		printf("%08llx",(0xFFFFFFFFULL)&(unsigned long long int)a.n[i]);
	}
	printf("\n");
}

#ifdef TEST_INT4096
int main()
{
	int4096 a = { {0x916f7671,0xf58ef549,0x93b877ca,0x962d1043,0xeeb892d6,0xa325a5d9,0x362e1f21,0x1950bd9b} };
	//7**90=1950bd9b  362e1f21  a325a5d9  eeb892d6  962d1043  93b877ca  f58ef549  916f7671
	int4096 b = { {0x00000363} };
	int4096 c = { {0x0} };
	printf("start\n");
	c = div_int4096_int4096(a,b);
	printf_int4096(c);
	c = mod_int4096_int4096(a,b);
	printf_int4096(c);
	return 0;
}
#endif
