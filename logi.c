/*C Program to find max of 3 nos. using logical operator*/
#include<stdio.h>

void main()
{
 int a,b,c;
// clrscr();
 printf("\n\nEnter The value of a,b,c\n\n");
 scanf("%d%d%d",&a,&b,&c);
 if((a>b)&&(a>c))
 {
 printf("a is maximum");
 }
 else
 {
 if ((b>a)&&(b>c))
 {
 printf("b is maximum");
 }
 else
 {
 printf("c is maximum");
 }
 }
 getch();
 }

