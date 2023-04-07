def my_func_sort(arg1, arg2, arg3):
    lst = [arg1, arg2, arg3]
    lst.sort()
    print("решение c sort", lst[1]+lst[2])
def my_func_no_sort(arg1, arg2, arg3):
    lst = [arg1, arg2, arg3]
    max_num = 0
    second_num = 0

    for i in lst:
        if i>=max_num:
            max_num = i

    lst.remove(max_num)
    for i in lst:
        if i>=second_num:
            second_num = i
    print("решение без sort",max_num+second_num)

arg1 = int(input("ведите аргумент 1: "))
arg2 = int(input("ведите аргумент 2: "))
arg3 = int(input("ведите аргумент 3: "))
my_func_sort(arg1, arg2, arg3)
my_func_no_sort(arg1, arg2, arg3)