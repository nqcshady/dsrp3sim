import random as r
def arena(v1,v2,v3,v4,v5):
    print('4       A       B')
    print(f'                 ')
    print(f'     {v1}    {v2}      ')
    print(f'3   {v3}  -_-  {v4}   C')
    print(f'        {v5}        ')
    print(f'                 ')
    print('2       1       D')

def arrow_logic():
    seed=r.randint(0,2)
    var1=["up arrow",1]
    var2=["down arrow",2]
    var3=["no arrow",3]
    match seed:
        case 0:
            return(var1)
        case 1:
            return(var2)
        case 2:
            return(var3)
    
def inline_logic():
    seed=r.randint(0,2)
    var1=["first in line",1]
    var2=["second in line",2]
    var3=["third in line",3]
    match seed:
        case 0:
            return(var1)
        case 1:
            return(var2)
        case 2:
            return(var3)
        
def logic_logic(val1,val2,usr):
    arrow_value=val1[1]
    inline_value=val2[1]
    ans2=0
    match usr:
        case "q":
            usr2=1
        case "w":
            usr2=2
        case "e":
            usr2=3
        case "r":
            usr2=4
        case "t":
            usr2=5
    if inline_value == 1:
        if arrow_value == 1:
            ans=4
        elif arrow_value == 2:
            ans=3
        elif arrow_value == 3:
            ans=5 
    elif inline_value == 2:
        if arrow_value == 1:
            ans=2
        elif arrow_value == 2:
            ans=1
        elif arrow_value == 3:
            ans=2
            ans2=1
    elif inline_value == 3:
        if arrow_value == 1:
            ans=4
        elif arrow_value == 2:
            ans=3
        elif arrow_value == 3:
            ans=5
    if usr2 == ans:
        return -1
    elif usr2 == ans2:
        return -1
    else:
        return ans
    
val1=arrow_logic()
val2=inline_logic()
print("Note: This is assuming that there will never be an all circles pattern for dives 1 and 3, just use your eyes in game.")
print(f"You are {val2[0]} with {val1[0]}, which tower are you baiting?")
arena("q","w","e","r","t")
array=["q","w","e","r","t"]
usr=input("Tower (Q,W,E,R,T): ")
log=logic_logic(val1,val2,usr)
if log == -1:
    print("Congrats! You were correct!")
else:
    print(f"Incorrect, you were supposed to soak {array[log-1]}")
