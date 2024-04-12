# study drill....


# def print_numbers(n, x):
#     i = 0
#     numbers = []

#     while i < n:
#         print("At the top i is %d" % i)
#         numbers.append(i)
#         i = i + x
#         print("Numbers now: ", numbers)
#         print("At the bottom i is %d" % i)

#     print("The numbers: ")
#     for num in numbers:
#         print(num)


# print_numbers(8, 2)

# Using for loop..
number = []
for i in range(0, 6):
    print("At the top i is %d" % i)
    number.append(i)
    print("Numbers now: ", number)
    print("At the bottom i is %d" % i)


print("The numbers: ")
for num in number:
    print(num)
