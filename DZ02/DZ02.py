# Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
num = int(input("Введите кол элементов списка: "))
list = [0] * num
for i in range(len(list)):
    list[i] = int(input(f"Введите {i} элемент списка: "))
number = int(input(f"Введите число для поиска ближайшего к нему: "))
i = 0
while number == list[i]:
    i += 1
    seach_num = list[i]
for list1 in list:
    if list1 != number:
        if abs(list1 - number) < abs(seach_num - number):
            seach_num = list1
print(f"Ближайшее число к числу {number} это {seach_num} ") 

