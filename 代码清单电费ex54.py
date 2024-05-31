def e_check(n):
    t = 0
    if(n>500):
        t=(n-500)*0.9+0.7+200*0.6
    elif(n>200):
        t=(n-200)*0.7+200*0.6
    else:
        t = n*0.6
    return t

print("电费:",e_check(150)+e_check(250)+e_check(600))
