"""
编写一个接受行序列作为输入的程序，并在使句子中的所有字符大写后打印行。
假设为程序提供了以下输入：
Hello world
Practice makes perfect
然后，输出应该是：
HELLO WORLD
PRACTICE MAKES PERFECT
提示：
如果输入数据被提供给问题，则应该假定它是控制台输入。
"""
lines = []
while True:
    s = input('input:')
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print(sentence)

