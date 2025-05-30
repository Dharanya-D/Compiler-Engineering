%{
#include <stdio.h>
%}
%token DT ID AO SC CMP IF WHILE IO ELSE NUM
%start S
%%
S: ST {printf("Valid");exit(0);};
ST: DT ID '(' EI ')' '{' E EIF ELOOP '}' ;
EI: DT ID | EI ',' DT ID;
E: ID AO EEX SC ;
EEX: ID '+' EEX |ID '*' EEX| ID |NUM;
EIF: IF '(' ECMP ')' '{' E '}' ELSE '{' E'}';
ECMP: ID CMP EEX;
ELOOP: WHILE '(' ECMP ')' '{' EINC '}' ;
EINC: ID IO SC;
%%
yyerror(){
printf("Invalid");
}
main(){
yyparse();
}
