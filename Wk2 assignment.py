# Create my_list
my_list = []
# Append 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#Insert 15 at the 2nd position in the list
my_list.insert(1, 15)
print(my_list)
#Extend my_list with 50,60,70
my_list.extend([50, 60, 70])
print(my_list)
#remove the last element from the list
my_list.pop()
print(my_list)
#sort list in ascending order
my_list.sort()
print(my_list)
# find and print index of value 30 
index_30 = my_list.index(30)
print(index_30)

