#Напишите функцию def distance_between_dots().

#Функция должна получать на вход координаты двух точек (в виде четырёх чисел) и возвращать расстояние между ними.

#Чтобы посчитать расстояние между точками, нужно воспользоваться формулой:

#Не забудьте проверить значения полученных аргументов!

def distance_between_dots(args):
    x1=args[0]
    y1=args[1]
    x2=args[2]
    y2=args[3]
    distance=((x1-x2)**2+(y1-y2)**2)**(1/2)    
    return distance

print (distance_between_dots([4,5,6,7]))