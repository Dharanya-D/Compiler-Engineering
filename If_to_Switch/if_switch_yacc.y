%{
#include <stdio.h>
int cnt=0;
%}
%token NUM IF ELSE ELIF PRINTF ID OB CB OP CP SC COM QUOT EQ
%start S
%%
S: if elif | if else {printf("Valid Program");};
if : IF OP ID EQ NUM CP {printf("switch(%s)\n\{\ncase %d:",$3,cnt) ;} text;
elif: elif elif | ELSE IF OP ID EQ NUM CP {cnt++;printf("case %d:",cnt);} text| else;
else: ELSE {printf("default");} def;
text: PRINTF OP QUOT ID QUOT COM ID CP SC
{printf("{printf(%s%s%s%s);\n}\n",$3,$4,$5,$7);};
def:PRINTF OP QUOT ID QUOT CP SC {printf("{printf(%s%s%s);\n}\n",$3,$4,$5);};
%%
yyerror(){
printf("ERROR!");
}
main(){
yyparse();
}
