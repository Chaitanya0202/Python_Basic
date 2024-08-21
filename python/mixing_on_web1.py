# num= int(input())
# for i in range(1,11):
#     print(2**i)

# ---------------------+
# Finding the  number divisible by 13 i list ///use anonymous function to filter

# lst=[12, 65, 54, 39, 102, 339, 221,]
# result = list(filter(lambda x: (x % 13 == 0),lst))
# print(result)

# +++++++++++++++++++++++++++++++++++++++++++
# Converting The decimal Number to Binary ////With Octa and hecadeciamal

# dec=34
# print("After Converting Decimal Into Binary of ",dec)
# print(bin(dec))
# print(oct(dec))
# print(hex(dec))

# '''''''''''''''''''''''''';;;;;
# Finding The ASCII Value of Charector
# c='R'
# print(f"The ASCII Vaalue of {c} is {ord(c)}")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# file size/
# import os
# fil= os.stat('sonipe.txt')
# print(fil.st_size)
# ..........................................
#  current directories finding

import pathlib
print(pathlib.Path().absolute())