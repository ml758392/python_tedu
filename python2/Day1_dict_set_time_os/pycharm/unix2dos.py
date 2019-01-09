# -*-coding:utf-8-*-
import sys

def unix2dos(fname):
    new_fname = fname+'.txt'
    with open(fname) as old:
        with open(new_fname,"w") as new:
            for line in old:
                new.write(line.rstrip()+"\r\n")

if __name__ == '__main__':
    unix2dos(sys.argv[1])
