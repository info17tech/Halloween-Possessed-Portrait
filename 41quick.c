//**objective:to perform sorting in a given list of numbers either in aascendind or descending order using quick sort.
//name:Bhavna joshi
//USN:18bbtit002
//date:7/09/19
//function name:quicksort
//output:

#include<stdio.h>
void quicksort(int[10],int,int);//declaring function quicksort
int main()
{int x[20], size,i;
	printf("enter size of array:");
		scanf("%d",&size);//scans for the int typed data type 
		printf("enter %d elements",size );
		for(i=0;i<size;i++)
			scanf("%d",&x[i]);//scans and refers to the address of i
		quicksort(x,0,size-1);
		printf("sorted elements:\n");
			for(i=0;i<size;i++)
				printf("%d\t",x[i] );
			return 0;
}
void quicksort(int x[10],int first, int last)
{
	int pivot, j,temp,i;
		if(first<last)
		{pivot=first;
			i=first;
			j=last;
				while(i<j)
					{while(x[i]<x[pivot]&& i<last)//increments when value of element is less than pivot 
						i++;
						while(x[j]>x[pivot])//decrements when greater than pivot
							j--;
						if(i<j)
							{temp=x[i];
								x[i]=x[j];
								x[j]=temp;
							}
					}
									temp=x[pivot];
									x[pivot]=x[j];
									x[j]=temp;
									quicksort(x,first,j-1);
									quicksort(x,j+1,last);		
			}
}