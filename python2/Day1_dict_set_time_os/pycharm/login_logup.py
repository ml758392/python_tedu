# -*-coding:utf-8-*-
dictionary = {}


def login():
    if not dictionary:
        print('''ERROR!!!
no user in database
please register before login!\n''')
        return
    print("{:%^50}0".format("Welcome to login"))
    username = input("input your username：").strip()
    password = input("input password：").strip()
    if username:
        if dictionary[username] == password:
            print("login successful")
        else:
            print("username or password error")

def register():
    print("{:*^50}".format("welcome to register"))
    username = input("input your username：").strip()
    password = input("input password：").strip()
    repeat = input("repeat password：").strip()
    if password and password == repeat:
        print("register successful!")
    else:
        print("ERROR!\nempty password or password mismatch!")
    dictionary.update({username: password})


def choice():
    while True:
        prompt = input('''(1)login
(2)register
(*)exit
input your choice:''').strip()
        if prompt == "1":
            login()
        elif prompt == "2":
            register()
        else:
            break


if __name__ == "__main__":
    choice()





