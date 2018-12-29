# -*-coding:utf-8-*-
def func(**args):
    for key, value in args.items():
        print(key, value)

func("name"=)
func(**{"name": "yy", "age": 18})


