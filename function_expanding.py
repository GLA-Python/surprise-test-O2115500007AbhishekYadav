def fun_exp(lst):
    data=[]
    for i in range(0,len(lst)-1):
        if lst[i]>lst[i+1]:
            a=lst[i]-lst[i+1]
        else:
            a=lst[i+1]-lst[i]
        data.append(a)

    flag = 0
    i = 0
    while i < len(data)-1:
        if(data[i] > data[i + 1]) or (data[i]==data[i+1]):
            flag = 1
        i += 1
        
    return False if flag==1 else True

    
lst=list(map(int,input().split()))
print(lst)
print(fun_exp(lst))
