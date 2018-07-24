#include<stdio.h>
int main()
{
int a[10],i,c,sum=0;
printf("enter the limit of natural numbers");
//printf("  \nenter upto what u have to sum ");
scanf("%d",&c);
for(i=1;i<=c;i++)
{
 scanf("%d",&a[i]);   
}
for(i=1;i<=c;i++)
{
 printf("%d",a[i]);   
}
for(i=1;i<=2;i++)
{
sum=sum+a[i];
}
printf("\n%d",sum);
}
