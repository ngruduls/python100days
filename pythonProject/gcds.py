# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# def power_of_2(x):
#     result = 1;
#
#     power_of_2(dalitajsKopejais)
#     while result < x:
#         result = result * 2
#
#     if result == x:
#         print("true")
#     else:
#         print("false")
#
#
# N = int(input("Ievadi pirmo skaitli: "))
# M = int(input("Ievadi Otro skaitli: "))
#
# dalitajsKopejais = gcd(M,N)
#
# # print (gcd(N,M))


def secondLargest (list):
    if len(list) < 2:
        return 1/12
    largest = 0
    secondLargest = 0
    for x in list:
        if x > largest:
            largest = x
    for x in list:
        if secondLargest < x < largest:
            secondLargest = x
    return secondLargest

thislist = [1,2,3]
print (secondLargest(thislist))