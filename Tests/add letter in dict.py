def letters_count (x):

    first_latter = x[0]
    count = 0
    new_str=''
    for i in x:
        if i == first_latter:
            count+=1
        else:
            new_str+=first_latter+str(count)
            first_latter=i
            count=1
    
    new_str+=first_latter+str(count)
    return new_str      
    
print(letters_count('aaabbccccdaa'))

