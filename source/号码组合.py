# 通过一个递归函数实现
# 传入参数：需要实现的数字，以及每个数字代表的字母

# 先构思两个数字，再构思三个数字*****
def func(num, nums):
    # num : 输入的数字
    # nums : 每个数字所对应的字母组合
    # 首先定义一个结果变量
    result = []
    # 如果数字小于等于9，则直接返回该数字代表的字符数组
    if num <= 9:
        return nums[num]
    # 否则，进入递归
    else:
        # 首先取第一个数字，从该数字代表的字母开始遍历
        for i in nums[num % 10]:
            # 取后一个字母进入递归，并且在返回的字符串中遍历
            for j in func(num // 10, nums):
                # 在结果集上添加一个字符串
                result.append(i + j)
        # num = num // 10
        # 返回该结果集
        return result


numStr = '0'
while True:
    numStr = input("please input the num")
    if '0' in numStr or '1' in numStr:
        continue
    else:
        break
print(reversed(numStr))
num = int(numStr[::-1])

print(num)

num2 = ['a', 'b', 'c']
num3 = ['d', 'e', 'f']
num4 = ['g', 'h', 'i']
num5 = ['j', 'k', 'l']
num6 = ['m', 'n', 'o']
num7 = ['p', 'q', 'r', 's']
num8 = ['t', 'u', 'v']
num9 = ['w', 'x', 'y', 'z']

nums = ['', '', num2, num3, num4, num5, num6, num7, num8, num9]

result = func(num, nums)

print(result)

print(len(result))
