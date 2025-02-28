
#def cenas(a:str,b:int,c:bool=False):
    #print(a,b,c)

def cenas(a,b,c=1,*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    print(a,b,c,args,kwargs)

a="OLA"
b=3.14
c=True
ar = (1,2,3,4)
z = {'foo':'bar','baz':'bav'}
# cenas()
# cenas(a)
# cenas(b)
# cenas(c)
# cenas(a,b)
# cenas(b,c)
cenas(a,b,c,1,2,3,4)
cenas(a,b,c,cenas=True,mais="cenas",*ar)


