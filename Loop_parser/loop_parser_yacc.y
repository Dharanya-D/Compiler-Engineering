%{
#include <stdio.h>
%}
%token DT ID SC WHILE IO FOR NUM DO CMP D
%start S
%%
S: ST {printf("Valid");exit(0);};
ST: WHILE '(' E ')' '{' E1 SC '}' | FOR '('EI SC E SC EINC')' '{' E1 SC '}'|D '{' E1 SC '}' WHILE '(' E
')' SC ;
E: ID CMP ID |ID CMP NUM ;
EI:DT ID '=' NUM ;
EINC:ID IO| ID DO;
E1: ID '=' E1|ID '+' E1|ID IO| ID;
%%
yyerror(){
printf("Invalid");
}
main(){
yyparse();
}
