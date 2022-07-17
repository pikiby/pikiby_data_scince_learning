# Напишите функция find_min_number(), которая принимает три числа на вход 
# и возвращает наименьшее из них.

# Используйте условия для решения задачи

def find_min_number(*args):
    
    min_n=args[0]
    args_l=len(args)
    for i in range(0,args_l):
        if args[i]<min_n:
            min_n=args[i]   
    return min_n

print(find_min_number(1, 2, 3))


###########

def find_min_number(a, b, c):
    list_n=[a,b,c]
    min_n_1=list_n[0]
    list_l=len(list_n)
    for i in range(0,list_l):
        if list_n[i]<min_n_1:
            min_n_1=list_n[i]   
    
    return min_n_1

###########

def sum_min_numbers(a, b, c):
    
    list_n=[a,b,c]
    min_n_1=list_n[0]
    list_l_1=len(list_n)
    
    for i in range(0,list_l_1):
        if list_n[i]<min_n_1:
            min_n_1=list_n[i] 
    

    list_n.remove(min_n_1)
    min_n_2=list_n[0]
    list_l=len(list_n)
    for i in range(0,list_l):
        if list_n[i]<min_n_2:
            min_n_2=list_n[i]
     
    return min_n_1+min_n_2

print(sum_min_numbers(1, 2, 3))