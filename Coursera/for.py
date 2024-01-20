'''
def calculate_repeats(s):
    repeat = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            repeat = repeat + 1
    return repeat


print(calculate_repeats('abccdeffggh'))



def shift_left(L):

    first_item = L[0]
    for i in range(1, len(L)):
        L[i-1] = L[i]
    L[-1] = first_item


letters = ['z', 'y', 'x', 'w']
shift_left(letters)
print(letters)



def sum_items(list1, list2):
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    return sum_list


print(sum_items([2, 4, 2], [1, 2]))


inner = ['1', '2', '3', '4', '5']
outer = ['1', '2', '3', '4', '5', '6', '7']
for i in outer:
    for j in inner:
        print("Spam!", end="")
'''


def mystery(lst):
    total = 0,
    for i in lst:

        for j in i:
            total = total + j
    return total


print(mystery([[10, 20], [20], [40, 10]]))
