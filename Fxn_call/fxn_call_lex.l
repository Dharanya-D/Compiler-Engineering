%{
#include "y.tab.h"
%}
%%
[ \n\t] ;
int|float|void return DT;
if return IF;
else return ELSE;
while return WHILE;
[0-9]+ return NUM;
[a-zA-Z_][a-zA-Z_]* return ID;
[><][=]? return CMP;
"=" return AO;
";" return SC;
"++" return IO;
. {return yytext[0];}
%%
