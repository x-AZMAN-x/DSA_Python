def powerSet(my_set):
    n = len(my_set)
    power_set_size = 1 << n

    print("Power Set: ")
    power_set = []
    for counter in range(power_set_size):
        subset = []
        for j in range(n):
            if counter & (1 << j):
                subset.append(my_set[j])
        power_set.append(subset)
    return power_set

# my_set = [1, 2, 3, 4]
my_set = []
size = int(input("How Many Elements You Want In Your List? "))
i = 0
while (i < size):
    x = int(input("Enter An Element: "))
    my_set.append(x)
    i += 1

print(powerSet(my_set))
print(len(powerSet(my_set)))