#include<stdio.h>
#include<string.h>
int PrintArray(int A[],int size)
{
	for(int i=0;i<size;i++)
	{
		printf("for %d element of array, the value is %d\n",i,A[i]);
	}
}



int main()
{
//	int A[]={1,2,3,4};
//	printf("array is : %d\n",A);
//	int size = sizeof(A)/sizeof(A[0]);
//	int output = PrintArray(A,size);
//	printf("output is : %d\n",output);

	char B[6] = {'B','P','P','L','E'};
	char *C = B;
	printf("C is : %s",C);
	
	
//	printf("The char is %s\n",B);
//	printf("The size of char is %d\n",sizeof(B));
//	printf("The strlen of char is %d\n",strlen(B));
}
