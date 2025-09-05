#Factorial
num = 5
fact = 1
for i in range(1, num+1):
    fact*=i
print(fact)

#Prime Number
for i in range(1, 101):
    if i>1:
        for j in range(2, i):
            if (i%j)==0:
                break
        else:
            print(i, end=' ')

#Palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

#fibonacci  
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b

#sum of elements in a list
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)


#Find largest element in a list
numbers = [10, 24, 5, 75, 32]   
largest = max(numbers)
print(largest)      

#Checking element is present or not in List
def check_element(lst, element):
    return element in lst   
print(check_element([1, 2, 3, 4, 5], 3))
print(check_element([1, 2, 3, 4, 5], 6))    

#Making copy or clone of List.
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list.copy()      
print(cloned_list)  

#Removing duplicates from List
def remove_duplicates(lst):
    return list(set(lst))       
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates(['a', 'b', 'b', 'c', 'a']))

#Count occurrences of an element in List
def count_occurrences(lst, element):
    return lst.count(element)   
print(count_occurrences([1, 2, 2, 3, 4, 4, 5], 2))
print(count_occurrences(['a', 'b', 'b', 'c', 'a'], 'a'))

#Finding second largest number from List
def second_largest(lst):
    unique_lst = list(set(lst))  
    unique_lst.sort()             
    if len(unique_lst) < 2:
        return None                
    return unique_lst[-2]
print(second_largest([10, 24, 5, 75, 32]))
print(second_largest([5, 5, 5, 5])) 

#Checking if String contains special character
import re
def contains_special_characters(s):
    return bool(re.search(r'[^a-zA-Z0-9]', s))  
print(contains_special_characters("Hello@World"))
print(contains_special_characters("HelloWorld"))

#Finding common elements between two Lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))      
print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
print(common_elements(['a', 'b', 'c'], ['b', 'c', 'd']))    














 




 

