# -*-coding:utf-8-*-
import functools
import inspect


def check_is_admin(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_args = inspect.getcallargs(func, *args, **kwargs)
            if func_args.get('username') != 'admin':
                raise Exception('This user is not allowed to put/get elem')
            return func(*args, **kwargs)
        return wrapper


class Stack:
    def __init__(self):
        self.storage = []

    @check_is_admin
    def put(self, username, elem):
        self.storage.append(elem)

    @check_is_admin
    def get(self, username):
        if not self.storage:
            raise Exception('There is no elem in stack')
        return self.storage.pop()


if __name__ == '__main__':
    a = Stack()

    # 不管位置参数还是关键字参数，都能识别
    a.put(username='admin', elem='pp')
    a.put('admin', 'oo')
    print(a.get(username='admin'))


