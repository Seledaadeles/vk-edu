#coding: utf-8
print('Current location is ' + input() + ' and time is ' + input() )
x = input()
x = set(x)
x = sorted(x)
x = ' '.join(map(str,x))
print(x)