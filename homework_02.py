# 问题1.对列表a 中的数字从小到大排序
# 问题2.排序后去除重复的数字
# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]

a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
a.sort(reverse=False)  # 为false时，是从小到大 为true时，从大到小
print(a)
print(set(a))  # 将列表转化为set集合(无序的不重复的)