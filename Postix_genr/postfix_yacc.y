%{
#include <stdio.h>
#include <stdlib.h>
%}
%token NUM ID
%left '+''-'
%left '*''/'
%%
start:T;
T: T'+'T {printf("+");}
| T'-'T {printf("-"); }
| T'*'T {printf("*"); }
| T'/'T {printf("/");}
| NUM {printf("%d",$1);}
| ID {printf("%s",$1);}
;
%%
int main()
{
printf("\nEnter expression:");
yyparse();
return 0;
}
int yyerror()
{
printf("Error");
}
