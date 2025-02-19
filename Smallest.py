smallest_num=None 
interval=[42,89,35,4,7,8,800,54,48,77,444]
for i in interval:
    if smallest_num is None or i< smallest_num:
        smallest_num=i
print( smallest_num)