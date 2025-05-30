%{
#include "y.tab.h"
%}
%%
[ \t]	;
int|float return DT;
[a-z][a-z0-9]* return ID;
"," return C;
";" return SC;
"\n" return NL;
. {return yytext[0];}
%%
