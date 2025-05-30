%{
#include "y.tab.h"
%}
%%
[ \t\n] ;
int|float return DT;
[0-9]+ return NUM;
while return WHILE;
for return FOR;
do return D;
[a-zA-Z][a-zA-Z0-9]* return ID;
";" return SC;
"++" return IO;
"--" return DO;
[<>][=]? return CMP;
. {return yytext[0];}
%%
