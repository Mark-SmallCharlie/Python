
#import keyword
#keyword.kwlist
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from ctypes.wintypes import WORD
from re import X
from tkinter import Y
from traceback import print_tb


print("Hello, World!")#���Hello, World!

counte =1                      
miles = 1000.0
name = "John"
print("Count is:", counte)
print("Miles is:", miles)
print("Name is:", name)

#Number(����)
#String(�ַ���)
#List(�б�)
#Tuple(Ԫ��)
#Dictionary(�ֵ�)
# ���庯��
#���ɱ����ݣ�3 ������Number�����֣���String���ַ�������Tuple��Ԫ�飩��
#�ɱ����ݣ�3 ������List���б���Dictionary���ֵ䣩��Set�����ϣ���
print("   ")


# ��������
a, b, c, d = 20, 5.5, True, 4+3j
print("a=",a,"b=",b,"c=",c,"d=",d)                      # Output: 20 5.5 True (4+3j)����������Ƕ��������
print(type(a), type(b), type(c), type(d)) # Output: <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>�����������int��float��bool��complex�����Ƕ��������
print("   ")
# �����ж�
a = 111
isinstance(a, int)
True
#type()������Ϊ������һ�ָ������͡�
#isinstance()����Ϊ������һ�ָ������͡�

# ���庯��
def my_function(x):
    return 3*x + 1

# ���ú���
print(my_function(5)) # Output: 16
print("   ")
...
...

#��ӡ�ַ���
str ="MarkSmallChirle"
print(str)                 # Output: MarkSmallChirle��ӡ�����ַ���
print(str[0:-1])           # Output: MarkSmallChirl ��ӡ�ַ����ĵ�һ���������ڶ����ַ������������һ���ַ���
print(str[0])              # Output: M    ��ӡ�ַ����ĵ�һ���ַ�
print(str[2:5])            # Output: rkS  ��ӡ�ַ���������������ַ�������������ַ���
print(str[2:])             # Output: rkSmallChirle��ӡ�ַ����ӵ������ַ���ʼ��ĩβ
print(str*2)               # Output: MarkSmallChirleMarkSmallChirle
print(str+"TEST")          # Output: MarkSmallChirleTEST
print("   ")

#\n ���з���rǰ׺��ʾԭʼ�ַ��������ַ����е�\n���ᱻת�塣
print('Mark\nSmallChirle')  # Output: Mark           SmallChirle
print(r'Mark\nSmallChirle') # Output: Mark\nSmallChirle
print("   ")

word ='Python'
print(word[0],word[5])   # Output: P y
print(word[-1],word[-6]) # Output: n P
print(word[1:5])         # Output: ytho
print(word[1:-1])        # Output: ytho
print("   ")

#bool����
X = True
Y = False
#�Ƚ������
print(2<3) # Output: True
print(2==3) # Output: Flsae
print(2!=3) # Output: True
print("   ")
#�߼������
print(X and Y) # Output: False
print(X or Y) # Output: True
print(not a) # Output: False
print("   ")
#����ת��
print(int(X))
print(float(Y))
#������λ�����
print(5&3) # Output: 1
print(5|3) # Output: 7
print(5^3) # Output: 6
print(~5)  # Output: -6
print(5<<2) # Output: 20 ��������������������� 5 ������λ���൱�ڳ��� 2 ���ݣ��õ� 20
print(5>>2) # Output: 1 ��������������������� 5 ������λ���൱�ڳ��� 2 ���ݣ��õ� 1
print("   ")

#�б�
list = ['a,b,c,d',123,4.56,'runb', 7]
tinylist = [8.9,'runoob']

print(list)         #��ӡ�б�
print(list[0])       #��ӡ�б�ĵ�һ��Ԫ��
print(list[1:3])    #��ӡ�б�ĵڶ�����������Ԫ��
print(list[:3])     #��ӡ�б��ǰ����Ԫ�� 
print(list[2:])     #��ӡ�б�ĵ����������һ��Ԫ��
print(tinylist*2)
print(list+tinylist)
print("   ")
def reverseWords(input): 
      
    # ͨ���ո��ַ����ָ������Ѹ������ʷָ�Ϊ�б�
    inputWords = input.split(" ") 
  
    # ��ת�ַ���
    # �����б� list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ���� -1 ��ʾ���һ��Ԫ�� list[-1]=4 ( �� list[3]=4 һ��) 
    # inputWords[-1::-1] ����������
    # ��һ������ -1 ��ʾ���һ��Ԫ��
    # �ڶ�������Ϊ�գ���ʾ�ƶ����б�ĩβ
    # ����������Ϊ������-1 ��ʾ����
    inputWords=inputWords[-1::-1] 
  
    # ��������ַ���
    output = ' '.join(inputWords) 
      
    return output 
  
if __name__ == "__main__": 
    input = 'I am runoob'
    rw = reverseWords(input) 
    print(rw)
 
    print("   ")

#Ԫ��
tuple=('apple',123,5.67,'banana')
tinytuple=(123,'runoob')

print(tuple)         #��ӡԪ��
print(tuple[0])      #��ӡԪ��ĵ�һ��Ԫ��
print(tuple[1:3])    #��ӡԪ��ĵڶ�����������Ԫ��
print(tuple[2:])     # ����ӵ�����Ԫ�ؿ�ʼ������Ԫ��
print(tinytuple*2)
print(tuple+tinytuple)
print("   ")

#����
sites={'Google','Runoob','Taobao','Facebook','Bilibili','X'}
print(sites)
#��Ա����
if 'Google' in sites:
    print('Google is a website')
else:
    print('Google is not a website')

#set���Խ��м�������
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a-b)           # a �� b �Ĳ
print(a|b)           # a �� b �Ĳ���
print(a&b)           # a �� b �Ľ���
print(a^b)           # a �� b �в�ͬʱ���ڵ�Ԫ��
print("   ")

#�ֵ�
#dict={}
#dict['one']="1 - ����̳�"
#dict[2]="2 - ���񹤾�"
#tinydict={'name': 'runoob','code':1,'site': 'www.runoob.com'}

#print(dict['one'])       #�����Ϊ 'one' ��ֵ
#print(dict[2])           #�����Ϊ 2 ��ֵ
#print(tinydict)          #����������ֵ�
#print(tinydict.keys())   #������м�
#print(tinydict.values()) #�������ֵ
#print("   ")








