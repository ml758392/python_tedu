# -*-coding:utf-8-*-
def func(**args):
    for key, value in args.items():
        print(key, value)


func(name="yy", age =18)
func(**{"name": "yy", "age": 18})


def fun(name, age):
    """
    这是文档的文字内容
    :param name:表示学生的姓名
    :param age: 表示学生的年龄
    :return: 此函数没有返回值
    """

help(fun)
fun.__doc__