def transfer(original,target):
    if len(original) != len(target):
        return "length not match"
    step=[]
    for i in range(len(original)):
        if original[i] != target[i]:
            step.append(f"replace the {original[i]} with the {target[i]} at the position {i}")
        return step
    
print(transfer("divi","abhi"))

################################################

def divi(start,goal):
    step=[]
    current=start

    while current !=goal:
        if current *3 <= goal:
            step.append(f"mutiply {current}by 3")
            current *= 3
        elif current +2 <= goal:
            step.append(f"add {current} to 2")
            current+=2
        else:
            step.append(f"sub 1 from {current}")
            current -= 1
    return step
print(divi(5,14))

#######################################3

def divi(start,goal):
    x,y = start
    gx,gy = goal
    step=[]

    while x < gx:
        x +=1
        step.append(f"move right to ({x},{y})")
    while y < gy:
        y +=1
        step.append(f"move up to ({x},{y})")
    return step
print(divi((0,0),(2,2)))

#####################################

def swap (start,goal):
    state=list(start)
    step=[]
    for i in range(len(state)-1,-1,-1):
        correct=goal[i]
        idx=state.index(correct)
        while idx < i:
            state[idx],state[idx+1]=state[idx+1],state[idx]
            step.append(f" Swap position {idx} to {idx+1} : {('  '.join(state))}")
            idx += 1
    return step
print(swap(['A','B','C'],['C','B','A']))
######################################################


def change_coin(amount,coin):
    change=[]
    for coin in sorted(coin,reverse=True):
        while amount >= coin:
            change.append(coin)
            amount -= coin 
    return change
    
print (change_coin(28,[5,2,1]))

##########################################

def transfer_string(original,target):
    step=[]
    for i in range(len(original)):
        if original[i] != target[i]:
            step.append(f"Replace {original} with {target} at postion {i}")
    return step
print(transfer_string('hello','helao'))

##################################################

def divi (start,goal):
    step=[]
    current=start
    while current != goal:
        if current < goal:
            current +=2
            step.append(f"add 2 : {current}")
            
        else:
            current -=1
            step.append(f"sub 1 : {current}")
    return step
print(divi(3,10))

##################################################

def move(start,goal):
    x,y=start
    gx,gy=goal
    step=[]
    while x<gx:
        x+=1
        step.append(f"right move ({x},{y})")
    while y<gy:
        y+=1
        step.append(f"move up ({x},{y})")
    return step
print(move((0,0),(2,1)))

############################################

def swap(start,goal):
    state=list(start)
    current=start
    step=[]
    for i in range(len(state)-1,-1,-1):
        current = goal[i]
        idx=state.index(current)
        while idx < i:
            state[idx],state[idx+1]=state[idx+1],state[idx]
            step.append(f"replace {idx} with {idx+1}: {(' '.join(state))}")
            idx +=1
    return step
print(swap(['A','B','C'],['B','C','A']))

#########################################

def divi(amount,coins):
    step=[]
    for coin in sorted(coins,reverse=True):
        while amount >= coin:
            step.append(coin)
            amount -=coin
    return step
print(divi(14,[5,1,2]))
###################




