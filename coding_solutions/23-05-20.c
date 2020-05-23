	C Program to Display first N Triangular Numbers (Where N is read from the Keyboard)
#include <stdio.h>
void triangular_series(int n)
{
for (int i = 1; i <= n; i++)
printf(" %d ", i*(i+1)/2);
}
int main()
{
int n ;
printf("Enter value for n");
scanf("%d",&n);
triangular_series(n);
return 0;
}
