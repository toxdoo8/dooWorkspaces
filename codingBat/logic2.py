def make_chocolate(small, big, goal):
  after_big = goal-(big*5)
  if after_big == 0:
    return 0
  elif after_big == small:
    return small
  elif after_big < small or after_big < 0:
    if after_big < 0:
      re = count_up(big, goal)
      if re == 0:
        return 'Monkey'
    elif after_big < small:
      return after_big
  else:
    return -1
def count_up(big, goal):
  newI = 0
  for i in range(1,big):
    if goal-(i*5) > 5:
      newI += i
  return newI
print(make_chocolate(6, 2, 7))
print(make_chocolate(5, 4, 9))


Str2_count_hi='Return the number of times that the string "hi" appears anywhere in the given string.'
def count_hi(str):
    c = 0
    for i in range(0,len(str)-1):
        if (str[i] + str[i + 1]).lower() in 'hi':
            c += 1
    print(c)
count_hi('HIABChi hi')

Str2CatDog='Return True if the string "cat" and "dog" appear the same number of times in the given string.'
def cat_dog(str):
  if 'catdog' in str:
    return True
  else:
    return False
print(cat_dog('catxdogxdogxca'))

# def close_far(a, b, c):
#     re_ab = abs(a-b)
#     re_ac = abs(a-c)
#     re = abs(re_ab-re_ac)
#     print(re_ab,re_ac,re)
#     if re >= 2:
#         return True
#     else:
#         return False
# close_far(1, 2, 10)

# def round_sum(a, b, c):
#     t = 0
#     for i in (a,b,c):
#         new_i = round10(i)
#         t += new_i
#         print(t, type(t))
#     return t
# def round10(i):
#     if i in range(0,5):
#         return 0
#     elif i%10 >= 5:
#         while i%10 != 0:
#             i += 1
#         return i
#     else:
#         while i%10 != 0:
#             i -= 1
#         return i
# round_sum(20,21,49)

# def no_teen_sum(a, b, c):
#   re = 0
#   for i in (a,b,c):
#     k = fix_teen(i)
#     re += k
#   return re
# def fix_teen(n):
#   if n not in (13,14,17,18,19):
#     return n
#   else:
#     return 0
# print(no_teen_sum(2, 1, 15))
# print(no_teen_sum(2, 1, 17))

#
# def lone_sum(a, b, c):
#     count = len(set((a, b, c)))
#     print('count',count)
#     ct = 0
#     dict = {}
#     if count == 1:
#         print('0')
#     elif count == 3:
#         total = a+b+c
#         print(total)
#     elif count == 2:
#         for i in (a, b, c):
#             # print(i)
#             if i in set((a, b, c)):
#                 ct += 1
#                 dict[i] = ct
#         key = min(dict.keys(), key=(lambda k: dict[k]))
#         print(key)
# lone_sum(4,5,6)
# lone_sum(3,2,3)
# lone_sum(33,22,33)
# lone_sum(3, 3, 3)
#
# def make_bricks(small, big, goal):
#     print(goal%5<=small and goal-(big*5)<=small)
# make_bricks(3, 1, 8)
# make_bricks(3, 1, 9)
# make_bricks(2, 1000000, 100003)
# make_bricks(1, 4, 12)
# make_bricks(5, 0, 12)
#
# def near_ten(num):
#     re = num%10
#     print(re)
#     if re in range(0,3):
#         print('True')
#     else:
#         print('False')
# near_ten(158)
#
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
