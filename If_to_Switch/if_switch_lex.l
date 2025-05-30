%{
#include <stdio.h>
#include "y.tab.h"
extern int yylval;
%}
%%
[ \t\n] ;
"if" return IF;
"else" return ELSE;
"printf" return PRINTF;
[a-zA-Z%][a-zA-Z0-9+]* {yylval=strdup(yytext); return ID;}
"{" return OB;
"}" return CB;
"(" return OP;
")" return CP;
[0-9]+ {yylval=atoi(yytext);return NUM;}
"==" return EQ;
";" return SC;
"," return COM;
\" {yylval =strdup(yytext);return QUOT;}
. return yytext[0];
%%
