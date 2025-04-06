# Pyramids
n = int(input("Enter the height of the pyramid: "))
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
    