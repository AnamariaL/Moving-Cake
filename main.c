#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int hanoi(int n,char a[],char b[],char c[]){

//set selection to n (i.e) if n is 1
    if(n==1){
        printf("\nMove layer %d from  %c plate to  %c plate",n,a,b);
    }
    else{
    //call the function hanoi(recursion) and return value to the function parameters
    //(n will get replaced with value of n-1).
   // Therefore  n-1 over n,a over a,c over b,b over c
        hanoi (n-1,a,c,b);
        printf("\nMove layer %d from  %c plate to  %c plate",n,a,b);
        //call the function hanoi and like the above function return values to function hanoi
        //as n-1 for n, c for a, b for b,a for c
        hanoi (n-1,c,b,a);
    }
}
int main() {
int n;//layers
char a[6]="silver"; //declare array to silver
char b[6]="bronze";//declare array to bronze
char c[6]="golden";//declare array to golden
printf("How many layers of cake  : ");
scanf("%d",&n);
//call the function and return the values
hanoi (n,a,b,c);

    return 0;
}
