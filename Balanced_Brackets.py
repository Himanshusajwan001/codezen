"""
Given a string expression, check if brackets present in the expression are balanced or not. Brackets are balanced if the bracket which opens last, closes first.
You need to return true if it is balanced, false otherwise.
Note: This problem was asked in initial rounds in Facebook
Sample Input 1 :
{ a + [ b+ (c + d)] + (e + f) }
Sample Output 1 :
true
Sample Input 2 :
{ a + [ b - c } ]
Sample Output 2 :
false
"""
def checkBalanced(expr):
    l=[]
    t=True
    opening=['{','[','(']
    closing=['}',']',')']
    dict={
        '}':'{',
        ']':'[',
        ')':'('
    }
    for i in expr:
        if(t==True):
            j=len(l)-1
            if i in opening:
                l.append(i)
            elif i in closing:
                if(len(l)==0):
                    t=False
                    break
                if(l.pop()!=dict[i] ):
                    t=False
                    break
    if(len(l)!=0):
        t=False
    return t

if __name__ == "__main__":
    exp=input()
    if checkBalanced(exp):
        print('true')
    else:
        print('false')
