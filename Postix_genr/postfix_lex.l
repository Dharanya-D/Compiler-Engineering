%{
#include<stdio.h>
#include "y.tab.h"
extern int yylval;
%}
%%
[0-9]+ {yylval = atoi(yytext); return NUM;}
[a-z][a-zA-Z]* {yylval=strdup(yytext);return ID;}
[\n\t] return 0;
. return yytext[0];
%%
yywrap() {return 1;}

