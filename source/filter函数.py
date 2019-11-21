def is_int(val):
    try:
        return int(val)
    except:
        return False


list = ['a', '3', 'd', 'f', '5', '6']

# 第一个参数是函数，第二个参数是需要判断的值，filter函数返回is_int 函数返回True的值
# filter 函数返回一个filter类，需要用list转换成列表，也可以直接for循环遍历
result = filter(is_int, list)
for i in result:
    print(i)

print(type(result))
