#--creating an empty list

my_list=[]

my_list.extend([10,20,30,40])
print(my_list)

#--inserting the value 15 at the second position in the list

my_list.insert(1,15)
print(my_list)

#--extending the my_list

my_list.extend([50,60,70])
print(my_list)

#---Removing the last element from my_list

my_list.pop()
print(my_list)

#--Sort my_list in ascending order

my_list.sort()
print(my_list)

#-- index of the value 30 in my_list

print(my_list.index(30))