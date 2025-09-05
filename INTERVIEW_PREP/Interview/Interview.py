from common_imports import *


print("Hello")

r = "welcome"
s = r[::-1] # Reverse String
print(s)


print(' '.join(w[::-1] for w in 'My Name is Jessa'.split()))

# iterate and remove number
number_list = [x for x in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] if x <=50]
print(number_list)

# Display all duplicate items from a list
sample_list = {(x for x in [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]if[10, 20, 60, 30, 20, 40, 30, 60, 70, 80].count(x)<1 )}

# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
number1 = 50
number2 = 70
print(number1*number2 if number1*number2 <=1000 else number1+number2)

# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
for i in range(1, 10): print(i+i-1)

str = "PYnative"
for i in str[0::2]:
  print(i)

def fun(l):
  return l[0]==l[-1]
print(fun ([10, 20, 30, 40, 10]))
print(fun ([75, 65, 35, 75, 30]))


str_x = "Emma is good developer. Emma is a writer"
x = str_x.count("Emma")
print("Emma displayed:", x)


for i in range(1, 11):
  print(i)

str="india"
print(str[-1])

str="india"
print(str[:-1])

str="india"
print(str[::-1])

str="india"
print(str[1:])

str="india"
print(str[:1])

str="india"
print(str[::1])

str="india"
print(str[2:3:4])

list1 = ["aaa","bbb"]
list2 = ["ccc","ddd"]
list3= list1 + list2
list1.extend(list2)
print(list1)
print(' '.join(list1))
print(' '.join(list3))
print(list3)


list4 = ["aaa","bbb"]
list5 = ["ccc","ddd"]
list6 = dict(zip(list4,list5))
print(list6)


class A:
  count = 0
  def __init___(self):
    A.count += 1
    print('class A is called')
   
a1 = A()
a2 = A()
print(A.count)


list7 = ['india', 'is', 'my', 'country']
str =''.join(list7)
duplicate = []
for i in str:
  if str.count(i)>1 and i not in  duplicate:
    duplicate.append(i)
print(duplicate)


str1 = "test"
unique = []
for i in str1:
  if str1.count(i) == 1 and i not in unique:
    unique.append(i)
print(unique)


class B:
  def demo(self):
    print('in calss B')

class C(B):
  def demo(self):
    print('in calss C')

class D(B):
  def demo(self):
    print('in calss D')

class E(D, C): #Based on the order class will be called
  pass

test = E()
test.demo()


list9 = ['india', 'is', 'my', 'country']
[print(word) for word in list9 if word.startswith("i")]

##################################################################################################
def common_letters():
      d = "naina"
      c = "reene"
      s1 = set(d) #filter common letter
      s2 = set (c)
      s3 = set(s1 & s2)
      print(s1)
      print(s2)
      print(s3)
common_letters()

def common_words():
  a = "sheena loves eating mango, and her sister also loves eating mango"
  print({w for w in a.replace(",","").split() if a.split().count(w)>1})
common_words()

def into_dic():
  list1 =["naina", "kimi", "sheena"]
  list2 =[43232, 54325, 54343]
  list3 = dict(zip(list1, list2))
  print (list3)
into_dic()


# def add():
#   list1 = float(input("Enter the number1:" ))
#   list2 = float(input ("Enter the number2:" ))
#   list3 = (sum((list1,list2)))
#   print(list3)
# add()


def sq_root():
  list1 = 45
  print(math.sqrt(list1))
sq_root()

def identify_number():
  list1= -34
  if list1 == 0:
    print("number is zero")
  elif list1 > 0 :
    print("number is positive")
  elif list1 < 0 :
    print("number is negative")
identify_number()


def odd_or_even():
  list1= -33
  if list1 % 2 == 0 :
    print("number is even")
  elif list1 % 2 != 0 :
    print("number is odd")
odd_or_even()


def largest_num():
  list1= [34, 55, 67]
  for i in list1:
    if i is max(list1):
      print("largest number is :" , i)
largest_num()


def fact():
  r = math.factorial(5)
  print(r)
fact()


def fibo(n):
  if n <=1:
    return n
  else:
    return fibo(n-1)+fibo(n-2)
print(fibo(10))

def sorting():
  r = "Iam wrirting python program"
  a = r.split()
  for i in a:
    print((i))
sorting()

num  = 1
def x(num):
  try:
    float(num)
    return True
  except:
    return False
print(x(num))


# print (f"{sum: ,}")

#########################################################################################################################

def x(c):
  print(len(c))
x("Manjunatha")


def x(c):
  print(max(c))
x([1,2,3,4,5,6])

def v(b):
  b.extend([5.6,7,8])
  print(b)
v([1,2,3,4])

def v(b):
  b.append([5.6,7,8])
  print(b)
v([1,2,3,4])

def v(b):
  b.insert(1, [5.6,7,8])
  print(b)
v([1,2,3,4])

def v(b):
  b.remove(5) # remove value which u want to remove
  print(b)
v([1,2,3,4,5,6,7,8])

def v(b):
  b.pop(5) # remove value based on position
  print(b)
v([1,2,3,4,5,6,7,8])

def v(b):
  b.sort() # sort numbrers assending or descending
  print(b[-2])
v([34,56,23,12,89])

def v(b):
  n = b.count(5)
  print(n)
v([1,2,3,5,5,6,6,8]) 

def v(c):
  s = c.upper()
  print(s)
v('india')

def v(c):
  s = c.capitalize()
  print(s)
v('india')

def v(c):
  s = c.title()
  print(s)
v('india')

def v(c):
  s = c.replace("I", "E")
  print(s)
v('Interviews')


def print_name(name,id):
  print(name,id)
print_name("hi", 23)


def add(i , j): 
 return i+j
print(add(10, 20))

 

num = [1,2,3,4,5]
def square(num):
  return num **2
a = map(square,num)
print(list(a))



















