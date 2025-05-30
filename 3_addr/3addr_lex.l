%{
#include<stdio.h>
#include "y.tab.h"
extern int yylval;
%}
%%
[ \t\n] return 0;
[0-9]+ {yylval=strdup(yytext); return IC;}
[_a-zA-Z][_0-9a-zA-Z]* {yylval=strdup(yytext); return ID;}
"+" {yylval=strdup(yytext);return PL;}
"-" {yylval=strdup(yytext);return MI;}
"*" {yylval=strdup(yytext);return AK;}
"/" {yylval=strdup(yytext);return BS;}
"=" {yylval=strdup(yytext);return EQ;}
";" {return SC;}
"(" {return OP;}
")" {return CP;}
. return yytext[0];
%%
