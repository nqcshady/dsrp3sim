import random as r
def arena(v1,v2,v3,v4,v5):
    print('4       A       B')
    print(f'                 ')
    print(f'     {v1}    {v2}      ')
    print(f'3   {v3}  -_-  {v4}   C')
    print(f'        {v5}        ')
    print(f'                 ')
    print('2       1       D')

def generation():
    seed,seed2=r.randint(0,2),r.randint(0,2)
    var1=[["up arrow",1],["down arrow",2],["no arrow",3]]
    var2=[["first in line",1],["second in line",2],["third in line",3]]
    return var1[seed], var2[seed2]

def get_answer(inline_value, arrow_value):
    answers = {
        1: {1: 4, 2: 3, 3: 5},
        2: {1: 2, 2: 1, 3: (2, 1)}, 
        3: {1: 4, 2: 3, 3: 5}
    }
    result = answers.get(inline_value, {}).get(arrow_value, None)
    if isinstance(result, tuple):
        return result  
    return result 

def logic_logic(val1,val2,usr):
    arrow_value=val1[1]
    inline_value=val2[1]  
    user_mapping = {
        "q": 1,
        "w": 2,
        "e": 3,
        "r": 4,
        "t": 5
    }
    usr2 = user_mapping.get(usr)
    ans = get_answer(inline_value, arrow_value)
    if usr2 == ans:
        return -1
    return ans
    
val1,val2=generation()
print("Note: This is assuming that there will never be an all circles pattern for dives 1 and 3, just use your eyes in game.")
print(f"You are {val2[0]} with {val1[0]}, which tower are you baiting?")
arena("q","w","e","r","t")
array=["q","w","e","r","t"]
usr=input("Tower (Q,W,E,R,T): ")
if logic_logic(val1,val2,usr) == -1:
    print("Congrats! You were correct!")
else:
    print(f"Incorrect, you were supposed to soak {array[logic_logic(val1,val2,usr)-1]}")
