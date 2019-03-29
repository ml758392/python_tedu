# -*-coding:utf-8-*-
import fileinput


for line in fileinput.input():
    meta = [fileinput.filename(),
            fileinput.fileno(),
            fileinput.filelineno(),
            fileinput.isfirstline(),
            fileinput.isstdin()]
    print(*meta, end="")
    print(" ", end="")
    print(line, end="")
