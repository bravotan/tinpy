#!/usr/bin/env python

import tinpy

tpl = '''\
[% for k in dic.keys() %][% var dic[k][kk] %][% done %]
[% var x %]
'''
class A:
    def func(self):
        return range(10)
    def x(self, a):
        return a

a = A()
dic = {'a': {'x': a}}
print tinpy.build(tpl, dic=dic, kk='x', a=a, x='XXX')
