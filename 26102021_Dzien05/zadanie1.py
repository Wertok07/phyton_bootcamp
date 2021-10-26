# string = ""
#
# x = 0
# while x<10:
#     y = 0
#     while y<10:
#         wartosc = x*y
#         string = string + " " + str(wartosc)
#         y = y + 1
#     string = string + "\n"
#     x = x + 1
#
# print(f"{string:5}")
for i in range(1, 10):
    print(f"{i:<4}", end="")
print()
for i in range(1, 10):
    print(f"{i:<2}", end="")
    for j in range(1, 10):
        print(f"{i*j:4}", end=" ")
    print()
