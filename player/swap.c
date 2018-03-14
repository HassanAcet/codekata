#include <stdio.h>
#include <string.h>
#include <conio.h>
void main()
{
     char str[20],temp;
     int a,b;
     clrscr();
     printf("\nEnter a string : ");
     scanf("%s",str);
     printf("\n\nOriginal String     : %s",str);
     for(a=0;a<strlen(str);a=a+2){
     temp = str[a];
     str[a] = str[a+1];
     str[a+1] = temp;
     }
     printf("\nAfter Swap String      : %s",str);
     getch();
}
