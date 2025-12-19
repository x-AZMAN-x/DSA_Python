def powerSetForLetters(my_set):
    letter = len(my_set)
    power_set_size = 1 << letter

    print("Power Set: ")
    power_set = []
    for counter in range(power_set_size):
        subset = []
        for j in range(letter):
            if counter & (1 << j):
                subset.append(my_set[j])
        power_set.append(subset)
    return power_set

my_set = ["a", "b", "c", "d"]
print(powerSetForLetters(my_set))
print(len(powerSetForLetters(my_set)))