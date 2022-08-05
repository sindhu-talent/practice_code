# print("helloworld")


# l=[1,2,1,10,11,12,12,9]
# res=A(l)
# print(res)
# s='astring'
# s1=s[-1:-12:-2]
# print(s1)
# str[5:-3]
##
# str="programiz"
# print('str=',str)
# print('str[0]=',str[0])
# print('str[-1]=',str[-1])
# print('str[1:5]=',str[1:5])
# print('str[5:-3)')
# l=str.capitalize()
# print(l)
# str=("geeks for geeks")
# l1=str.count('geeks')
# print(l1)
# str='capitalize'
# l2=str.index('i')
# print(l2)
# str='this is python'
# l3=str.split()
# print(l3)
# str='this is python'
# l4=str.swapcase()
# print(l4)
# str='python is programming language'
# l5=str.title()
# print(l5)
## LIST:
# '" list=[]
# print(list)
# list=[]
# list.append(10)
# list.append(20)
# print(list)
# list1=[10,20,30]
# list.append(list1)
# print(list)
# list1.count(1)
# print(list1)
# list1[2]=50
# print(list1)
# list2=[50,60,70]
# list1.extend(list2)
# print(list1)
# list1.insert(2,[80,90])
# print(list1)
# list=[90,60,70,50]
# list.remove(50)
# print(list)
# list=[90,60,70,50]
# list.pop()
# print(list)
# list=[50,60,80,100]
# list.sort(reverse=True)
# print(list)
# list=[50,60,80,100]
# list.copy()
# print(list)
# # l=('s','i','n','d','h','u')
# # print(l.count('i'))
## count:
# # l=(2,3,4,5,6,5,4,4,3)
# # print(l.count(4))
# # index:
# l=(1,2,3,("geeks","for"),6,7,8,9)
# print(l[4])"'

## QUESTION 1 :
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))
#
## QUESTION 2:
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# x=int (input ('enter a value'))
# print(fact(x))
## QUESTION 3:
# n=int(input('enter a value'))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print (d)
## QUESTION 4:
# values=input('enter a value')
# l=values.split("enter a value")
# t=tuple(l)
# print (l)
# print (t)
## QUESTION 5;
# class InputOutString(object):
#     def__init__(self):
#     self.s = ("")
# def getString(self):
#     self.s = raw_input()
# def printString(self):
#     print self.s.upper()
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
## QUESTION 6:
# #!/usr/bin/env python
# import math
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print (','.join(value))
## QUESTION 7:
# input = input('enter a value')
# dimensions=[int(x) for x in input.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
# print(multilist)
## QUESTION 8:
# items=[x for x in input().split(',')]
# items.sort()
# print (','.join(items))
# l=[]
# s=input("enter a string")
# if s:
#     l.append(s.upper())
# for i in l:
#     print(i)
# s=input()
# words = [word for word in s.split(" ")]
# print (" ".join(sorted(list(set(words)))))
## QUESTION 9:
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     i = int(p, 2)
#     if i%5==0:
#         value.append(p)
# print (','.join(value))
## QUESTION 10:
# values = []
# for i in range(1000, 3001):
#      s = str(i)
#      if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and(int(s[3])%2==0):
#         values.append(s)
# print (",".join(values))
## QUESTION 11:
# s =input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print ("LETTERS", d["LETTERS"])
# print ("DIGITS", d["DIGITS"])
## QUESTION 12:
# s =input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#      d["UPPER CASE"]+=1
#     elif c.islower():
#      d["LOWER CASE"]+=1
#     else:
#         pass
# print ("UPPER CASE", d["UPPER CASE"])
# print ("LOWER CASE", d["LOWER CASE"])
## QUESTION 13:
# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print (n1+n2+n3+n4)
## QUESTION 14:
# values = input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print( ",".join(numbers))
## QUESTION 15:
# netAmount = 0
# while True:
#     s =input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print (netAmount)
## QUESTION 16:
# import re
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print (",".join(value))
##QUESTION 17:
# from operator import itemgetter, itemgetter
# l = []
# while True:
#     s =input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
# print (sorted(l, key=itemgetter(0,1,2)))
##QUESTION 18:
# def putNumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
#             for i in reverse(100):
#                 print(i)
##QUESTION 19:
# x={'apple','banana','cherry'}
# y={'go0gle','microsoft','apple'}
# z=x.difference(y)
# print(z)
# x={'apple','banana'}
# x.discard('banana')
# print(x)
##QUESTION 20:
# import math
# pos=[0,0]
# while True:
#     s=input("enter a value")
#     if not s:
#         break
#     movement=s.split("enter a value")
#     direction=movement[0]
#     steps=int(movement[1])
#     if direction=="UP":
#         Pos[0]+=steps
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         Pos[1]+=steps
#     else:
#         pass
# print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
##QUESTION 20:
# freq={} #frequency of words in text
# line=input()
# for word in line.split():
#     freq[word]=freq.get(word,0)+1
# words=freq.keys()
# word.sort()
# for w in word:
#     print("%s:%d" %(w,freq[w]))
##QUESTION 21:
# def square(num):
#     return num ** 2
# print (square(2))
# print (square(3))
# print (abs.__doc__)
# print (int.__doc__)
# print (input.__doc__)
##QUESTION 22:
# def square(num):
#     '''Return the square value of the input number.
#     The input number must be integer.
#     '''
#     return num ** 2
# print(square(2))
# print(square.__doc__)
##QUESTION 22:
# class Person:
#     name=("Person")
#     def __init__(self, name = None):
#       self.name=name
# jeffrey=Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name))
# nico = Person("nico")
# nico.name="Nico"
# print("%s name is %s" % (Person.name, nico.name))
##QUESTION 23:
# def SumFunction(number1, number2):
#     return (number1+number2)
# print (SumFunction(1,2))
##QUESTION 23:
# def printValue(n):
#     print (str(n))
# printValue(3)
##QUESTION 24:
# def printvalue(s1,s2):
#     print (int(s1)+int(s2))
# printvalue("3","4")
##QUESTION 25:
# def printvalue(s1,s2):
#     print(s1+s2)
# printvalue("3","4")
##QUESTION 26:
# def printValue(s1,s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1>len2:
#         print(s1)
#     elif len2>len1:
#          print(s2)
#     else:
#         print(s1)
#         print(s2)
#     printvalue("one","three")
##QUESTION 27:
# def checkvalue(n):
#     if n%2==0:
#         print("it is an even number")
#     else:
#         print("it is an odd number")
##QUESTION 27.B:
# def printDict():
#     d=dict()
#     d[1]=1
#     d[2]=2**2
#     d[3]=3**2
#     print(d)
# printDict()
##QUESTION 28:
# def printDict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=1**2
#     print(d)
# printDict()
##QUESTION 29:
# def printDict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=1**2
#     for (k,v) in d.items():
#         print(v)
##QUESTION 30:
# printDict()
# def printDict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=1**2
#     for k in d.keys():
#         print(k)
# printDict()
##QUESTION 31:
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(li)
# printList()
##QUESTION 32:
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[:5])
# printList()
##QUESTION 33:
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[-5:])
# printList()
##QUESTION 34:
# def printTuple():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(tuple(li))
# printTuple()
##QUESTION 35:
# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print(tp1)
# print(tp2)
##QUESTION 36:
# li=list()
# for i in li:
#     if tp[i]%2==0:
#         li.append(tp[i])
# tp1=tuple(li)
# print(tp1)
##QUESTION 37:
# s=input()
# if (s=="Yes" or s=="YES" or s=="yes"):
#     print("yes")
# else:
#     print("No")
##QUESTION 38:
# li=[1,2,3,4,5,6,7,8,9,10]
# evenNumbers=filter(lambda x : x%2==0,li)
# print(evenNumbers)
##QUESTION 39:
# li=[1,2,3,4,5,6,7,8,9,10]
# squareNumber=map(lambda x : x**2,li)
# print(squareNumber)
##QUESTION 40:
# li=[1,2,3,4,5,6,7,8,9,10]
# evenNumbers=map(lambda x : x**2,filter(lambda x : x%2==0,li))
# print(evenNumbers)
##QUESTION 41:
# evenNumbers=filter(lambda x: x%2==0,range(1,21))
# print(evenNumbers)
##QUESTION 42:
# class American(object):
#     @staticmethod
#     def printNationality():
#         print("america")
# anAmerican=American()
# anAmerican.printNationality()
# American.printNationality()
# class American(object):
#     pass
# class Newyorker(American):
#     pass
# anAmerican=American()
# aNewyorker=Newyorker()
# print(anAmerican)
# print(aNewyorker)
##QUESTION 42:
# class circle(object):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return self.radius**2*3.14
# acircle=circle(2)
# print(acircle.area())
##QUESTION 43:
# class Rectangle(object):
#     def __init__(self,l,w):
#         self.length = l
#         self.width = w
#     def area(self):
#         return self.length*self.width
# aRectangle=Rectangle(2,10)
# print(aRectangle.area())
##QUESTION 44:
# class shape(object):
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class  Square(shape) :
#     def __init__(self, l):
#         shape. __init__(self)
#         self.length = l
#     def area(self):
#         return self.length * self.length
# aSquare=Square(3)
# print(aSquare.area())
##QUESTION 45:
# def throws():
#      return 5/0
# try:
#      throws()
# except ZeroDivisionError:
#      print("division by zero")
# except exceptioneroor:
#     print('caught an exception')
# finally:
#      print ('In finally block for cleanup')
##QUESTION 46:
# class MyError(exception):
#     """MY own exception class
#     Attributes:
#         message __ expalanation of the Error
#     """
#     def __init__(self,message):
#       self.message=message
# error=MyError("something wrong")
##QUESTION 50:
# import re
# emailAddress=input()
# pat2="(\w+)@((\w+\.)+(com))"
# r2=re.match(pat2,emailAddress)
# print(r2.group(1))
## QUESTION 51:
# import re
# emailAddress=input()
# pat2="(\w+)@(\w+)\.(com)"
# r2=re.match(pat2,emailAddress)
# print(r2.group(2))
## QUESTION 52:
# import re
# s=input()
# print(re.findall("\d+",s))
## QUESTION 53:
# unicodestring=u"hello world!"
# print(unicodestring)
##QUESTION 54:
# s = input()
# u = s.encode("utf-8")
# print(u)
##QUESTION 55:
# -*- coding:utf-8 -*-
##QUESTION 56:
# n=int(input())
# sum=0.0
# for i in range (1,n+1):
#     sum+=float(float(i)/(i+1))
# print(sum)
##QUESTION 57:
# n=int(input())
# sum=0.0
# for i in range(1,n+1):
#     sum+=float(float(i)/(i+1))
#     print(sum)
## QUESTION 58 :
# def f(n):
#     if n==0:
#         return 0
#     return f(n-1)+100
# n=int(input())
# print(f(n))
## QUESTION 59:
# def f(n):
#     if n==0:return 0
#     elif n==1:return 1
#     else:return (n-1)+f(n-2)
# n=int(input())
# print(f(n))
##QUESTION 60:
# def f(n):
#     if n==0:return 0
#     elif n==1: return 1
#     else:return f(n-1)+f(n-2)
# n=int(input())
# values=[str(f(x)) for x in range (0,n+1)]
# print(",".join(values))
## QUESTION 61:
# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#          yield i
#         i+=1
# n=int(input())
# values=[]
# for i in EvenGenerator(n):
#     values.append(str(i))
# print(",".join(values))
##QUESTION 62:
# def NumGenerator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i
# n=int(input())
# values=[]
# for i in NumGenerator(n):
#     values.append(str(i))
#     print(",".join(values))
## QUESTION 63:
# li=[2,4,6,8]
# for i in li:
#     assert i%2==0
# print(li)
## question 64:
# expression=input()
# print(eval(expression))
##QUESTION 65:
# import math
# def bin_search(li,element):
#     bottom=0
#     top=len(li)-1
#     index=-1
#     while top>=bottom and index==-1:
#         mid=int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index=mid
#         elif li[mid]>element:
#             top=mid-1
#         else:
#             bottom=mid+1
#     return index
# li=[2,5,7,9,11,17,222]
# print(bin_search(li,11))
# print(bin_search(li,12))
## QUESTION 66:
# import math
# def bin_search(li,element):
#     bottom=0
#     top=len(li)-1
#     index=-1
#     while top>=bottom and index==-1:
#         mid=int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index=mid
#         elif li[mid]>element:
#             top=mid-1
#         else:
#             bottom=mid+1
#     return index
# li=[2,5,7,9,11,17,222]
# print(bin_search(li,11))
# print(bin_search(li,12))
## QUESTION 67:
# import random
# print(random.random()*100)
## QUESTION 68:
# import random
# print(random.random()*100-5)
## QUESTION 69:
# import random
# # print(random.choice([i for i in range(11) if i%2==0]))
##                                  FUNCTIONS
# def even_list(L):
#     L1=[]
#     for i in L:
#         if i%2==0:
#             L1.append(i)
#     return L1
# a=even_list([1,2,3,4,5,6,7,8])
# print(a)
# b=even_list([11,12,13,14])
# print(b)
## QUESTION 70:
# import random
# print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))
## QUESTION 71:
# import random
# print(random.sample(range(100, 201),5))
## QUESTION 72:
# import random
# print(random.sample([i for i in range(100,201) if i%2==0],5))
## QUESTION 73:
# import random
# print(random.sample([i for i in range (1,1001) if i%5==0 and i%7==0],5))
## QUESTION 74:
# import random
# print(random.randrange(7,16))
## QUESTION 75:
# import zlib                     NOT EXCUTED
# s='hello world!hello world!hello world!hello world!'
# t= zlib.compress(s)
# print(t)
# print(zlib.decompress(t))
## QUESTION 76:
# from timeit import Timer
# t=Timer("for i in range(100):1+1")
# print(t.timeit())
## QUESTION 77:
# from random import shuffle
# li=[3,6,7,8]
# shuffle(li)
# print(li)
## QUESTION 78:
# subjects=["I","You"]
# verbs=["Play","Love"]
# objects=["Hockey","Football"]
# for i range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentence="%s %s %s." % (subjects[i],verbs[j],objects[k])
#              print(sentence)
## QUESTION 79:LIST COMPREHENSION
# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%2!=0]
# print (li)
## QUESTION 80:
# li = [12,24,35,70,88,120,155]
# li = [x for x in li if x%5!=0 and x%7!=0]
# print (li)
## QUESTION 81:
# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i%2!=0]
# print (li)
## QUESTION 82:
# array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
# print (array)
## QUESTION 83:
# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
# print (li)
##QUESTION 84:
# li = [12,24,35,24,88,120,155]
# li = [x for x in li if x!=24]
# print (li)
## QUESTION 85:
# set1=set([1,3,6,78,35,55])
# set2=set([12,24,35,24,88,120,155])
# set1 &= set2
# li=list(set1)
# print (li)
## QUESTION 86:
# def removeDuplicate( li ):
#     newli=[]
#     seen = set()
#     for item in li:
#         if item not in seen:
#             seen.add( item )
#         newli.append(item)
#     return newli
# li=[12,24,35,24,88,120,155,88,120,155]
# print (removeDuplicate(li))
## QUESTION 87:
# class Person(object):
#     def getGender( self ):
#         return "Unknown"
# class Male( Person ):
#     def getGender( self ):
#         return "Male"
# class Female( Person ):
#     def getGender( self ):
#         return "Female"
# aMale = Male()
# aFemale= Female()
# print (aMale.getGender())
# print (aFemale.getGender())
## QUESTION 88:
# dic = {}
# s=input()
# for s in s:
#     dic[s] = dic.get(s,0)+1
# print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
# QUESTION 89:
# s=input("enter a value")
# s = s[::-1]
# print (s)
## question 90:
# s=input("enter a value")
# s = s[::2]
# print (s)
##question 91:
# import itertools
# print (list(itertools.permutations([1,2,3])))
## question 92:
# def solve(numheads,numlegs):
#     ns='No solutions!'
#     for i in range(numheads+1):
#         j=numheads-1
#     if 2*i+4*j==numlegs:
#         return i,j
#     numheads=35
#     numlegs=94
#     solutions=solve(numheads,numlegs)
#     print(solutions)
#

##                                              set 1

# ##
# def test(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# s=result1result2=test(5,10)
# print(s)
# def test():
#     print('sindhu')
#     return
# res=test()
# QUESTION 1:
# def table(n):
#     for i in range(1,11):
#         print("%d*%d=%d" %(n,i,n*i))
# n=12
# table(n)
## QUESTION 2:
# def arearectangle(a,b):
#     return(a*b)
# def perimeterrectangle(a,b):
#     return(2*(a+b))
# a=8;
# b=7;
# print("Area=",arearectangle(a,b))
# print("perimeter=",perimeterrectangle(a,b))
# ## QUESTION 3:
# import math
# def find_circumference(radius):
#     return 2 * math.pi * radius
# def find_Area(radius):
#     return math.pi * radius * radius
# r = float(input('please Enter the radius of a circle: ')
# circumference = find_Circumference(r)
# area = find_Area(r)
# print(" Circumference Of a Circle = %.2f" % circumference)
# print(" Area Of a Circle = %.2f" % area)
##QUESTION 3:
import fileinput
import math
# def find_Diameter(radius):
#     return 2 * radius
# def find_Circumference(radius):
#     return 2 * math.pi * radius
# def find_Area(radius):
#     return math.pi * radius * radius
# r = float(input(' Please Enter the radius of a circle: '))
# diameter = find_Diameter(r)
# circumference = find_Circumference(r)
# area = find_Area(r)
# print("\n Diameter Of a Circle = %.2f" % diameter)
# print(" Circumference Of a Circle = %.2f" % circumference)
# print(" Area Of a Circle = %.2f" % area)
##QUESTION 4:
# def power(a,b):
#     if(b==0):
#         return 1
#     elif a==0:
#         return 0
#     elif b==1:
#         return a
#     else:
#         return a*power(a,b-1)
# print(power(6,2))
## QUESTION 5:
# x=int(input("enter a age"))
# if x>=18:
#     print("user is valid for voting:,")
# else:
### QUESTION 6:
# number=int(input("enter any number is even or odd"))
# if(number%2)==0:
#     print("the number is even")
# else:
#     print("the number is odd")
## QUESTION 7:
# number=11
# if number >=1:
#     for i in range(2, int(number / 2) + 1):
#        if (number%i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")
# else:
#     print(num, "is not a prime number")
## QUESTION 8:
# def factorial(prevFact, prev, n):
#     global size
#     for x in range((prev + 1), n + 1):
#         size = multiply(x, prevFact, size)
# for i in range((size - 1), -1, -1):
#         print(prevFact[i], end="value")
# print(end" ")
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if(num1 > num2):
#   print(num1, "is greater")
# elif(num1 < num2):
#     print(num2, "is greater")
# else:
#     print("Both are equal")
## QUESTION 9:
# def fizzler(num):
#     if number % 3 != 0 and number % 5 != 0:
#         return num
#     if number% 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     if number % 3 == 0:
#         return "Fizz"
#         return "Buzz"
#     if __name__ == ("__main__"):
#         number = int(input("Enter a number: "))
# print(fizzler(num))
## QUESTION 9:
# def sum_of_numbers(limit):
#     total = 0
#     for i in range(limit):
#         if (i % 3 == 0 or i % 5 == 0):
#             total = total + i
#             i = i + 1
#         return total
# userInput = int(input("Enter limiting number: "))
# plusOne = userInput + 1
# print(sum_of_numbers(plusOne))
## example:
# total_sum = 0
# for i in range(1000):
#     if (i%3 == 0 or i%5 == 0):
#         total_sum = total_sum+i
# print (total_sum)
##NUMBERS PATTERN:
# rows=6
# for i in range(rows):
#     for j in range(i):
#         print(i, end=' ')
#     print('')
## QUESTION 10:
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
## QUESTION 11:
# n=int(input("Enter the number till you want to check: "))
# primes = []
# for i in range (2, n+1):
#     for j in range(2, i):
#         if i%j == 0:
#             break
#     else:
#         primes.append(i)
# print(primes)
## QUESTION 12:
# def check_speed(speed):
#     if speed<=70:
#         return 'ok'
#     elif speed>=70:
#         points=(speed-70)/5
#         prints('points = {}'.form at(points))
#     if points>=12:
#         return 'license suspended'
#         check_speed(80)
#     point=2
## QUESTION 13:
# def speed(s):
#     dp=(s-70)/5
#     if s<=70:
#         print("ok")
#     elif s>70:
#         print("demerit points:",dp)
#         if dp>12:
#             print("license is cancelled")
# s=int(input("enter a speed of car:"))
# speed(s)

##                                         SET 1: PROGRAMS
## QUESTION 1:
# color=["red","green","white","black","pink","yellow"]
# color=[x for (i,x) in enumerate (color) if i not in (0,4,5)]
# print(color)
# OR
# l=['red','green','white','black','pink','yellow']
# l.remove('red')
# l.remove('pink')
# l.remove('yellow')
# print(l)
## QUESTION 2:
# def match_words(words):
#     ctr=0
#     for word in words:
#         if len(word)>1 and word[0]==word[-1]:
#             ctr+=1
#     return ctr
# print(match_words(['abc','xyz','aba','1221']))
## QUESTION 3:
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))
## QUESTION 4:
# d={1:['a','g','k','i'],2:['g','b','c'],3:['a','k','g','c']}
# l=[]
# for i in d.values():
#     l.extend(i)
# print(l)
# c=input("enter a character:")
# print("number of occurence of given character in a given dictionary is:", l.count(c))
## QUESTION 5: SUM OF THE LIST
# def sum_list(items):
#     sum_numbers=0
#     for x in items:
#         sum_numbers+=x
#     return sum_numbers
# print(sum_list([1,2,-8]))
## QUESTION 6:DUPLICATE VALUES IN LIST
# a=[10,20,30,20,10,50,60,40,80,50,40]
# dup_items=set()
# uniq_items=[]
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
# print(dup_items)
##QUESTION 7: REVERSE LIST
# l=[1,2,3,4,5,6]
# l1=[]
# for i in range(len(l)):
#     l1.insert(i,l[-1])
#     l.pop(-1)
# print(l1)
## QUESTION 8:FACTORIAL OF ANY NUMBER
# num=int(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("factorial of",num,"is",fact)
## QUESTION 9: MULTIPLICATION NUMBER OF GIVEN NUMBER
# num = int(input("Enter the number: "))
# print("Multiplication Table of", num)
# for i in range(1, 11):
#    print(num,"X",i,"=",num * i)
##QUESTION 10:
# num = int(input("Please Enter any Number: "))
# i = 1
# print("Natural Numbers from 1 to {0} are".format(num))
# while (i <= num):
#  print (i, end = ' ')
#  i = i + 1
## QUESTION 11:
from logging import exception

numbers = [12, 75, 150, 180, 145, 525, 50]


# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     elif item % 5 == 0:
#         print(item)
## QUESTION 12:LENGTH OF LIST
# n = len([123])
# print("The length of list is:" ,n)
##ANOTHER ONE
# n = len([1,2,3])
#  print("The length of list is: ", n)
##QUESTION 13: EVEN POSITIONS ARE IN LIST
# L = [10,20,30,40,50,60,70,80,90,100]
# print("The list is :")
# print(L)
# print("The elements in even positions are : ")
# for i in range(1, len(L), 2):
#    print(L[i])
## QUESTION 14:    TWO INTEGER NUMBERS AND THEIR PRODUCT AND SUM
# while True:
#     x=int(input("enter a value"))
#     y=int(input("enter a value"))
#     z=(x*y)
#     if z>>1000==True:
#         print(x+y)
#     else:
#         print(x*y)
## QUESTION 15:
# z='capitalize'
# for x in range(6,len(z),2):
#     if x%2==0:
#         print(z[x])
## QUESTION 16:
# sampleDict = {"class":{"student": {"name": "Mike","marks":{"physics": 70,"history": 80}}}}
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
# print(sampleDict['class']['student']['marks']['history'])
## QUESTION 17:
# Dict = {"name":"kelly","age":25,"salary":8000,"city":"new york"}
# keys = ["name", "salary"]
# newDict = {k: Dict[k] for k in keys}
# print(newDict)
## QUESTION 18:DICTIONARY VALUE OR NOT
# dictionary={"a":1,"b":2}
# contains1=1 in dictionary.values()
# print(contains1)
## TRUE
# dictionary={"a":1,"b":2}
# contains3=3 in dictionary.values()
# print(contains3)
##  FALSE
## QUESTION 19:
# d = {'a':10,'b':7,'c':2}
# answer = 1
# for i in d:
#     answer = answer * d[i]
# print(answer)
#
#                                        SET2 PROGRAMS
#
###QUESTION 1:
# d={'a':'b','b':'c','c':'a'}
# a='abc'
# b=''
# for i range d :
#     for j in range d:
# if i==j:
#         b=b+str(d[i])
# print(d)
## QUESTION 1:
# d={'a':'b','b':'c','c':'a'}
# enter=str(input("enter a input:"))
# k=list(i for i in enter)
# ans=[]
# for i in k:
#     ans.append(d[i])
#     print("".join(ans))
## QUESTION 7: STAR PROBLEM
# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end='')
#     print("\r")
## QUESTION 9:
# class py_solution:
#     def reverse_words(self, s):
#         return ' '.join(reversed(s.split()))
# print(py_solution().reverse_words('my dad'))
## QUESTION 2:
# num = int(input("Enter a number: "))
# fac=1
# if num < 0:
#    print(" factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        fac = fac*i
#    print("The factorial of",num,"is",fac)
## QUESTION 3:
# list=[12,40,50,60,70,2,3,6,900,1000]
# max=2
# min=1000
# for i in list:
#     if max<i:
#         max=i
#     elif min>i:
#         min=i
# print("maximum of element",max)
# print("minimum of element",min)
# QUESTION 5:
# l=[1,2,3,4,5,6,7,8,9]
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append("even")
#     if i%2!=0:
#             l1.append("odd")
# print(l1)
## QUESTION 6:
# def sumofnumber(limit):
#     total=1
#     for i in range(limit+1):
#         if i%3==0 or i%5==0:
#             total=total+i
#             i=i+1
#     print(total)
# print(sumofnumber(20))
## QUESTION 8:
# def fizz_buzz(n):
#     if n%3==0 and n%5==0:
#         print("fizz_buzz")
#     elif n%3==0:
#         print("fizz")
#     elif n%5==0:
#         print("buzz")
#     else:
#         print(n)
# fizz_buzz(90)
##QUESTION 9:
# def fun(str):
#     s=''
#     for i in str:
#         s=i+s
#         return s
# str= 'python'
# print(fun(str))
### QUESTION 10:
# l=[5,10,30,'hai',5,6]
# d={}
# for i in range(0,len(l)):
#     d[i]=l[i]
#     print(d)
#
##
# l1=[0,1,2,3,4,5]
# l2=[6,7,8,9,10]
# l1,l2.extend("hi")
# print(l1+l2)
# QUESTION 4:
# english=float(input("please enter english marks"))
# telugu=float(input("please enter telugu marks"))
# maths=float(input("please enter maths marks"))
# physics=float(input("please enter physics marks"))
# total=english+telugu+maths+physics
# percentage=(total/400)*100
# print("total marks=%.2f",total)
# print("marks percentage=%.2f",percentage)
# if percentage>=90:
#     print("A grade")
# elif percentage>=70:
#     print("B grade")
# elif percentage>=50:
#     print("C grade")
# elif percentage>=35:
#     print("D grade")
# else:
#     print("fail")


# def smart_check(concatinate):
#     def inner(a,b):
#         if type(a)==str and type(b)==str:
#             return concatinate(a,b)
#         else:
#             print("concatinate not possible")
#     return inner
# @smart_check
# def concatinate(a,b):
#     print(a+b)
# concatinate("10","16")
###
##
##
# def smart_check(concatinate):
#     def inner(a,b):
#          if type(a)==str and type(b)==str:
#              return concatinate(a,b)
#          else:
#              print("concatinate not possible")
#     return inner
# @smart_check
# def concatinate(a,b):
#      print(a+b)
# concatinate("for","geeks")
##
# def smart_check(concatinate):
#      def inner(a,b):
#           if type(a)==int and type(b)==int:
#               return concatinate(a,b)
#           else:
#               print("concatinate not possible")
#      return inner
# @smart_check
# def concatinate(a,b):
#     print(a+b)
# concatinate(10,20)
# def gen(n):
#      for i in range(0,n,2):
#          yield i
# x=gen(20)
# print(next(x))
# print(next(x))
# print(next(x))
#                OR
# res=(x for x in range(0,20,2))
# print(next(res))
# print(next(res))
# GENERATOR FUNCTION:
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# for value in simpleGeneratorFun():
#     print(value)
### GENERATOR OBJECT:
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# x = simpleGeneratorFun()
# print(next(x))
# print(next(x))
# print(next(x))
## USING FOR LOOP:
# def generator2():
#     num = 1
#     yield num
#     num += 1
#     yield num
#     num += 1
#     yield num
# for item in generator2():
#     print(item)
## GENERATOR EXPRESSION:
# lst = [1,2,3,4]
# generator = (x**2 for x in lst)
# for item in generator:
#     print(item)
##                            LAMBDA FUNCTIONS

# l=[1,2,3,4,5,6]
# l1=list(map(lambda i:i*i,l))
# print(l1)
##                                  OR
# l1=set(map(lambda i:i*i,[1,2,3,4,5]))
# print(l1)
# tables = [lambda x=x: x * 10 for x in range(1, 11)]
# print(tables())
##
# table=[lambda x = x: x*10 for x in range(1.11)]
# print(table())
# NORMAL PROGRAM
# def even_list(l):
#     l1=[]
#     for i in l:
#         if i%2==0:
#             l1.append(i)
#     return l1
# print(even_list([1,2,3,4,5,6]))
## FILTERS FUNC():
# l1=list(filter(lambda i:i%2==0,[1,2,3,4,5,6]))
# print(l1)
# REDUCE FUNC():
# from functools import reduce
# l1=(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))
# print(l1)

# x = "GeeksforGeeks"
# (lambda x: print(x))(x)

# string = 'GeeksforGeeks'
# (lambda string: print(string))(string)

# string = 'GeeksforGeeks'
# print(lambda string: string)

# animals = ['dog', 'cat', 'parrot', 'rabbit']
# uppered_animals = list(map(lambda animal: str.upper(animal), animals))
# print(uppered_animals)
## QUESTION 1:
# def evenOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")
# evenOdd(1)
# evenOdd(2)
## QUESTION 2:
# x=int(input("enter a age value"))
# if x>=18:
#     print("valid for voting:",x)
# else:
#     print("not valid for vote:",x)
## QUESTION 3:
# def isPerfect(n):
#     sum = 1
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             sum = sum + i + n / i
#         i+=1
#     return (True if sum == n and n != 1 else False)
# print("Below are all perfect numbers till 1000")
# n = 2
# for n in range(1000):
#     if isPerfect(n):
#         print(n, " is a perfect number")
## QUESTION 4:
# l=[11,24,33,2,4,6,97]
# even_numbers=list(filter(lambda x:x%2==0,l))
# print(even_numbers)
# odd_numbers=list(filter(lambda x:x%2!=0,l))
# print(odd_numbers)
## QUESTION 6:
# def factorial(n):
#     return 1 if (n == 1 or n == 0) else n * factorial(n - 1);
# num = 6;
# print("Factorial of", num, "is",factorial(num))
#                                         OR
# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         while (n > 1):
#             fact *= n
#             n -= 1
#         return fact
# num = 6;
# print("Factorial of", num, "is",factorial(num))
## QUESTION 7:
# def checkyear(year):
#     import calendar
#     return (calendar.isleap(year))
# year = 2022
# if(year):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")
## QUESTION 9:
# def intro(**data):
#     print("Data type of argument:",type(data))
#     for key,values in data.items():
#         print("{} is {}".format(key,values))
# intro(first="sindhu",last="yegiteela",age=23,mobile=8332014376)
# intro(First="swapna", Last="chenchu", Email="swapna418@mail.com", Country="india", Age=25, Phone=9949832493)
## QUESTION 10:
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")
## QUESTION 5:
# def mul(l):
#     L=[]
#     for i in l:
#         L.append(i*10)
#     print(L)
# L=list(int(i) for i in input("enter a value:").split(","))
# mul(L)
## 5:list comprehension
# list=(x*10 for x in [2,4,8,9])
# print(list)
## QUESTION 8:
# def abc(*args):
#     for args in args:
#         print(args)
# abc("hello",1,2,3)
## QUESTION 5:
# def func(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(func(3,5,8))
##  *args and **kwargs
# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
# args = ("Geeks", "for", "Geeks")
# myFun(*args)
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)

# def dict_a(a,b):
#     print(locals())
# dict_a(a='sindhu',b='chenchu')
## question 1:
# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end='')
#     print("\r")
# for i in range(rows,0,-1):
#     for j in range(0,i-1):
#         print("*",end='')
#     print("\r")
# x=10
# print(id(x))
# y=20
# print(id(y))
# x=30
# print(id(x))
# x=10
# print(id(x))
# y=20
# print(id(y)
# z=10
# print(id(z))
# # z=50
# print(id(z))
# f=open('abc.txt')
# print(f.read())
## QUESTION 2:
# x=5
# y=0
# try:
#     print(x/y)
# except Exception as e:
#     print(e)
# else:
#     print("else")
# finally:
#     print("Finally method")
##QUESTION 3:
# ZeroDivisionError
# n=int(input("enter n value:"))
# print(n/0)
# NameError
# def func():
#     print(ans)
# func()
# IndexError
# list=[1,3,5]
# print(list[3])
# KeyError
# dict={'a':1,'b':3,'c':5}
# print(dict['d'])
# EOFError
# while True:
#      data = input('Enter name : ')
#      print ('Hello',data)
# AttributeError
# class Attributes(object):
#      pass
# object = Attributes()
# print(object.attribute)
## QUESTION 4:
# class Validate(Exception):
#      pass
# try:
#     age=int(input("Enter your age:"))
#     if age<19:
#         raise Validate
# except Validate as e:
#       print("He is not eligible")
# else:
#     print("He is eligible")
# finally:
#     ("eligible")
## QUESTION 5:
# file = open("file.txt", "r")
# print (file.read(5))
## QSTN 1:
# a ='nikhil'
# a1=[]
# for i in a:
#     s=a.split(" ")
#     a1.append(i)
# for j in a1:
#     print(j)
#      OR
# list=[1,0,1,2,0,1,0,2]
# seggrigate=([x for x in list if x==0] + [x for x in list if x==1]+[x for x in list if x==2])
# print(seggrigate)
## QSTN 2:
# f=open("python.txt","r")
# words=f.read().split()
# x=set(words)
# print(words)
## QSTN 3:
# def decor(func):
#     def inner(age):
#         if age>=18:
#             print("he is eligible")
#         else:
#             func(age)
#     return inner
# @decor
# def vote(age):
#     print("hello,you are not eligible")
# vote(age=int(input("enter a age")))
## QSTN 5:
# def factorial(func):
#     def inner(n):
#         from functools import reduce
#         print(reduce(lambda x,y:x*y,n))
#         func(n)
#     return inner
# @factorial
# def fact(n):
#     print("hello,factorial")
# fact(range(1,8))
## QSTN 6:


# QSTN 1:                                                                SET:5
# s="google.com"
# dict={}
# for i in s:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
# output:{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# QSTN 2:

# QSTN3:
# from functools import reduce
# print(reduce(lambda x,y:x+y,[5,10,15,20]))
# output:
# 50
# QSTN4:
# list=['abc', 'xyz', 'aba', '1221']
# count=0
# for i in list:
#     if len(i)>1 and i[0]==i[-1]:
#         count=count+1
# print("The count is",count)
# output:
# The count is 2
# QSTN5:
# list=['a', 'b', 'c', 'a', 'd', 'e']
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
# output:
# {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
# QSTN6:
# dict={'a':10,'b':2,'c':5,'d':4}
# value=1
# for i in dict.values():
#     value=value*i
# print(value)
# output:
# 400
# QSTN7:
# dict={'a':12,'b':20,'c':50,'d':45}
# x=dict.values()
# max=max(x)
# min=min(x)
# print("maximum number is:",max)
# print("Minimum number is:",min)
# output:
# maximum number is: 50
# Minimum number is: 12
# QSTN8:
# x=int(input("Enter x Value:"))
# y=int(input("Enter y Value:"))
# z=int(input("Enter z Value:"))
# a1 = min(x, y, z)
# a3= max(x, y, z)
# a2 = (x + y + z) - a1 - a3
# print("sorted order is:", a1, a2, a3)
#         (or)
# list=[x,y,z]
# list.sort()
# print(list)
# output:
# Enter x Value:30
# Enter y Value:23
# Enter z Value:10
# sorted order is: 10 23 30
# QSTN9:
# a=int(input("Enter a Value:"))
# b=int(input("Enter b Value:"))
# li=[a,b]
# li[0]=li[1]
# print(li)
# output:
# Enter a Value:25
# Enter b Value:50
# [50, 50]
# QSSTN10:
# def sum(x,y,z=10):
#     sum=x+y+z
#     print("sum of x,y,z is:",sum)
# sum(50,30,5)
# output:
# sum of x,y,z is: 85
# QSTN11:
# def test(*args,**kwargs):
#     print(kwargs)
#     kwargs.update(k3=7)
#     print(kwargs)
#     print(args)
# test(10,20,30,k1=5,k2=6,k3=8)
# output:
# {'k1': 5, 'k2': 6, 'k3': 8}
# {'k1': 5, 'k2': 6, 'k3': 7}
# (10, 20, 30)
# QSTN12,13:
# class Arithmetic:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def addition(self):
#         return self.x+self.y
#     def substraction(self):
#         return self.x-self.y
# class Calculator(Arithmetic):
#     def multiplication(self):
#         return self.x*self.y
#     def moddivision(self):
#         return self.x%self.y
# class FloatDiv(Calculator):
#     def floatdivision(self):
#         return self.x/self.y
# obj=FloatDiv(10,2)
# print("The addition of x,y is:",obj.addition())
# print("The substraction of x,y is:",obj.substraction())
# print("The multiplication of x,y is:",obj.multiplication())
# print("The modular division of x,y is:",obj.moddivision())
# print("The Float division of x,y is:",obj.floatdivision())
# output:
# The addition of x,y is: 12
# The substraction of x,y is: 8
# The multiplication of x,y is: 20
# The modular division of x,y is: 0
# The Float division of x,y is: 5.0
## QSTN 15:
# f=open("test.txt","r")
# e=f.read()
# print(e)
# f.close()
# output:
# Using writemode automatically create test.txt file and insert the data same time.
##QSTN 16:
# with open("python.txt","a",encoding='utf8') as f:
#      f.write("\n Dejan Živković','Gregg Berhalter")
#      f=open("python.txt","r")
# print(f.read())
## QSTN 17:
# f=open("python.txt","w")
# b=f.write("india is my country")
# print(b)
# f.close()
# with open("python.txt","r") as f:
#     print(f.read())
# QSTN 18:
# a=10
# b=0
# try:
#     c=a/b
# except Exception as e:
#     print(e)
# else:
#     print(c)
# finally:
#     print("finally method")
## QSTN 19:
# l=[1,2,3,4,5]
# square=list(map(lambda i:i*i,l))
# print(square)
# l1=[2,3,4,5,6,8,4,7]
# Even_numbers=list(filter(lambda x:x%2==0,l1))
# print(Even_numbers)
# from functools import reduce
# number=reduce(lambda x,y:x+y,[24,35])
# print(number)
###
# f=open("test.txt","r")
# a=f.read(4)
# print(a)
# READ()MODE:
# f=open("test.txt","r")
# a=f.read()
# print(a)
# READLINES()
# f=open("test.txt","r")
# a=f.readlines()
# print(a)
# READLINE()
# f=open("test.txt","r")
# c=f.readline()
# print(c)
## WRITE()
# f=open("test.txt","w")
# a=f.write(" welcome to tweak \n this is file handling")
# print(a)
## WRITABLE()
# f=open("test.txt","w")
# print(f.writable())
##
# f=open("test.txt","r")
# print(f.writable())
##WRITELINES()
# f=open("test.txt","w")
# e=f.writelines("this is python \n this is file handling")
# print(e)
## sorted()
# t=(40,10,30,20)
# t1=sorted(t)
# print(t1)
# print(t)
##RSTRIP():
# x="   abcd   "
# a=x.rstrip()
# print(a)
#   or
# x=" ssahg abcd ,,,. "
# c=x.rstrip()
# print(c)
##LSTRIP():
# c=" ,,...ssdhcdk efgh "
# b=c.lstrip(",..ssdhg")
# print(b)
## CONTEXT MANAGER:
# with open("test2.txt","r")as f:
#     a=f.read()
# print(a)
##
# with open("test2.txt","w") as f:
#     b=f.write("amma")
#     print(b)
## SPLIT():
# with open("test.txt","r")as f:
#     a=f.readlines()
# for i in a:
#     w=i.split()
# print(w)
## STATIC METHOD:
# class Durgamath:
#     @staticmethod
#     def add(x,y):
#         print('the sum:',x+y)
#     @staticmethod
#     def product(x,y):
#         print('the product:',x*y)
#     @staticmethod
#     def average(x,y):
#         print('the average:',x+y/2)
# Durgamath.add(10,20)
# Durgamath.product(10,20)
# Durgamath.average(10,20)
## while loop:
# i=1
# while i<5:
#     print(i)
#     i+=1
##for loop:
# l=[1,2,4,5,7,7]
# sum=0
# for i in l:
#     sum +=i
#     print(i)
#     print(sum)
##break :
# i=1
# while i<5:
#     print(i)
# if i==3:
#     "break"
#     i+=1
##
# l=[1,3,4,6,8,9,3,5,6,8]
# for i in l:
#     if i==9:
#         continue
#     print(i)
## pass:
# for i in range(1,10):
#     if i==5:
#         pass
#     print(i)
##
# try:
#     x=10
#     y=0
#     z=(x/y)
# except Exception as e:
#     print(e)
# else:
#     print(z)
# finally:
#     print("finally method")
##GENERATOR EXPRESSION:
# k=[2,9,4,5,7]
# l=(x**3 for x in k)
# for k in l:
#     print(k)
## REVERSE STRING:
# def reverse(s):
#      str=''
#      for i in s:
#         str=i+str
#      return str
# k='nanna'
# print(reverse (k))
##
# def abc(s):
#     l=''
#     for i in s:
#         l=i+l
#     return l
# k="swapna"
# print(abc(k))
##
# k="python"
# print(k[::-1])
##FACTORIAL
# n=int(input("enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("the factorial",n,"is",fact)
##
# def sum(list):
#     sum=0
#     for i in list:
#         sum=i+sum
#     return sum
# print(sum([2,4,7,8]))
## interview questions:
# l=[1,2,3,4,5]
# #l1=[1,2,3,5]
# l.remove(4)
# print(l)
###
# l=[1,2,3,4,5]
# #l1=[1,2,3,5]
# l.pop(3)
# print(l)
## lambda func()
# k=[2,3,4,5,8,9]
# num=list(map(lambda i:i*i,k))
# print(num)
## convert string:
# s="ketha"
# s1=[]
# for i in s:
#     s.split(",")
#     s1.append(i)
# print(s1)
##
# s=['k','e','t','h','a']
# k=""
# for i in s:
#     k=k+i
# print(k)
##
# s=['k','e','t','h','a']
# k=""
# for i in s:
#     k=i+k
# print(k)
## rotation problem
# l=[1,2,3,4,5,8]
# l1=l*2
# for i in range(0,len(l)):
#     print(l1[i:len(l)+i])
##
# n=8
# list_1 = [1, 2, 3, 4, 5, 6]
# if n > len(list_1):
#     n = int(n % len(list_1))
# list_1 = (list_1[-n:] + list_1[:-n])
# print(list_1)

##
# k="sindhu"
# l=[]
# for i in k:
#     k.split(",")
#     l.append(i)
# for j in l:
#     print(j)
## stack memory:
# def fun():
#     a=20
#     b=[]
#     c=""
## reference counting
# x=10
# y=x
# if id(x)==id(y):
#     print("x and y refer to the same object")
##
# list=[1,2,3,4,5,56]
# list.pop()
# print(list)
##
# c={3,4,6,7,8,9}
# a=c.pop()
# print(c)
##
# k=int(input("enter a value:"))
# fact=1
# i=1
# while i<=k:
#     fact=fact*i
#     i=i+1
# print("factorial",k,"is",fact)
##
# list=[x if x%2==0 else x*100 for x in range(1,10)]
# print(list)
# output:[100, 2, 300, 4, 500, 6, 700, 8, 900]

# list=[x*50 if x%2!=0 else x*100 for x in range(1,10) ]
# print(list)
# output:50, 200, 150, 400, 250, 600, 350, 800, 450]
##
# tuple=(5,6,9,10,3,5,4)
# print(sorted(tuple))
## ENUMERATE
# k=tuple(enumerate([1,2,3,4]))
# print(k)
##pop()
# l=[2,4,6,8,6,5,3,2]
# l.pop()
# print(l)
##
# l=[3,5,8,9,4,6,12,98]
# x=l.pop()
# print(x)
# list=[1,2,3,4,56]
# print(enumerate(list))
# a=[1,2,3,4,6]
# b=enumerate(a)
# print(a,3,2)
# #
# k=[3,5,7,9,2]
# b=enumerate(k)
# print(k,2)
##
# g="sindhu yegiteela"
# print(g[-8:-6])
##
# f=open("python.txt","w")
# for i in range(10):
#     f.write("this is python %d\r\n"%(i+1))
# f.close()
# def func(s):
#     str=''
#     for i in s:
#         str=i+str
#     return str
# s="python"
# print(func(s))
# num=int(input("enter a value"))
# fact=2
# for i in range(1,num+1):
#     fact=fact*i
# print("factorial of",num,"is",fact)
# def sum_list(items):
#     sum=0
#     for i in items:
#         sum=sum+i
#     return sum
# print(sum_list([1,2,3,4,5]))
# f=open("tweak.txt","w")
# f.write("this is file")
# print(e)
# f.close()

# f=open("tweak.txt","r")
# f.read()
# print(e)
# f.close()

# f=open("tweak.txt","w")
# f.write("this is python")
# #print(e)
# f.close()

# f=open("tweak.txt","r")
# print(f.tell())

# f=open("test2.txt","r")
# f.read()
# f.close()
# f=open("tweak.txt","r")
# if f.mode=="r":
#      e=f.read()
# print(e)
# f.close()
# print(e)
# f=open("test.txt","r")
# e=f.read()
# print(e)
# f.close()
##
# f=open("tweak.txt","a")
# f.write("my mom\n")
# f.close()
##
# f=open("test.txt","w+")
# for i in range(10):
#     f.write("this is line %d\r\n" % (i+1))
# f.close()
##
# def func(s):
#     str=''
#     for i in s:
#         str=i+str
#     return str
# s="sindhu"
# print(func(s))
# try:
#     f=open("tweak.txt",encoding='utf-8')
# finally:
#     f.close()
##
# with open("tweak.txt",encoding="utf-8")as f:
#     f.close()
# ## swapping case:
# x=int(input("enter a value:"))
# y=int(input("enter a  value:"))
# z=x
# x=y
# y=z
# print("the value of x after swapping:x",x)
# print("the value of y after swapping:y",y)
# even or odd numbers:
# def odd_num(l):
#     l1=[]
#     for i in l:
#         if i%2!=0:
#             l1.append(i)
#     return l1
# a=even_num([1,4,5,6,9,8,7])
# print(a)
# b= odd_num([1,3,4,6,7,9])
# print(b)
##
# f=open("python.txt","w+")
# f.readlines()
# for x in f:
#     print(x)
# f.close()
# REGULAR EXPRESSIONS:
# 1.Findall():
# import re
# txt="the rain in spain"
# x=re.findall("ai",txt)
# print(x)
##
# import re
# num="this is python module"
# z=re.findall("the",num)
# print(z)
##
# 2.search():
# import re
# text='india'
# k=re.search(text,"india is a my country")
# print(k.start(),k.end())
##
# s="sindhu"
# s="gayatri"
# print(s)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1= person("swapna",24)
# print(s1.name)
# print(s1.age)
##create object
# class sindhu:
#     s=5
# s1=sindhu()
# print(s1.s)
##
# import json
# a={"name":"sindhu","age":24,"salary":50000}
# b=json.dumps(a)
# print(b)
##
# import json
# print(json.dumps(("welcome","to","geeks")))
# print(json.dumps((12345)))
# print(json.dumps((123.456)))
# print(json.dumps((True)))
# print(json.dumps((False)))
# print(json.dumps((None)))
# def reverse(s):
#     str=""
#     for i in s:
#         str=i+str
#     return str
# s="sindu"
# print(reverse(s))
##
# def sum(list):
#     sum=0
#     for i in list:
#         sum=sum+i
#     return sum
# print(sum([1,2,3,45]))
##
# l=[1,2,3,4,5]
# for i in range(0,5):
#     print(i)
# NORMAL REVERSE STRING:
# s="sindhu"
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)
##
# S="SINDHU"
# S[0]="R"
# PRINT(S)
## for loop in sum:
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum = 0
# for val in numbers:
#     sum = sum+val
# print("The sum is", sum)
##read()
# f=open("tweak.txt","r+")
# print(f.read(4))
# f.close()
##readlines():
# f=open("tweak.txt","r+")
# print(f.readlines(4))
# f.close()
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def age(self):
#         return self.age
# f=student("sindhu",24)
# print(f.name)
# print(f.age)
# import pandas as pd
# df = pd.DataFrame()
# print(df)
# lst = ['Geeks', 'For', 'Geeks', 'is',
#        'portal', 'for', 'Geeks']
# df = pd.DataFrame(lst)
# print(df)
# from main1 import sales
# print(sales)
##
# num = float(input("Enter a number: "))
# if num > 0:
#    print("Positive number")
# elif num == 0:
#    print("Zero")
# else:
#    print("Negative number")
# py_string = 'Python'
# print(sorted(py_string))
# l=[1,2,3,4,5]
# l1=sorted(l)
# print(l1)
# print(l)
# t=(40,30,20,10)
# t1=sorted(t)
# print(t1)
# print(t)
# mylist = [5, 4, 3, 2, 1]
# s=sorted(mylist)
# print(s)
## count and repeated in list
# l=['a','b','c','a','b','a']
# l1={} #empty dict
# for i in l:
#     l1[i]=l.count(i)
# print(l1)
## prime numbers:
# n1=int(input("enter a value"))
# n2=int(input("enter a value"))
# for number in range(n1,n2+1):
#     if number>1:
#         for i in range(2,number):
#             if(number%i)==0:
#                 break
#         else:
#             print(number)
##
# num=int(input("enter a number:"))
# f=0
# x,y=0,1
# while y<=50:
#    print(y)
#    x,y=y,x+y

# y=sum
# sum=x+y
# def Fibonacci(n):
#     if n<0:
#         print("incorrect input")
#     elif n==0:
#         return 0
#     elif n==0 and n==1:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# print(Fibonacci(9))
#
#
# n=int(input("enter a number:"))
# a,b=0,1
# sum=0
# count=1
# print(" fibonacci series:", end=" ")
# while (count<= n):
#     print(sum,end=" ")
#     count += 1
#     a=b
#     b=sum
#     sum=a+b
##
# l=[1,2,3,4,5,6,7,8,100]
# for i in range(0,99):
#    print(i)
##
# n=int(input("enter a value"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end = " ")
#     print()
##DECORATOR WITH SQUARE :
# def smart_dive(func):
#     def sumofsquares(a,b):
#         return func(5**2,6**2)
#     return sumofsquares
# @smart_dive
# def add(a,b):
#     c=a+b
#     return c
# c=add(5,6)
# print("sum of two values=",c)
# DECORATOR WITH SUM :
# def decorateFun(add):
#     def sum(a,b):
#         return add(5,6)
#     return sum
# @decorateFun
# def add(a,b):
#     c=a+b
#     return c
# c=add(5,6)
# print("addition of two values=",c)
##GENERATORS:
# def generatorfunc():
#     yield 1
#     yield 2
#     yield 3
# for value in generatorfunc():
#     print(value)
## PRIME NUMBERS IN ASCENDING ORDER:
# x=[3,8,5,1,13]
# for i in range(len(x)-1):
#     for j in range(len(x)-1):
#         if x[j]>x[j+1]:
#             y=x[j]
#             x[j]=x[j+1]
#             x[j+1]=y
# print(x)
# f=open("file.text","r")
# s1=f.read(3)
# s2=f.read(2)
# s3=f.read()
# print(s1)
# print(s2)
# print(s3)
# f=open("file.text","r")
# d=f.readlines()
# print(d)
#
# f=open("file.text","r")
# s=f.readline()
# print(s)
# #
# f=open("file.text","w")
# l=[]
# for i in range(3):
#     name=input("enter a name:")
#     l.append(name+'\n')
# f.writelines(l)
# f.close()
# with open("file.text",encoding="utf-8")as f:
#     s=f.read(4)
#     print(s)
##
# import csv
# with open('start.csv', 'w') as csvfile:
#     startwriter = csv.writer(csvfile, delimiter=' ',
#     quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     startwriter.writerow(['Start'] * 2 + ['working example of csv write'])
#     startwriter.writerow(['starting', 'this is an example', 'just a simple working example'])
# ##
# import csv
# with open('start.csv', 'w') as csvfile:
#     startwriter = csv.writer(csvfile)
#     startwriter.writerow(['Start'] * 2 + ['working example of csv write'])
#     startwriter.writerow(['starting', 'this is an example', 'just a simple working example'])
##
# import csv
# newdict=[{'branch': 'ME', 'cgpa': '9.4', 'student_name': 'Sulaksh', 'year': '2'},
# {'branch': 'COE', 'cgpa': '8.9', 'student_name': 'Amit', 'year': '2'},
# {'branch': 'IF', 'cgpa': '8.3', 'student_name': 'Rutuja', 'year': '2'},
# {'branch': 'IM', 'cgpa': '7.1', 'student_name': 'Madhu', 'year': '2'}]
# print(type(newdict))
# fields = ['student_name', 'branch', 'year', 'cgpa']
# #filename = "uni_records.csv"
# with open("uni_records.csv", 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = fields)
#     writer.writeheader()
#     writer.writerows(newdict)
##
# m1=open("file.text","r")

# m2=open("file_B.text","w")
# str=""
# while str:
#     str=m1.readline()
#     m2.write(str)
# m1.close()
# m2.close()
##
# f=open("test.txt","w")
# s=f.writelines("india is a my country")
# print(s)
##
# f = open("test.txt","w+")
# iter_seq = ["This is good platform\n", "Datascience is buzzword"]
# line = f.writelines( iter_seq )
# #print(line)
# f.close()
##
# f=open("file.text","w")
# items=["this is filehandling\n","worlds mom bestiee"]
# line=f.writelines(items)
##
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def age(self):
#         return self.age
# f=student("swapna",25)
# print(f.name)
# print(f.age)
## MULTIPLE INHERITANCE:
# class read:
#     read=""
#     def read(self):
#         print(self.read)
# class write:
#     write=""
#     def write(self):
#         print(self.write)
# class books(read,write):
#     def study(self):
#         print("read:",self.read)
#         print("write:",self.write)
# s=books()
# s.read="sis"
# s.write="son"
# s.study()
##MULTILEVEL INHERITANCE:
#
# class grandfather:
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
#
# class father(grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         grandfather.__init__(self, grandfathername)
#
# class son(father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         father.__init__(self, fathername, grandfathername)
#
#     def print_name(self):
#         print("grandfather name:", self.grandfathername)
#         print("father name:", self.fathername)
#         print("son name:", self.sonname)
#
# s1 = son("chitty", "dad", "thathaiah")
# print(s1.grandfathername)
# s1.print_name()
##
# def decor(func):
#     def inner(s):
#         if s>=18:
#             print("eligible to vote")
#         else:
#             print("it is not eligible")
#     return inner
# @decor
# def vote(age):
#     print("vote is eligible")
# s=vote(int(input("enter a age value")))
##
# f=open("file.text","r+")
# f.write("this is file")
## WITHOUT DECORATOR:
# def decor(func):
#      def inner(a):
#          if a>=18:
#              print("eligible to vote")
#          else:
#              print("it is not eligible")
#      return inner
# def vote(age):
#      pass
# a=decor(vote)
# a(20)
# l=[1,2,3,4,5,6]
# count=0
# for i in l:
#     count=count+i
# print(count)
##
# l=[1,2,3,4,5,6]
# count=1
# for i in l:
#      count=count*i
# print(count)
# # generators:
# def even():
#      for i in range(10):
#          if (i % 2 == 0):
#              yield i
# for i in even():
#     print(i)
##
# def multiple_stringyield():
#     str1="sindhu"
#     yield str1
#     str2="swapna"
#     yield str2
#     str3="nithi"
#     yield str3
# obj=multiple_stringyield()
# print(next(obj))
# print(next(obj))
# print(next(obj))
##
# def func1():
#     for i in range (10):
#         yield i
# a=func1()
# #print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# for i in a:
#     print(i)
##
# def func1():
#     for i in range (10):
#         yield i
# a=func1()
# print(a)
# for i in a:
#     print(i)

##
# import sys
# def func():
#     l=[]
#     for i in range(10):
#         yield i
# a=func()
# print(sys.getsizeof(a))
# for i in a:
#      print(a)
#      break
# for i in a:
#     print(a)
##
# l=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# def evenno(fun):
#     def inner(l):
#         for i in l:
#             if(i%2==0):
#                 print("even numbers")
#             else:
#                 print('odd numbers')
#     return inner
# @evenno
# def even(l):
#     #print("even or odd numbers")
#     pass
# l=[1,2,3,4,5,6,7,8,9,10]
# print(evenno(l))
#num=int(input("enter a values:"))
# l=[10,20,30,40,37,45,55,67,88]
# def even(a):
#     s=[]
#     for i in a:
#         if i%2==0:
#             s.append(i)
#     return s
# print(even(l))
##
# number=int(input("enter any number is even or odd"))
# if(number%2)==0:
#     print("the number is even")
# else:
#     print("the number is odd")
##
## COVERT LIST TO STRING:
# def func(s):
#     str=""
#     for i in s:
#         str+=i
#     return str
# s=["sindhu","gayathri","honey"]
# #print(s)
# print(func(s))
##
# def func(s):
#     str=""
#     for i in s:
#         str+=i
#     return (''.join(s))
# s=["sindhu","gayathri","honey"]
# #print(s)
# print(func(s))
##
# s=["college","school","sports","study"]
# print(s)
# list=''.join([str(i) for i in s])
# print(list)

##NESTED LIST TO LIST:

# l = [[1],[2,3,4,5],[9]]
# k = []
# for sublist in l:
#     for item in sublist:
#         k.append(item)
# print(k)
#       OR ANOTHER
##
# from functools import reduce
# l = [[14], [215, 383, 87], [298], [374], [2,3,4,5,6,7]]
# k= reduce(lambda x,y: x+y, l)
# print(k)
##
# l=[1,2,3,[4,5,6],7,8,[1,2,3],[10]]
# c=[]
# def reemovnestings(l):
#         for i in l:
#             if type(i)==list:
#                 reemovnestings(i)
#             else:
#                 c.append(i)
# print ('The original list: ', l)
# reemovnestings(l)
# print("the list after removing nesting:",c)
##map()
# l=[1,2,3,4,5]
# k=list(map(lambda i:i*i,[1,2,3,4,5]))
# print(k)
# #
# k=set(map(lambda i:i*i,[2,3,5,6,8]))
# print(k)
##
# l=[2,3,4,56,7,9,6,12,15]
# b=list(filter(lambda i:i%2==0,l))
# print(b)
##
# tables = [lambda x=x: x * 10 for x in range(1, 11)]
# for table in tables:
#     print(table())
## EXCEPTIONS:
# try:
#     a=10
#     b=0
#     c=((a+b)/(a-b))
# except ZeroDivisionError:
#     print("a/b result in 0")
# else:
#     print(c)
# finally:
#     print("finally method")
##
# def func(k,l):
#     try:
#         m=(k+l)/(k-l)
#     except ZeroDivisionError:
#         print("k/l result in 0")
#     else:
#         print(m)
#     finally:
#         print("finally method")
# func(3,4)
# func(4,4)
##
# try:
#     a = int(input("enter a value"))
#     b = int(input("enter a value"))
#     c = a / b
# except Exception:
#     print("can't be divide by zero")
# else:
#     print(c)
# finally:
#     print("finally method")
##
# try:
#     a=int(input("enter a value"))
#     b=int(input("enter a value"))
#     c=a/b
#     print(c)
# finally:
#     print("finally")
##
# l=[[1],[2],[3],[4]]
# k=[]
# for i in l:
#     k.extend(i)
# print(k)
##
# l=[1,2,3,4,5,6]
# # l.remove(4)
# # print(l)
# l.pop(3)
# print(l)

# l=[1,2,3,4,5,6,7,8,9]
# k=[]
# for i in range(len(l)):
#     if i%2!=0:
#         k.append(i)
# print(k)
##
# l=[1,2,3,4,5,6,7,8]
# l.pop(4)
# print(l)
##
# l=[1,2,3,4,5,6,7,8]
# for i in range(0,len(l)-1,2):
#     if i<len(l) or i==len(l)-1:
#         l.remove(l[i])
#     else:
#         break
# print(l)
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)-1,0,-2):
#     l.remove(l[i])
# print(l)
#l=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)-1,0,-2):
#     l.remove(l[i])
# print(l)
# d={"s":1,"i":2,"n":3,"d":4,"u":5}
# print(d)
# print(d.values())
# print(d.get("d"))
# print(d.items())
# l=[1,2,3,4,1,2,3,4]
# d={}
# for i in l:
#     d[i]=l.count(i)
# print(d)
# l=[10,20,30]
# #print(l)
# l.append(50)
# l.append([60,70])
# print(l)
# l.extend([50,40])
# print(l)
# s="sindhu"
# str=""
# for i in s:
#     str=i+str
# print(str)
##
# l=[1,2,3,4,5,6,7,8,9]
# #print("the list is:")
# #print(l)
# for i in range(0,len(l),2):
#     print(l[i])
##
# import pandas
# data={
#     'cars':["volvo","bmw","breeza"],
#     'passings':[1,6,3]
# }
# items=pandas.DataFrame(data)
# print(items)
##
# import pandas as pd
# data={
#     "calory":[420,400,380],
#     "duration":[40,50,45]
# }
# num=pd.DataFrame(data)
# print(num)
## tuple() unpacking
# a=(10,20,30)
# c,d,e=a
# print(d)
##
# a=[10,[20,30],[40,[50,[60],10]]]
# print(a[2][1][0])
##
# l=[1,2,3,4,1,2,3,4]
# d={}
# for i in l:
#     d[i]=l.count(i)
# print(d)
##list compreh():
# l=[1,2,3,4,5,6,7,8,9]
# k=[x for x in l if x%2==0]
# print(k)
##
# l=[1,2,3,4,5,6,7,8,9]
# k=[1,2,3,4,5,6,7,8,9]
# d={(i,j) for i,j in zip(l,k)}
# print(d)
##
# l=[1,2,3,4,5,6,7,8,9]
# k=[1,2,3,4,5,6,7,8,9]
# d={i:j for (i,j) in zip(l,k)}
# print(d)
##polymorphism:
# def add(a, b):
#     return a + b
#
# def add(a, b, c):
#     return a + b + c
# print(add(2, 3,5))
##pop():
# l=[1,2,3,4,6]
# l.pop()
# print(l)
## Method overloading:
# def product(a, b):
#     p = a * b
#     print(p)
# def product(a, b, c):
#     p = a * b * c
#     print(p)
# product(4, 5, 5)
## Method overriding:
# class parent():
#     def show(self):
#         print("inside parent")
#
# class child(parent):
#     def show(self):
#         parent.show(self)
#         print("inside child")
# obj=child()
# obj.show()
## single inheritance:
# class parent:
#     def func1(self):
#         print("parent")
# class child(parent):
#     def func2(self):
#         print("child")
# obj=child()
# obj.func1()
# obj.func2()
##Multiple inheritance:
# class func1:
#     func1=""
#     def func1(self):
#         print(self.func1)
# class func2:
#     func2=""
#     def func2(self):
#         print(self.func2)
# class func3(func1,func2):
#     def func4(self):
#         print("func1:",self.func1)
#         print("func2:",self.func2)
#
# s=func3()
# s.func1="sindhu"
# s.func2="swapna"
# s.func4()
## Multilevel inheritance:
# class parent1():
#     def func1(self):
#         print("this is function1 class")
# class parent2(parent1):
#     def func2(self):
#         print(" this is function 2 class")
# class parent(parent2):
#     def func3(self):
#         print("this is function class")
# obj=parent()
# obj.func1()
# obj.func2()
## Hierarchical inheritance:

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()
# a=[1,2,3,4,5,6]
# for i in a:
#     pass
# a=[1,2,3,4,5,6]
# for i in a:
#     if i==5:
#         break
#     if i==4:
#         continue
# print(i,end=" ")
# ##sort()
# l=[9,2,4,6,5,2,1,8]
# l.sort()
# print(l)
## sorted()
# l=(9,2,4,6,5,2,1,8)
# s=sorted(l)
# print(l)
# print(s)
##
# class parent:
#     def func1(self):
#         print("this is parent class")
# class child(parent):
#     def func2(self):
#         print("this is child class")
# obj=child()
# obj.func1()
# obj.func2()
##
# class read:
#     read=""
#     def read(self):
#         print(self.read)
# class write:
#     write=""
#     def write(self):
#         print(self.write)
# class books(read,write):
#     def study(self):
#         print("read:",self.read)
#         print("write:",self.write)
# s=books()
# s.read ="sindhu"
# s.write ="swapna"
# s.study()
##
# class parent1:
#     def func1(self):
#         print("parent1")
# class parent2(parent1):
#     def func2(self):
#         print("parent2")
# class parent(parent2):
#     def func3(self):
#         print("parent class")
# ob=parent()
# ob.func1()
# ob.func2()
##
# class child1:
#     def func1(self):
#         print("this is child class1")
# class child2(child1):
#     def func2(self):
#         print("this is child class2")
# class child(child1):
#     def func3(self):
#         print("this is child class")
# b1=child()
# b2=child2()
# b1.func1()
# b1.func3()
# b2.func1()
# b2.func2()
##
# l=int(input("enter avalue"))
# if l%2==0:
#     print("even numbers")
# else:
#     print("odd numbers")
##
# l=[1,2,3,4,5,6,6,7,8,9]
# k=[]
# def even(l):
#     for i in l:
#         if i%2==0:
#             k.append(i)
#     return k
# print(even(l))
##split()
# string="this is python"
# string1=string.split()
# print(string1)
##join()
# string="this","is", "python"
# str1=''.join(string)
# print(str1)
##

# def set_list(list):
#     list = ["A", "B", "C"]
#     return list
# def add(list):
#     list.append("D")
#     return list
# my_list = ["E"]
#
# print(set_list(my_list))
#
# print(add(my_list))
##MCQ
# list1=[3,4,5,2,1,0]
# list1.pop(1)
# print(list1)
##
# d="hello world"
# print(d[::-1])
##
# myList = [lambda x: x ** 2,
#          lambda x: x ** 3,
#          lambda x: x ** 4]
#
# for f in myList:
#     print(f(3))
# r = ['s', 'r', 'a', 's']
# s = ['a', 'a', 'n', 'h']
# k=["".join([i, j]) for i, j in zip(r,s)]
# print(k)


# class A(object):
#     def __init__(self, a):
#         self.num = a
#
#     def mul_two(self):
#         self.num *= 2
# class B(A):
#     def __init__(self, a):
#         A.__init__(self, a)
#
#     def mul_three(self):
#         self.num *= 3
#
#
# obj = B(4)
# print(obj.num)
#
# obj.mul_two()
# print(obj.num)
#
# obj.mul_three()
# print(obj.num)
##
# class Human(object):
#     def __init__(self, name):
#         self.human_name = name
#
#     def getHumanName(self):
#         return self.human_name
#
#     def isEmployee(self):
#         return False
# class IBEmployee(Human):
#     def __init__(self, name, emp_id):
#         super(IBEmployee, self).__init__(name)
#         self.emp_id = emp_id
#
#     def isEmployee(self):
#         return True
#
#     def get_emp_id(self):
#         return self.emp_id
# employee = IBEmployee("Mr Employee", "IB007")
# print(employee.getHumanName())
# print(employee.isEmployee())
# print(employee.get_emp_id())
# class X:
#     def __init__(self):
#         self.__num1 = 5
#         self.num2 = 2
#
#     def display_values(self):
#         print(self.__num1, self.num2)
# class Y(X):
#     def __init__(self):
#         super().__init__()
#         self.__num1 = 1
#         self.num2 = 6
# obj = Y()
# obj.display_values()
##
# main_dict={}
# def insert_item(item):
#    if item in main_dict:
#        main_dict[item] += 1
#    else:
#        main_dict[item] = 1
# #Driver code
# insert_item('Key1')
# insert_item('Key2')
# insert_item('Key2')
# insert_item('Key3')
# insert_item('Key1')
# print (len(main_dict))
##
# def deco(fun):
# 		def inner(x,y):
# 			if type(x) or type(y)==str:
# 				print('we cant do addition')
# 			else:
# 				print(x+y)
#           m=fun()
#                 return m
# 		  return inner
##
# class A:
#     def display(self):
#         print('i am from class A')
# class B:
#     def display(self):
#         print('i am from class B')
# class c(A, B):
#     def __init__(self):
#         print('i am from class C constructor')
# obj = c()
# obj.display()
##
# def palindrome(s):
#     return s==s[::-1]
# s="radar"
# abc=palindrome(s)
# if abc:
#     print("yes")
# else:
#     print("no")
#
# a=[10,20,30,20,10,50,60,40,80,50,40]
# dup_items=set()
# unique_items=[]
# for i in a:
#     if i not in dup_items:
#         unique_items.append(i)
#         dup_items.add(i)
#     print(dup_items)
##
# n=int(input("enter a value"))
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#         i+=1
#     return fact
# print(fact(n))
# l=[1,2,3,4,4,3,2,4,5,7,9]
# k=[]
# for i in l:
#     if i not in  k:
#         k.append(i)
# l=k
# print("list after removing duplicate values ",l)
##
# l=[1,2,3,4,4,3,2,4,5,7,9]
# k=set(l)
# print(list(k))
##
# l=[1,2,3,4,4,3,2,4,5,7,9]
# print(l[::-1])
##
# l=[1,2,3,4,5,6]
# print(l[-1])
##REMOVE DUPLICATE VALUES:
# l=[1,2,3,4,5,3,2,4,5,6,7,8,5,4,3]
# k=[]
# for i in l:
#     if i not in k:
#         k.append(i)
# l=k
# print("after removing a duplicate values:",l)
##
# str="sindhu"
# str1=""
# for i in str:
#     str1=i+str1
# print(str1)
##
# l=[1,2,3,4,5,6]
# k=[]
# for i in l:
#     if i%2==0:
#         k.append(i)
# print(k)
##
##
# l=['s','i','n','d','u']
# k=""
# for i in l:
#     k=k+i
# print(k)
##
# s="sindhu"
# s1=[]
# for i in s:
#     s.split(",")
#     s1.append(i)
# print(s1)
##
# assert sum([2,3,5])==10
# print("it is correct")

# def test_sum():
#     assert sum([2, 3, 5]) == 10, "It should be 10"
# if __name__ == "__main__":
#     test_sum()
#     print("Everything passed")
##
# def test_sum():
#     assert sum([2,3,5])==10
# def test_sum_tuple():
#     assert sum((1,3,5))
# if__name__="__main__"
# test_sum()
# test_sum_tuple()
# print("everything is correct")
##
# import random
# for i in range(5):
#     a=random.randint(1,10)
#     print(a)
##
# l=[1,2,3,4,5]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
##
# str1 = "w3resource"
# for index, char in enumerate(str1):
#     print("Current character", char, "position at", index )
# str1 = 'vamsee'
# print("Original String is", str1)
# res = str1[0]
# l = len(str1)
# mi = int(l / 4)
# res = res + str1[mi]
# res = res + str1[l-1]
# print("New String:", res)
##
# sample_str = "P@yn2at&#i5ve"
# def find_digits_chars_symbols(sample_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0
#     for char in sample_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         # if it is not letter or digit then it is special symbol
#         else:
#             symbol_count += 1
#
#     print("Chars =", char_count)
#
# sample_str = "P@yn2at&#i5ve"
# print("total counts of chars, Digits, and symbols \n")
# find_digits_chars_symbols(sample_str)
##
# str="sindhu"
# str1=""
# for i in str:
#     str1=i+str1
# print(str1)
##
# from math import*
# print(sqrt(4))
##
# import random
# for i in range(5):
#     a=random.randint(1,10)
#     print(a)
# #
# l=[10,20,30,40,50,60,70,80]
# sum=0
# for i in l:
#     sum=i+sum
#     print(i)
#     print(sum)
##
# a="hello world"
# s=a.endswith("hello")
# print(s)
##
# Python program to illustrate destructor
# class Employee:
#
#     # Initializing
#     def __init__(self):
#         print('Employee created.')
#
#     # Deleting (Calling destructor)
#     def __del__(self):
#         print('Destructor called, Employee deleted.')
# obj = Employee()
# del obj
##SPLIT():
# str="this is programming language"
# str1=str.split()
# print(str1)
##JOIN():
# str='this', 'is', 'programming', 'language'
# str1=''.join(str)
# print(str1)
##LIST COMPREH():
# l=[1,2,3,4,5,6,7]
# l1=[x**2 for x in l]
# print(l1)
##DICT COMPREH():
# l=[1,2,3,4,5,6,7,8]
# k={x:x**2 for x in l}
# print(k)
## ZIP():
# l=('sindhu','swapna','nithi')
# k=('neeru','vamsee','bharu')
# m=zip(l,k)
# print(tuple(m))
##zip():
# l=[1,2,3,4,5,6]
# x=zip(l)
# print(list(x))
# ##
# l=[2,3,4,5,6,8,9]
# k=zip(l)
# print(tuple(k))
##
# l=[3,8,1,4]
# l.sort()
# print(l)
##
# l=[3,8,1,4]
# print(sorted(l))
# print(l)
##
# n=int(input("enter a value:"))
# a,b=0,1
# sum=0
# count=1
# print("fibonacci series:",end="")
# while(count<=n):
#   print(sum,end="")
#   count+=1
#   a=b
#   b=sum
#   sum=a+b
##
# N = int(input("Number of elements in Fibonacci Series, N, (N>=2) : "))
#
# #initialize the list with starting elements: 0, 1
# fibonacciSeries = [0,1]
#
# if N>2:
# 	for i in range(2, N):
# 		#next elment in series = sum of its previous two numbers
# 		nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
# 		#append the element to the series
# 		fibonacciSeries.append(nextElement)
#
# print(fibonacciSeries)
##
# import random
# for i in range(5):
#     a=random.randint(1,10)
# print(a)
##
# str="sindhu"
# str1=""
# for i in str:
#     str1=i+str1
# print(str1)
# def reverse(str):
#     str1=""
#     for i in str:
#         str1=i+str1
#     return str1
# str="sindhu"
# print(reverse(str))
# #str="sindhu"
## 1 TO 100
# for i in range(1,99):
#     print(i)
##
# for i in range(1,50):
#     print(i)
##
# l=[1,2,3,4,5,3,4,2,4,5,2,3,5,7,7,8,8,4,3,5]
# k=[]
# for i in l:
#     if i not in k:
#         k.append(i)
# l=k
# print("to remove the duplicate values from list",l)
##
# l=[1,2,3,4,5,3,4,2,4,5,2,3,5,7,7,8,8,4,3,5]
# k=set(l)
# print(list(k))
##
# l="vamseee"
# k=set(l)
# print(list(k))
##
# str="this is program"
# str1=str.split()
# print(str1)


# k=[[1,2,3], [1,2], [2,3], [1,2,3], [2,3], [1,2,3,4]]
# unique = []

# original_list=[71, 36, 51, 75, 82, 78, 40]
# print('Orginal List:', original_list)
# reversed_list=[]
# for i in original_list:
#     reversed_list.insert(0,i)
# print('Reversed List:', reversed_list)
##REVERSE IN LIST:
# l=[1,2,3,4,5,6]
# k=[]
# for i in l:
#     k.insert(0,i)
# print(k)
##
#l=[1,2,3,4,5,6]
# #k=l.append(8)
# #l.extend([7,8,9])
#l.insert(4,[6,7,8])
# #l[4]=65
#print(l)
##
# s="sindhu"
# print('s[3:5]=',s[3:5])
#
# l=[1,2,3,4,5,6,7,8,9]
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append("even")
#     if i%2!=0:
#         l1.append("odd")
# print(l1)
# l=[20,2,3,24,22,34,45,12,12,33,24]
# def even(a):
#     b=[]
#     for i in a:
#         if i%2==0:
#             b.append(i)
#     return b
# print(even(l))
##
# l=[10,20,30,40,50]
# a=0
# b=0
# for i in l:
#     if i>a:
#         a=i
# print(a)
# for j in l:
#     if j>b and j!=a:
#         b=j
# print(b)
##
# s="this is python"
# k=s.replace("python","language")
# print(k)
##
# s="happy new year"
# k=s.split()
# s1=""
# for i in k:
#     s1=i+s1
# print(s1)
##REVERSE NO:
# n=3456
# rev=0
# while n>0:
#     a=n%10
#     rev=rev*10+a
#     n=n//10
# print(rev)
# s="happy new year"
# s1=s.split()
# k=""
# for i in s1:
#     k=i+k
# print(k)
##
# s="sindhusha"
# s1={}
# for i in s:
#     s1[i]=s.count(i)
# print(s1)
##
# l=[1,2,3,4,5,6,7,5,4,3,2,3,4,1,6,7]
# k=[]
# for i in l:
#     if i not in k:
#         k.append(i)
# l=k
# print(k)
##
# l = [1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 3, 4, 1, 6, 7]
# k=set(l)
# print(list(k))
#
# l=[1,2,3,4,5,6]
# even_list=[]
# for i in l:
#     if i%2==0:
#         even_list.append(i*i)
#     else:
#         even_list.append(i*i*i)
# print(even_list)
##
# l=[1,2,3,4,5,6]
# even_list=[]
# odd_list=[]
# for i in l:
#     if i%2==0:
#         even_list.append(i*i)
#     else:
#         odd_list.append(i*i*i)
# print(even_list)
# print(odd_list)
## REVERSE OF LIST:
# l=[1,2,3,4,5,6,6,5]
# h=[]
# for i in l:
#     h.insert(0,i)
# print(h)
##
# k=[[1,2,3],[2,3,4],[4,5,6,7]]
# for i in k:
#     print(i)
##
# l=[1,2,3,4,5]
# x=zip(l)
# print(list(x))
#print(l)
##
# l=[1,2,3,4,5,6,4,3,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
##
# s="sindhusha"
# s1={}
# for i in s:
#     if i not in s1:
#         s1[i]=1
#     else:
#         s1[i]+=1
# print(s1)
##
# n=int(input("enter a value"))
# def fact(n):
#     fact=1
#     i=1
#     while i<=n:
#         fact=fact*i
#         i+=1
#     return fact
# print(fact(n))
##
# n=int(input("enter a value"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     i+=1
# print(fact)
##
# l="there is a shop in hyderabad"
# l1={}
# for i in l:
#     l1[i]=l.count(i)
# print(l1)
##
# l="my name is sindu"
# even=""
# l2=l.split()
# for i in l2:
#     even=i+even
# print(even)
# ##
# l= 'my name is sindu'
# l1=l.split(" ")
# k=[]
# for i in range (0,len(l1)):
#     if i%2==0:
#         k.append((l1[i][::-1]))
#     else:
#         k.append(l1[i])
# print(" ".join(k))

# s="sindhu"
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)

# import datetime
# from time import gmtime,strftime
# print(strftime(" %H:%m:%S ",gmtime()))
##
# def checkprime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return 1
# n=int(input("enter a value"))
# p=checkprime(n)
# if p==1:
#     print("not prime")
# else:
#     print("prime")
##
# n=1234
# rev=0
# while n>0:
#     a=n%10
#     rev=rev*10+a
#     n=n//10
#     if(rev%2==0):
#         print(rev)
#     rev=0
##
# l=[1,2,3,4]
# for i,j in enumerate(l) :
#     if i%2==0:
#         print(i)
#
l='1234'
#even=[]
#odd=[]
# for i in range (len(l)):
#     if i%2==0:
#         even.append(i)
#     #else:
#         #pass
# print(even)
#

# i=[1,2,3,4,5]
# j=['a','b','c','d','e']
# for i,j in zip(i,j):
#     print(i,j)
# d={'name':1,'branch':2,'address':3}
# d.popitem()
# print(d)
##
# import copy
# list1=[[1,2,3],[4,5,6]]
# list2=copy.copy(list1)
# list1.append([7,8,9])
# print("old_list:",list1)
# print("new_list:",list2)

##
# import copy
# list=[[1,2,3],[4,5,6],[7,8,9]]
# list1=copy.deepcopy(list)
# list[1][2]="abc"
# print("old_list:",list)
# print("new_list:",list1)
##
# def reverse(s):
#     return s=s[::-1]
#import palindrome
##
# def reverse(s):
#     return s==s[::-1]
# s="amma"
# pwd=reverse(s)
# if pwd:
#     print("palindome")
# else:
#     print("palindrome or not")
##
# l=[1,2,3,4,5,6]
# even=[]
# for i in l:
#     if i%2==0:
#         even.append(i*i)
#     else:
#         even.append(i*i*i)
# print(even)
##
# l=[1,2,3,4,5,6]
# list=[x for x in l if x%2==0]
# print(list)
#
# # CHECK WHETHER PRIME OR NOT:
# def checkprime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return 1
# n=int(input("enter a value"))
# p=checkprime(n)
# if p==1:
#     print("prime")
# else:
#     print("not prime")
##
# l=[1,2,3,4,5,6,7,8,9,10]
# #
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append("True")
#     if i%2!=0:
#         l1.append("False")
# print(l1)
# Python program to check if the number is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))
#
# # initialize sum
# sum = 0
#
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
#
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
##
##append():
# l=[1,2,3,4,5,6,7,8,9,10]
# l1=l.append(11)
# print(l)
#extend():
# l2=l.extend([12,13,14])
# print(l)
# # pop():
# l.pop()
# print(l)
##delete():
# del l[4]
# print(l)
# #slicing:
#l.[start:stop:step]
# l1=l[:5]
# print(l1)
# negative slicing:
# l3=l[-2]
# print(l3)
##nested list:indexing,changing
# l.append([15,16,17])
# print(l)
# l[4]=18
# l[2:5]=[19,20,21]
# print(l)
# print(l[1][1])

# ##
# a=[1,2,3,4,5]
# b=['a','b','c','d','e']
# var=dict(zip(a,b))
# print(var)



# for a,b in zip(a,b):
#     print(a,b)
# var={k:v for(k,v) in zip(a,b)}:
#     print(var)

# x = [1,2,3,4,[5,6],[7,8]]
# print(x[4][1])

# l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,[15, 16, 17]]
# print(l1[10][1])
##
# def palindrome(s):
#     return s==s[::-1]
# s="mom"
# ycs=palindrome(s)
# if ycs:
#     print("palindrome")
# else:
#     print("not palindrome")
# ##
# l=[1,2,3,4,5,6]
# k={x:x**2 for x in l}
# k={x:x for x in l if x%2==0}
# print(k)
# str="gayathri"
# str1=str.capitalize()
# print(str1)
##

# class parent():
#     def func(self):
#         print("parent")
# class child(parent):
#     def func1(self):
#         print("child")
# obj=child()
# obj.func()
# obj.func1()
##
# n=int(input("enter a value:"))
# a,b=0,1
# sum=0
# count=1
# print("fibonacci series:",end="")
# while (count<=n):
#     print(sum,end="")
#     count+=1
#     a=b
#     b=sum
#     sum=a+b
# num=int(input("enter a value"))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if num==sum:
#     print(num,"armstrong")
# else:
#     print(num,"is not armstrong")


# d={'a':1,'b':2,'c':3,'d':4,'e':5}
# print(d.get('d'))
#
#
# d={'a':1,'b':2,'c':3,'d':4,'e':5}
# def get_key(val):
#     for key,value in d.items():
#         if val==value:
#             return key
#     return "key doesn't exist"
# print(get_key(5))

# import json
# a={"name":"sindhu","age":24,"salary":50000}
# a1=json.dumps(a)
# print(a1)
#
# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age=age
#
#     def say_hi(self):
#         print('Hello, my name is'+self.name+str(self.age))
# p = Person('Nikhil',25)
# p.say_hi()

## multiple inheritance

# class read:
#     def read(self):
#         print("par1")
# class write:
#     def read(self):
#         print("par2")
# class books(write,read):
#     def read(self):
#         print("child")
#         super().read()
#         super().read()
#
#
# c=books()
# c.read()
##
# x={1:2,3:4}
# y={5:6,7:8}
# x.update(y)
# print(x)

# class read:
#     read=" "
#     def read(self):
#         print(self.read)
# class write:
#     write=" "
#     def write(self):
#         print(self.write)
# class books:
#     def study(self):
#         print("read:",self.read)
#         print("write:",self.write)
# s=books()
# s.read="sindu"
# s.write="swapna"
# s.study()


## fibonacci series
# n=int(input("enter a value:"))
# a,b=0,1
# sum=0
# count=1
# print("fibonacci series:",end=" ")
# while(count<=n):
#     print(sum,end=" ")
#     count+=1
#     a=b
#     b=sum
#     sum=a+b
##
# l=[1,0,1,3,1,2]
# l1=[]
# for i in range(len(l)):
#     if l[i]==1:
#         l1.append(i)
# print(l1)

## AUTHENTICATION IN DJANGO:
# Django comes with a built-in user authentication system to handle objects such as users, groups, permissions, etc.
# It not only performs authentication but authorization as well.
#
# Following are the system objects:
# users
# Groups
# Password Hashing System
# Permissions
# A pluggable backend system
# Forms Validation
# Apart from this, there are various third-party web apps that we can use instead of the default system to provide more user authentication with more features.


# x="aabbccacddaab"
# k=" "
# y={}
# for i in x:
#     y[i]=x.count(i)
# for m,n in y.items():
#     k+=m+str(n)
# print(k)
## PRIME OR NOT

# def checkprime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return 1
# n=int(input("enter avalue"))
# p=checkprime(n)
# if p==1:
#     print("not prime")
# else:
#     print("prime")

## PRINT PRIME NUMBERS
# n1=int(input("enter avalue"))
# n2=int(input("enter a value"))
# for number in range(n1,n2):
#     if number>1:
#         for i in range(2,number):
#             if(number%i)==0:
#                 break
#         else:
#             print(number)
# import re
# #tr=sreej@#!cho#wdhary
# str1=re.sub("[@#!]"," ","sreej@#!cho#wdary")
# print(str1)
##
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms = int(input("How many terms? "))
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))
#

# x=56789
# rev=0
# while x>0:
#     a=x%10
#     rev=rev*10+a
#     x=x//10
# print(rev)
# ##
# l=[1,2,3,4,5]
# l1=[6,7,8,9,10]
# l2=[]
# for i in range(len(l)):
#     l2.append(l[i]+l1[i])
# print(l2)
#
# l=[1,2,3,4,5]
# l1=[6,7,8,9,10]
# l2=[]
# import numpy as np
# x=np.array(l)
# y=np.array(l1)
# print(l2)

# l1 = [1,2,6,12]
# l2 = [12,6,2,1]
# print(l1 == l2)
# print(set(l1) == set(l2))
##
# l = [1,2,3,4,5]
# m = map(lambda x: 2**x, l)
# print(list(m))
## CLASS
# class welcome:
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         print('Welcome ' , self.name )
#
# cw = welcome('Turing')
# cw.say_hello()
##
# print("Welcome to TURING".capitalize())
##
# data =  [1, 2, 3]
# def incr(x):
#     return x+1
# print(list(map(incr, data )))
##
# import re
# result = re.findall('Welcome to Turing ', 'Welcome', 1)
# print(result)

#
# t = '%(a)s %(b)s %(c)s'
# print(t % dict(a='Welcome' , b = 'to' , c='Turing'))

# skills2 = ['Nodejs' , 'Python' , 'Reacys', 'vueshs' ]
# skills2.insert(3, 'Java')
# print(skills2)
##
# class Hello:
#     def __init__(self, a ='welcome to '):
#         self.a = a
#
#     def welcome(self, x):
#         print(self.a + x)
# h = Hello()
# h.welcome('Turing')



# inputs = ['node' , 'react' , 'vue']
# print(inputs)
# for i in inputs :
#     inputs.append(i.upper())
# print(inputs)


# x = "abcde"
# i ="a"
# while i in x[:-1]:
#     print(i, end = " ")


# y = [2, 5j ,7]
# y.sort()
# print(y)



# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# for value in simpleGeneratorFun():
#     print(value)
###
# l=[1,2,3,4,5,6]
# l1=[6,5,4,3,0,0]
# l2=[]
# for i in range(0,len(l1)):
#     l2.append(l[i]+l1[i])
# print(l2)
# ##
# str="missicippi"
# print(''.join(set(str)))

#  foo = 'mppmt'
# >>> ''.join(sorted(set(foo), key=foo.index))
# 'mpt'

## CREATE()
##SINGLE DIMENSION
# import numpy as np
# a=np.array([1,2])
# print(a)
# print(a.ndim)
# print(type(a))
##MULTI DIMENSION
# import numpy as np
# b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(b)
##
# import numpy as np
# a=([[1,2,3],[4,5,6]])
# b=np.asarray(a,order="F")
# for i in np.nditer(b):
#     print(i)
##ASARRAY()
# import numpy as np
# a = ([[1, 2, 3], [4, 5, 6],[7,8,9],[10,11,12]])
# b = np.asarray(a)
# for i in np.nditer(b):
#     print(i)
## BUFFER()
# import numpy as np
# a=b"welcome"
# c=np.frombuffer(a,dtype="S1")
# print(c)
##BUFFER FUN()
# import numpy as np
# a=b"welcome python"
# c=np.frombuffer(a,dtype="S2")
# print(c)
##ITER()
# import numpy as np
# a=([10,20,30,40])
# b=np.fromiter(a,dtype=int,count=-3)
# print(b)
##FLOAT()
# import numpy as np
# a=([10,20,30,40])
# b=np.fromiter(a,dtype=float,count=3)
# print(b)
##BYTES()
# import numpy as np
# a=([10,20,30,40])
# b=np.fromiter(a,dtype="S1",count=3)
# print(b)
# ##
##INTIALIZE()
# import numpy as np
# a=np.zeros([2,3,4])
# print(a)
#
# import numpy as np
# a=np.ones([2,3,4])
# print(a)
##
# import numpy as np
# a=np.full([2,3,4],5)
# print(a)
##
# import numpy as np
# a=np.random.rand(2,3)
# print(a)
# import numpy as np
# a=np.eye(5)
# print(a)
##
# import numpy as np
# a=np.arange(1,10,1)
# print(a)
##
# import numpy as np
# a=np.linspace(10,100,10)
# print(a)
## DIFFERENCE
# import numpy as np
# a=np.linspace(10,100,10,endpoint=False,retstep=True)
# print(a)
##
# import numpy as np
# a=np.logspace(1,10,10,base=2)
# print(a)
# ##
# import numpy as np
# a=np.logspace(1,10,10)
# print(a)
##
# import numpy as np
# a=np.arange(10,100,10)
# b=a.reshape([3,3])
# print(b)
##
# import numpy as np
# a=np.arange(10,100,10)
# b=a.reshape([3,3])
# print(b)
# c=np.size(b)
# print(c)
# d=np.shape(b)
# print(d)
##SLICING
#import numpy as np
# a=np.array([1,2,3,4])
# b=a[0:3]
# print(b)
## COPY()
# import numpy as np
# a=np.array([1,2,3,4])
# b=np.copy(a)
# print(b)
##
# import numpy as np
# a=np.array([1,2,5,4,6])
# b = np.copy(a)
# print(b)
# c = a.view()
# print(c)
##
# import numpy as np
# a=np.array([[10,20],[30,40]])
# b=np.insert(a,3,35)
# print(b)
# c=np.delete(a,3)
# print(c)
# d=np.array([[10,20],[30,40]])
# e=np.array([[40,50],[60,70]])
# f=np.append(d,e)
# print(f)
# g=np.concatenate((d,e))
# print(g)
# k=np.concatenate((d,e),axis=0) (column-wise)
# print(k)
# m=np.concatenate((d,e),axis=1) (row-wise)
# print(m)
# import numpy as np
# a=np.array([10,20,30,40])
# b=np.where(a>20)
# c=np.where(a==20)
# print(b)
# print(c)
##
# import numpy as np
# a=np.arange(10,100,10)
# b=a.reshape(3,3)
# print(b)
##
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([5,4,3,2,1])
# c=np.subtract(a,b)
# print(c)
##
# import numpy as np
# a=np.array([1,2,3,4,5])
# #b=np.array([5,4,3,2,1])
# c=np.sqrt(a)
# print(c)
##
# import numpy as np
# a=np.array([1,2,3,4,5])
# # b=np.array([5,4,3,2,1])
# c=np.exp(a)
# print(c)
##
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([5,4,3,2,1])
# c=np.divide(a,b)
# print(c)
##
# import numpy as np
# a=np.array([[10,20],[30,40],[50,60]])
# b=np.min(a,axis=0)
# print(b)
##
# import numpy as np
# a=np.array([[10,20],[30,40],[50,60]])
# b=np.max(a,axis=0)
# print(b)
##
# import numpy as np
# a=np.array([[10,20],[30,40],[50,60]])
# b=np.sum(a,axis=0)
# print(b)
##
# import numpy as np
# a=np.array([[10,20],[30,40],[50,60]])
# b=np.mean(a)
# print(b)
##
# import numpy as np
# a=np.array([[10,20],[30,40],[50,60]])
# b=np.median(a,axis=0)
# print(b)
##
# import numpy as np
# a=np.array([[10,20],[30,40],[50,60]])
# b=np.std(a)
# print(b)
#

# num=4
# l1 = [1, 2, 3, 4, 5, 6,7,8,9,10]
#
# l1 = (l1[len(l1) - num:len(l1)] + l1[0:len(l1) - num])
#
# print("rotation of List by 3 : " + str(l1))
##
# import pandas as pd
# print(pd.__version__)

# import pandas as pd
# d=pd.read_csv("C:\\Users\\sindh\\OneDrive\\Desktop\\Match.csv")
# df=pd.DataFrame(d)
# print(df)
# print(df.to_string())
# print(df.head())
#
# print(df.tail())

# print(df.describe())

# print((df.describe()).T)

#print(df[0:20:2])
##
#print(df[["id","inning"]])
##
#print(df[["id","inning"]][0:20:2])
##
#print(df.info())
##
#print(df.loc[[1,9]])

#print(df.loc[10,["id","inning"]])

#print(df.loc[0:15,["id","inning"]])
##
#print(df.iloc[[1,10]])

#print(df.iloc[0:4,0:5])
#print(df.iloc[0:5,2])
#print(df.iloc[[1,2,5],:5])
##
# print(df.iloc[:,[1,5,8]])

#print(df.sort_values("inning"))
##
#print(df.sort_values(["inning","id"]))

#print(df.sort_values(["inning","id"],ascending=[0,15]))

##
# df["match"]=0
# print(df)
##
# df["match"]=df["id"]+df["inning"]+df["total_runs"]
# print(df)
##
# df.drop(columns="inning")
# print(df)
##
#print(df.duplicated())
##
# import numpy as np
# s=pd.Series(np.random.rand())
# print(s)
# import numpy as np
# a=np.nditer([1,2,3,4])
# print(a)
##
# l=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("enter a value"))
# for i in range(0,n):
#     a=l[-1]
#     l.pop()
#     l.insert(i,a)
# print(l)
##

# str="missicippi"
# str1={}
# for i in str:
#     if i not in str1:
#         str1[i]=1
#     else:
#         str1[i]+=1
# print(str1)
##REMOVE DUPLICATE VALUES
# s="misicippi"
# s1=""
# for i in s:
#     if i not in s1:
#         s1=s1+i
# print(s1)
##
# s="missicippii"
# c=1
# s1=""
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         c+=1
#     else:
#         s1=s1+s[i]+str(c)
#         c=1
#
# for i in range(len(s)-1,-1):
#     if s[i]==s[i-1]:
#         c+=1
#     else:
#         s1=s1+s[i]+str(c)
#         break
# print(s1)
# #
#l=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("enter a value"))

# def rightRotate(lists, num):
#     list = []
#     for item in range(len(l) - num, len(l)):
#         list.append(l[item])
#
#     for item in range(0, len(l) - num):
#         list.append(l[item])
#
#     return list
# num = 4
# list_1 = [1, 2, 3, 4, 5, 6,7,8,9,10]
# print(rightRotate(list_1, num))

# s="missicippi"
# l=list(s)
# k=[]
# ans=""
# print(len(l))
# print(l)
# c=1
# for i in range(0,len(l)):
#     if i==len(l)-1:
#         ans=ans+l[i]+str(c)
#     elif l[i]==l[i+1]:
#         c=c+1
#     else:
#         ans = ans + l[i]+str(c)
#         c=1
# print(ans)
#
# n1=int(input("enter value"))
# n2=int(input("enter a value"))
# for number in range(n1,n2):
#     if number>1:
#         for i in range(2,number):
#             if(number%i)==0:
#                 break
#         else:
#             print(number)

# l="aaabbbddss"
# l1={}
# for i in l:
#     l1[i]=l.count(i)
# print(l1)
# n=int(input("enter a num: "))
# sum=0
# temp=n
# while temp>0:
#     i=temp%10
#     sum+=i**len(str(n))
#     temp//=10
# if n==sum:
#     print("armstrong number")
# else:
#     print("not a armstrong num")


# n=int(input("enter a num: "))
# x=list(map(int,str(n)))
# y=list(map(lambda i :i**len(str(n)),x))
# if (sum(y)==n):
#     print("armstrong number")
# else:
#     print("not a armstrong num")


# l=[1,2,3,4,'a','b','c']
# l[1],l[5]=l[5],l[1]
# print(l)


# s1="abbcc"
# s2="vnnbbc"

# for i in set(s1):
#     for j in set(s2):
#         if i==j:
#             print(i)


# df1=id,name,age,uuid
# 10k records
# df2=uuid,salary
# 100k records
# df3=id,name age,salary,uuid


# name=' kambapuram vinay kumar '
# l=name.strip()
# print(l)

# l=['a',1,2.0,2.5,-3.5,8]
# l1=[]
# for i in l:
#     if type(i)==float and i<0:
#         l1.append(i)
# print(l1)


# l=['a',1,2.0,2.5,-3.5,8]
# l1=[]
# for i in l:
#     if  i and i>0:
#         l1.append(i)

# print(l[::2])
# print(l[2::-1])


# class parent:
#     def sum(self,a,b):
#         print(a+b)
#     def  sum(self,a,b,c):
#         print(a+b+c)
# x=parent()
# x.sum(5,2,3)


# class A:
#     def mul(self):
#         print("multipy two elements")
#
#
# class B(A):
#     def mul(self):
#         super().mul()
#         # print("modify the behaviour ")
#
#
# x = B()
# x.mul()

# l=[[1,2,3],[4,5,6],7,8,[10]]
# l1=[]
# def func(l):
#     for i in l:
#         if type(i)==list:
#             func(i)
#         else:
#             l1.append(i)
# print("the list after removing:",l)
##
# l=[[1,2],[3,4],5,6,[1,2],3,4]
# l1=[]
# for i in l:
#     if type(i)==list:
#         l1.extend(i)
#     else:
#         l1.append(i)
# print(list(set(l1)))

# l=[1,2,3]
# l1=[[i,i*2]for i in l]
# print(l1)
# l=[1,2,3]
# l1=list(map(lambda i: [i,i*2],[1,2,3]))
# print(l1)

# s="radar"
# s1=s[::-1]
# if s==s1:
#     print("yes")
# else:
#     print("no")
##
# l=[1,2,3,4,5,6,7,8,9]
# l1=list(map(lambda i:i+3,l))
# print(l1)

# def fun(fun1):
#     def inner(a):
#         if a < 18:
#             print("not eligible to vote")
#
#         else:
#             print("yes")
#
#     return inner
#
#
# @fun
# def vote(a):
#     pass
#
#
# vote(19)
## WITHOUT IN BUILT FUNCTION
# l=[1,3,'a',1,'b',2,'a',2,1]
# d={}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
##
# l=[1,3,'a',1,'b',2,'a',2,1]
# d={}
# for i in l:
#     d[i]=l.count(i)
# print(d)

##
# l="HAPPY NEW YEAR"
# b=l.split()
# s=""
# for i in b:
#     s=i+' '+s
# print(s)



# dic_of_dics={'animal_1':{'name':'dog','age':5},'animal_2':{'name':'cat','age':2},'city_1':{'name':'kottayyam', 'population':1335},
# 'city_2':{'name':'kochi','population':10091}}
#
# list_of_dics = [{k: v} for k, v in dic_of_dics.items()]
#     # [value for value in dic_of_dics.values()]
# print(list_of_dics)

##

# import re
# str="my age is 18 i am badasfsdf fasfsaf"
# res=re.findall(r"\s",str)
# print(res)
##
# import re
# string="my age is 18 i am badasfsdf fasfsaf 8 10 2000"
# result=re.findall(r"\d",string)
# print(result)

given_list=[1,1,2,2,3,3,4]
# k=l.pop()
# print(k)
# def dupes(a):
#     s = {}
#     for ele in a:
#         if ele not in s:
#             s[ele] = 1
#         else:
#             s[ele] += 1
#     for x in s:
#         if s[x] == 1:
#             return 'this is the only non-repeating element value is :', s[x], 'and the key is :', x
#     return
#
# l = [4, 7, 4, 5, 7, 6, 5, 6, 10]
# cd = dupes(l)
# print("This is dupes: ", cd)
#
#
# mylist = list(dict.fromkeys(mylist))
# print(mylist)
# res = []
# [res.append(x) for x in given_list if x not in res]
# print(res)
##
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# L = [[row[i] for row in matrix] for i in range(3)]
# print(L)
##
# keys = ['name', 'age', 'job']
# values = ['Bob', 25, 'Dev']
#
# D =tuple(zip(keys, values))
#
# print(D)
##
# keys = ['name', 'age', 'job']
# values = ['Bob', 25, 'Dev']
#
# D =list(zip(keys, values))
#
# print(D)

#
# def output_strings(str1,str2):
#     op1=""
#     op2=""
#     for ch in str1:
#         if ch not in str2 and ch not in op1:
#             op1+=ch
#     for ch in str2:
#         if ch not in str1 and ch not in op2:
#             op2+=ch
#     if len(op1)!=0 and len(op2)!=0:
#         return op1,op2
#     elif len(op1)!=0 and len(op2)==0:
#         return op1,None
#     elif len(op2)!=0 and len(op1)==0:
#         return None,op2
#     elif len(op1)==0 and len(op2)==0:
#         return None,None
#
# str1=input()
# str2=input()
# print(output_strings(str1,str2))
# x=lambda a*a


def myfunc(a):
    a=a.append(5)
x=[1,2,3,4]
myfunc(x)
print(x)

















