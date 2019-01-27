# -*-coding:utf-8-*-
# def index_words(text):
#     result = []
#     if  text:
#         result.append(0)
#     for index, letter in enumerate(text, 1):
#         if letter == ' ':
#             result.append(index)
#     return result
#
#
# text = 'The zen of python, by tim peters'
# print(index_words(text))


def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            yield index


text = 'The zen of python, by tim peters'
print(list(index_words(text)))
