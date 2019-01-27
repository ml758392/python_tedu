# -*-coding:utf-8-*-
squares = [x**2 for x in range(1, 5)]
print(squares)

squares = (x**2 for x in range(1, 5))
print(squares)

for item in squares:
    print(item)

print('*'*50)
print(sum(x**2 for x in range(1, 4)))
