import array

arr = array.array('i',[1,2,3])

print("The new created array is : ", end=" ")
for i in range (0, 3):
    print(arr[i], end=" ")
print("\r")

# using append() to insert new value at end
arr.append(4)


print("The appended array is : ", end="")
for i in range (len(arr)):
    print (arr[i], end=" ")


arr.insert(2,5)
# 换行
print("\r")

print ("The array after insertion is : ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")


print("\r")
"""
pop function removes the element at the position mentioned in
its argument and return it. 
"""
print(arr.pop(2))
# 换行
print("\r")

print ("The array after insertion is : ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")

print("\n")
print("---------------------------\n")
"""
remove function  is used to remove the first occurrence of the
value mentioned in its arguments
"""
arr = array.array('i',[1,2,3,1,5])

# print original array
print("The new created array is : ", end="")
for i in range(0,5):
    print(arr[i],end=" ")

print("\r")
# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print("The array after removing is : ",end="")
for i in range(len(arr)):
    print(arr[i],end=" ")

print("\r-------------------------\r")
"""
index() the function returns the index of the first occurrence 
of the value mentioned in the arguments.
"""

arr = array.array('i', [1,2,3,1,2,5])

# printing original array
print ("The new created array is : ",end="")
for i in range(0,6):
    print(arr[i],end=" ")

print("\r")

print(arr.index(2))
print("-------------------\r")

arr.reverse()
for i in range(len(arr)):
    print(arr[i],end=" ")


arr = array.array()


