"""
 "Krojenie" list
"""

list1 = [10,20,30,40,50,60,70,80,90,100]

print(f"7 parametr = {list1[6]}, inaczej {list1[-4]}")
print(f"przedzial = {list1[3:-2]}")
print(f"przedzial ze stepem 2 = {list1[3:-2:2]}")
print(f"inne: przedzial ze stepem 2 = {list1[::2]}")
print(f"przedzial ze stepem 0 = {list1[::]}")
list1.reverse()
print(f"lista odwrócona = {list1}")
print(f"lista odwrócona = {list1[::-1]}")
list1.reverse()
print(f"lista odwrócona = {list1[::-1]}")

#sortowane
lista2 = [9,-10,11-100,20,0,0.1,-1234]
lista2.sort(reverse=True)
print(f"lista posortowana = {lista2}")