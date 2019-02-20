a=10
b=20
a if a<b else b
10
x=1<2<3
x
True
x=1<3<2
x
False
def compare(a,b,c):
    return a if a<b else b
def compare(a,b,c):
    return a if a<b and a<c else b if b<c and b<a else c

