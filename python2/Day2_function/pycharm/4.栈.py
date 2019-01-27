# -*-coding:utf-8-*-
# 栈不但实现了先进后出的数据结构，还会检查操作栈的用户是否具有相应的权限，只有管理员才能进行栈操作

# 不使用装饰器
# def check_is_admin(username):
#     if username != 'admin':
#         raise Exception('This user is not allowed to put/get elem')
#
#
# class Stack:
#     def __init__(self):
#         self.storage = []
#
#     def put(self, username, elem):
#         check_is_admin(username)
#         self.storage.append(elem)
#
#     def get(self, username):
#         check_is_admin(username)
#         if not self.storage:
#             raise Exception('There is no elem in stack')
#         self.storage.pop(elem)


# 使用装饰器
def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('This user is not allowed to put/get elem')
        return f(*args, **kwargs)
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
    a.put(username='admin', elem='pp')
    print(a.get(username='admin'))

    # a.put('admin', elem=2) 回报错,因为值是从关键字参数中获取的
    # 解决获取参数的问题









