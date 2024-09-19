pattern_size = int(input("Enter the size of the pattern: "))

row = 0
while row < pattern_size:
    for _ in range(pattern_size):
        print("*", end="")
    print()
    row += 1

# for i in range(pattern_size):
#     for j in range(pattern_size):
#         if i == 0 or i == pattern_size - 1 or j == 0 or j == pattern_size - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()