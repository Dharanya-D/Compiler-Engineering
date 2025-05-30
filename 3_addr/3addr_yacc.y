%{
#include "y.tab.h"
#include <stdio.h>
count=1;
%}
%token ID EQ PL MI AK BS OP CP IC SC
%%
S: statements {printf("\n\nvalid!!\n\n");} ;
statements: statement statements | statement ;
statement: ID EQ E {printf("%s = %s\n", $1, $3);};
E: E PL T {printf("t%d = %s %s %s\n", count, $1, $2, $3); sprintf($$, "t%d", count); count++;}
| E MI T {printf("t%d = %s %s %s\n", count, $1, $2, $3); sprintf($$, "t%d", count); count++;} |
value {$$ = $1;}
| T ;
T: T AK F {printf("t%d = %s %s %s\n", count, $1, $2, $3); sprintf($$, "t%d", count); count++;}
| T BS F {printf("t%d = %s %s %s\n", count, $1, $2, $3); sprintf($$, "t%d", count); count++;} |
value {$$ = $1;}
| F ;
F: OP E CP {$$ = $2;} | value {$$ = $1;};
value: IC | ID {$$ = $1;};
//operator: PL | AK | MI | BS {$$ = $1;};
%%
void yyerror(){
printf("Invalid Syntax!");
}
int main(){
yyparse();
return 0;
}
