def scope_test():
    def do_local():
        spam = "local spam"  # 局部变量

    def do_nonlocal():
        nonlocal spam  # 相当于从闭包中去找变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"  # 声明了一个全局变量，和闭包中的变量没有关系

    spam = "test spam"  # 这个是闭包的变量

    do_local()
    print("After local assignment:", spam)  # test spam   这是局部变量
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # nonlocal spam   这是闭包中的变量
    do_global()
    print("After global assignment:", spam)  # nonlocal spam   这依然是闭包中的变量


scope_test()
print("In global scope:", spam)  # global spam   这个是全局的变量
