
#import keyword
#keyword.kwlist
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from ctypes.wintypes import WORD
from re import X
from tkinter import Y
from traceback import print_tb


print("Hello, World!")#输出Hello, World!

counte =1                      
miles = 1000.0
name = "John"
print("Count is:", counte)
print("Miles is:", miles)
print("Name is:", name)

#Number(数字)
#String(字符串)
#List(列表)
#Tuple(元组)
#Dictionary(字典)
# 定义函数
#不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
#可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）；
print("   ")


# 定义数字
a, b, c, d = 20, 5.5, True, 4+3j
print("a=",a,"b=",b,"c=",c,"d=",d)                      # Output: 20 5.5 True (4+3j)输出的数字是定义的数字
print(type(a), type(b), type(c), type(d)) # Output: <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>输出的类型是int、float、bool、complex而不是定义的数字
print("   ")
# 类型判断
a = 111
isinstance(a, int)
True
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。

# 定义函数
def my_function(x):
    return 3*x + 1

# 调用函数
print(my_function(5)) # Output: 16
print("   ")
...
...

#打印字符串
str ="MarkSmallChirle"
print(str)                 # Output: MarkSmallChirle打印整个字符串
print(str[0:-1])           # Output: MarkSmallChirl 打印字符串的第一个到倒数第二个字符（不包含最后一个字符）
print(str[0])              # Output: M    打印字符串的第一个字符
print(str[2:5])            # Output: rkS  打印字符串第三到第五个字符（包含第五个字符）
print(str[2:])             # Output: rkSmallChirle打印字符串从第三个字符开始到末尾
print(str*2)               # Output: MarkSmallChirleMarkSmallChirle
print(str+"TEST")          # Output: MarkSmallChirleTEST
print("   ")

#\n 换行符和r前缀表示原始字符串，即字符串中的\n不会被转义。
print('Mark\nSmallChirle')  # Output: Mark           SmallChirle
print(r'Mark\nSmallChirle') # Output: Mark\nSmallChirle
print("   ")

word ='Python'
print(word[0],word[5])   # Output: P y
print(word[-1],word[-6]) # Output: n P
print(word[1:5])         # Output: ytho
print(word[1:-1])        # Output: ytho
print("   ")

#bool类型
X = True
Y = False
#比较运算符
print(2<3) # Output: True
print(2==3) # Output: Flsae
print(2!=3) # Output: True
print("   ")
#逻辑运算符
print(X and Y) # Output: False
print(X or Y) # Output: True
print(not a) # Output: False
print("   ")
#类型转换
print(int(X))
print(float(Y))
#二进制位运算符
print(5&3) # Output: 1
print(5|3) # Output: 7
print(5^3) # Output: 6
print(~5)  # Output: -6
print(5<<2) # Output: 20 这是左移运算符。将整数 5 左移两位，相当于乘以 2 的幂，得到 20
print(5>>2) # Output: 1 这是右移运算符。将整数 5 右移两位，相当于除以 2 的幂，得到 1
print("   ")

#列表
list = ['a,b,c,d',123,4.56,'runb', 7]
tinylist = [8.9,'runoob']

print(list)         #打印列表
print(list[0])       #打印列表的第一个元素
print(list[1:3])    #打印列表的第二个到第三个元素
print(list[:3])     #打印列表的前三个元素 
print(list[2:])     #打印列表的第三个到最后一个元素
print(tinylist*2)
print(list+tinylist)
print("   ")
def reverseWords(input): 
      
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ") 
  
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
  
    # 重新组合字符串
    output = ' '.join(inputWords) 
      
    return output 
  
if __name__ == "__main__": 
    input = 'I am runoob'
    rw = reverseWords(input) 
    print(rw)
 
    print("   ")

#元组
tuple=('apple',123,5.67,'banana')
tinytuple=(123,'runoob')

print(tuple)         #打印元组
print(tuple[0])      #打印元组的第一个元素
print(tuple[1:3])    #打印元组的第二个到第三个元素
print(tuple[2:])     # 输出从第三个元素开始的所有元素
print(tinytuple*2)
print(tuple+tinytuple)
print("   ")

#集合
sites={'Google','Runoob','Taobao','Facebook','Bilibili','X'}
print(sites)
#成员测试
if 'Google' in sites:
    print('Google is a website')
else:
    print('Google is not a website')

#set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a-b)           # a 和 b 的差集
print(a|b)           # a 和 b 的并集
print(a&b)           # a 和 b 的交集
print(a^b)           # a 和 b 中不同时存在的元素
print("   ")

#字典
#dict={}
#dict['one']="1 - 菜鸟教程"
#dict[2]="2 - 菜鸟工具"
#tinydict={'name': 'runoob','code':1,'site': 'www.runoob.com'}

#print(dict['one'])       #输出键为 'one' 的值
#print(dict[2])           #输出键为 2 的值
#print(tinydict)          #输出完整的字典
#print(tinydict.keys())   #输出所有键
#print(tinydict.values()) #输出所有值
#print("   ")








