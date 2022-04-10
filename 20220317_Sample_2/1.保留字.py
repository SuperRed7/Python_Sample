# coding:utf-8
"""
保留字是Python赋予特殊意义的一些单词,不能用作常数或变数,或任何其他标识符名称。
保留字区分大小写。
https://www.jianshu.com/p/ed8ec8ec20b8
1.条件关键字:if,elif,else,for,in,while,break,return,continue
2.运算符 True,False,None
3.类级 class,lamdba,def,is,import,from
4.逻辑运算符 and,or,not
5.异常 try,exception,raise,finally
6.python特殊 is,nonlocal,del,global,with,as,yield,assert
"""
import keyword
print(keyword.kwlist)
true='真'
# True='真'
