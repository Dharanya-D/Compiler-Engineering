%{
#include <stdio.h>
#include "y.tab.h"
extern int yylval;
%}
%%
[0-9]+ {yylval=strdup(yytext); return IC;}
[_a-zA-Z][A-ZA-z0-9_]* {yylval=strdup(yytext);return ID;}
"+" {yylval=strdup(yytext);return PL;}
"-" {yylval=strdup(yytext);return MI;}
"*" {yylval=strdup(yytext);return AK;}
"/" {yylval=strdup(yytext);return BS;}
"\\" {yylval=strdup(yytext);return FS;}
">" {yylval=strdup(yytext);return GT;}
"<" {yylval=strdup(yytext);return LT;}
"=" {yylval=strdup(yytext);return EQ;}
"&" {yylval=strdup(yytext);return AD;}
"|" {yylval=strdup(yytext);return OR;}
"^" {yylval=strdup(yytext);return XR;}
"%" {yylval=strdup(yytext);return MD;}
"~" {yylval=strdup(yytext);return IV;}
"?" {yylval=strdup(yytext);return QM;}
":" {yylval=strdup(yytext);return CN;}
";" {return SC;}
"," {return CM;}
"{" {return OB;}
"}" {return CB;}
"(" {return SC;}
")" {return SC;}
%%
