def keypadCombinations(pressed_keys, currentCombination = "", index = 0, results = None):
    keypad = {
        '2' : ["a", "b", "c"],
        '3' : ["d", "e", "f"],
        '4' : ["g", "h", "i"],
        '5' : ["j", "k", "l"],
        '6' : ["m", "n", "o"],
        '7' : ["p", "q", "r", "s"],
        '8' : ["t", "u", "v"],
        '9' : ["w", "x", "y", "z"],
    }

    if results is None:
        results = []

    if index == len(pressed_keys):
        if currentCombination:
            results.append(currentCombination)
        return results
    
    current_digit = pressed_keys[index]

    for letter in keypad.get(current_digit, []):
        keypadCombinations(pressed_keys, currentCombination + letter, index + 1, results)

    return results

pressed_keys = input()
combinations = keypadCombinations(pressed_keys)
print(combinations)
print(f"Total Count Of The Possible Combinations = {len(combinations)}.")