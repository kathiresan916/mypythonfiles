'''
grades = [60, 70]
grades.extend([80, 90])
# grades.append(90)
print(grades)


grades = [70, 60, 75, 60]
grades.remove(60)
print(grades)


grades = [80, 70, 60, 90]
grades.sort()
grades.insert(1, 95)
print(grades)


list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1[-1])



def double_first_element(lst):
    if len(lst) > 0:
        lst[0] = lst[0] * 2


list1 = [10, 100, 1000]
double_first_element(list1)
print(list1[0])


def interrupted(s):
    s[-1] = "-"

greeting = "how are you"
interrupted(greeting)
print(greeting)


for i in range(2, 11, 3):
    print(i)



def print_every_third_char(s):
    for i in range(0, len(s), 3):
        print(s[i])


print(print_every_third_char('abcABCacbABC'))



for i in range(5, 101, 5):
    print(i)
'''

# print('3' in [1, 2, 3]) False
# print(len([1,2,3]) == len(['a', 'b', 'c'])) True
# print([1, 2, 3] in len('mom')) Error
# print(int('3') in [len('a'), len('b'), len('c')]) False
# print('a' in ['mom', 'dad']) False
# print(len('mom') in [1, 2, 3]) True

'''
def secret(s):
    i = 0
    resullt = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1
    return result


print(secret('123abc')) #all error



def example(L):
    """(list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result
'''


def compress_list(L):
    compressed_list = []
    i = 0
    while i < len(L):
        compressed_list.append(L[i] + L[i+1])
        i = i + 2
    return compressed_list


print(compress_list(['a', 'b', 'c', 'd']))
