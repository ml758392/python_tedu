# -*-coding:utf-8-*-
import re


print(re.search(r'to', 'welcome to beijing, welcome to nayang').group())



print(re.search(r'((^W)(.+?))g$', 'welcome to BeiJing', re.I).group())