# Week 3 - Star Programs


# 1. Increasing asterisks.
for i in range(1, 6):
    print("*" * i)


# 2. Decreasing asterisks.
for i in range(5, 0, -1):
    print("*" * i)


# 3. Right-aligned asterisks.
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)


# 4. Left-aligned asterisks with spaces.
for i in range(1, 6):
    print("* " * i)


# 5. Pyramid pattern.
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)


# 6. Inverted pyramid pattern.
for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)


# 7. Upside-down pyramid pattern.
for i in range(5, 0, -1):
    print("* " * i)


# 8. Hollow half pyramid.
for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 9. Diamond pattern.
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)


# 10. Hollow square.
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 11. Hollow diamond.
n = 5

for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 12. Hourglass pattern.
for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)

for i in range(2, 6):
    print(" " * (5 - i) + "* " * i)


# 13. Checkered pattern.
for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()