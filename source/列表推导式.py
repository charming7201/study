list = [1,2,3,4,5,6,7,8,9,10]

# 找出列表中大于5的数
result = [n for n in list if n > 5]

# 将列表中小于6的数换成0
result2 = [n if n > 5 else 0 for n in list]

print(result,result2)