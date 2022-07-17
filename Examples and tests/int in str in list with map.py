# Разработайте функцию holes_count(), которая подсчитывает количество отверстий 
# в заданном числе. Например, в цифре 8 два отверстия, в цифре 9 - одно. 
# В числе 146 - два отверстия. 
# Подсказка: используйте словарь для записи количества отверстий в цифрах

def holes_count(number):
    holes_dict={1:0,2:0,3:0,4:1,5:0,6:1,7:0,8:2,9:1}
    number_str=str(number)
    number_map=map(int,number_str)
    number_list=list(number_map)
    sum_holes=0
    for i in number_list:
        sum_holes+=holes_dict[i]
    return sum_holes

print(holes_count(123))
print(holes_count(8888))