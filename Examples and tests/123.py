

temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
from collections import OrderedDict
temps.sort(key=lambda x: x[1], reverse=True)
od = OrderedDict(temps)
print(od)