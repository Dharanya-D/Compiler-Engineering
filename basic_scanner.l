%{
int count = 0;
%}
alpha [a-zA-Z]
digit [0-9]
op    [+|*|,]

%%
int|float { printf("It is a keyword %s\n",yytext); }
{digit}+    { printf(" Cons %s\n",yytext); }
{alpha}({alpha}|{digit})* {printf(" Id%d %s\n",++count,yytext); }
%%
int main()
{
FILE *f1;
f1=fopen("input.c","r");
yyin=f1;
yylex();
return 1;
}
