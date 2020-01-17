#Lists are arrays?!


list = ["list element one","list element two", "list element three"]

# print(len(list)) # returns 3

# print(list[0]) #returns the element in index 0 of the list

# print(list[0:2])#returns the first two elements. this slice method is excluding the second
# #point, so it will start slicing from 0 but stop at index 2.

# list.insert(0, "new element")
print(list)

list2 = ["1", "2"]

#list.insert(0, list2) #returns a 2D array with list 2 as the first element
# list.append(list2) #appending is only  adding the element to the back of the list.
#in this case returning also a 2D array but with this second list as the last element.
#if we want individual elements to be added to the original list we need to use extend method

list.extend(list2)
print(list)

removed = list.pop() #removes the last value in the list and returns the value
print(removed)
list.remove("1")
print(list)


#other methods:

# list.sort() #returns sorted items in alphabetical order and numbers in ascending order
#sort() function does not alter the original list it just returns the sorted version of the list
# list.reverse()
#if we want to sort the array and then reverse it we can use sort().reverse() but there's another way:
list3 = [5, 3944, 12, 0]
list4 = ["x", "e", "b"]
#alters the list in place
list3.sort(reverse=True) #returns [3944, 12, 5, 0]
list4.sort(reverse=True)#[3944, 12, 5, 0]
print(list3) 
print(list4)

# other methods for lists
nums = [4, -21, 0]
print(sum(nums)) # -17
print(min(nums)) # -21
print(max(nums)) # 4
print(nums.index(0)) # Index with the value is 2
#If we pass an element that is not in the list  we will get a value error.
#We can check for presence by using this instead:
# X in Y returns a boolean
print(0 in nums) #true
print(3 in nums) #false

# To make loops:
for item in enumerate(nums):
  print(item) #this returns the index and value as we loop in our list

for item in enumerate(nums, start= 1):#start at index 1
  print(item) 


words = ['cat', 'dog', 'bird']
#list to string
words_str = ''.join(words)
print(words_str)
words_list =  words_str.split(' ')#does not have a default separator!!!
print(words_list)


