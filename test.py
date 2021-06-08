input_list = [0, 0, 1, 2, 2, 3, 3, 4, 4]
temp = []
result = []



for i,v in enumerate(input_list):  
    if len(temp) == 0:
        temp.append(v)
        continue

    elif temp[-1] == v:
        temp.append(v)
            
    else:
        result.append(temp)
        
        temp = []
        temp.append(v)
        
    if temp[-1] == input_list[:-1]:
        result.append(temp)
        break
       
print(result)
