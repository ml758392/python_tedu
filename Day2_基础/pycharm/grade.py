#-*-coding:utf-8-*-
grade = int(input("请输入成绩："))
if grade>=90:
    print("优秀")
elif grade>=80:
    print("好")
elif grade>=70:
    print("良")
elif grade>=60:
    print("及格")
else:
    print("要加油了")