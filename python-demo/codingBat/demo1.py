
def lone_sum(*a):
    c = 0
    dict = {}
    for i in (a):
        # print(i)
        if i in set((a)):
            c += 1
            dict[i] = c
    key = min(dict.keys(), key=(lambda k: dict[k]))
    print(key)
# lone_sum(1, 2, 3)
lone_sum(9,11,11)
# lone_sum(3, 3, 3)

# def make_bricks(small, big, goal):
#     print(goal%5<=small and goal-(big*5)<=small)
# make_bricks(3, 1, 8)
# make_bricks(3, 1, 9)
# make_bricks(2, 1000000, 100003)
# make_bricks(1, 4, 12)
# make_bricks(5, 0, 12)

# def near_ten(num):
#     re = num%10
#     print(re)
#     if re in range(0,3):
#         print('True')
#     else:
#         print('False')
# near_ten(158)

# def string_splosion(str):
#   re = []
#   a=''
#   for i in str:
#       a += i
#       re += a
#       # re += str[:len(str)+1]
#   print(''.join(re))
# string_splosion('code')
#
