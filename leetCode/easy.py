def count_primes(num):
  prime=[2]
  x = 3
  while x<=num:
    for i in range(3,x,2):
      k = i
      if x%i==0:
        x += 2
        break
    else:
      prime.append(x)
      x += 2
  return prime,len(prime)
a, b = count_primes(100)
print(a, b)

# def isPalindrome(x):
#     a = str(x)[::-1]
#     if str(x) == a:
#         return True
#     else:
#         return False
# print(isPalindrome(121))
# print(isPalindrome(-121))
# print(isPalindrome(10))

# def twoSum(nums, target):
#     dict={}
#     for k,v in enumerate(nums):
#         result=target-v
#         if result in dict:
#             print([dict[result], k])
#         dict[v] = k
# twoSum([9, 0, 2, 11, 7, 15], 9)
#
# class Solution(object):
#     def reverse(self, x):
#         try:
#             if x > 0:  # handle positive numbers
#                 a = int(str(x)[::-1])
#             if x <= 0:  # handle negative numbers
#                 a = -1 * int(str(x * -1)[::-1])
#                 # handle 32 bit overflow
#             mina = -2 ** 31
#             maxa = 2 ** 31 - 1
#             if a not in range(mina, maxa):
#                 return 0
#             else:
#                 return a
#         except:
#             print('Invalid integer value',x)
#             exit(10)
# x = Solution()
# print(x.reverse(-123.678))
# print(x.reverse(-246))


likes = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
# print(likes.count("likes"))

