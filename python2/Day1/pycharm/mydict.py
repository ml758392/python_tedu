# -*-coding:utf-8-*-
addict = {"name": "bob", "age": 18}
for key in addict:
    print('%s:%s' % (key, addict[key]))
print('%(name)s' % addict)