#Задана строка S, состоящая из малых латинских букв. 
#Требуется узнать длину наибольшей подстроки, в которой все буквы одинаковы.

#Например:

def most_long_latter_str(text):
    latter=text[0]
    count=1
    most_count=1
   
    for a in text:
        if a is latter:
            count+=1
        else:
            latter=a
            if most_count<count:
                most_count=count
            count=1
                
            
    return most_count

print (most_long_latter_str("adddbbbbbbbaabaa"))