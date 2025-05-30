%{
#include "y.tab.h"
#include <stdio.h>
count=1;
%}
%token ID FS GT LT PL AK BS MI EQ AD OR XR MD IV QM CN SC CM OB CB OP CP IC
%%
S: statements {printf("\n\nVALID!!\n\n");} ;
statements: statement statements|statement;
statement: ID EQ E SC {printf("STR[%s],%s\n",$1,$3);};
E:value operator value{
$$=$1;
if(!strcmp($2,"+"))
printf("ADD %s, %s\n", $1, $3);
else if (!strcmp($2, "-"))
printf("SUB %s, %s\n", $1, $3);
else if (!strcmp($2, "*"))
printf("MUL %s, %s\n", $1, $3);
else if (!strcmp($2, "/"))
printf("DIV %s, %s\n", $1, $3);
};
value: IC {printf("LOAD R%d, %s\n", count, $1); sprintf($$, "R%d", count++);}| ID {printf("LOAD
R%d, [%s]\n", count, $1); sprintf($$, "R%d", count++);};
operator: PL | AK | MI | BS {$$ = $1;};
%%
void yyerror(){
printf("Invalid Syntax!");
}
int main(){
yyparse();
return 0;
}
