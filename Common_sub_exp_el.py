def del_containing_rhs(var):
    flag=0
    x=hashtable.items()
    for lhs,rhs in x:
        if(var in lhs):
            flag=lhs
            break
    if(flag!=0):
        hashtable.pop(flag)
file=open("expr1.txt",'r')
text=file.readlines()
hashtable={}
values=[]
for i in text:
    val=i.removesuffix('\n')
    values.append(val.split('='))

for lhs,rhs in values:
    if ('-' in rhs) or ('/' in rhs):
        rev=rhs
    else:
        rev=rhs[::-1]
    if (hashtable.get(rhs,0)==0) and (hashtable.get(rev,0)==0):
        del_containing_rhs(lhs)
        print(lhs,'=',rhs)
        hashtable[rhs]=lhs
        
    elif (hashtable.get(rhs,0)!=0): 
        print(lhs,'=',hashtable[rhs])
    elif (hashtable.get(rev,0)!=0):
        print(lhs,'=',hashtable[rev])
