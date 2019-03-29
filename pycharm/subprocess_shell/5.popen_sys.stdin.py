import subprocess
import sys


def test_python(cmd):
    obj = subprocess.Popen(cmd, 
                           stdin=sys.stdin, 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE,
                           cwd="/root", 
                           shell=True)
    stdout, stderr = obj.communicate()
    if obj.returncode == 0:
        return stdout.decode()
    return stderr.decode()


if __name__ == "__main__":
    print(test_python("grep root"))
