%{
#include<stdio.h>
%}
%token DT ID C SC NL
%start s
%%
s: stmt NL {printf("Valid \n");exit(0);};
stmt: DT varlist SC ;
varlist: varlist C ID | ID;
%%
yyerror()
{
printf("error");
}
main()
{
yyparse();
}
