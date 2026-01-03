def brackets(num):
    def backtrack(current_string, openBracket, closeBracket):
        if len(current_string) == 2 * num:
            result.append(current_string)
            return
        
        if openBracket < num:
            backtrack(current_string + "(", openBracket + 1, closeBracket)
        
        if closeBracket < openBracket:
            backtrack(current_string + ")", openBracket, closeBracket + 1)

    result = []
    backtrack("", 0, 0)
    return result
    
def print_parentheses(n):
    """
    Print all balanced parentheses combinations for n pairs.
    
    Args:
        n (int): Number of pairs of parentheses
    """
    combinations = brackets(n)
    
    print(f"All balanced parentheses for {n} pair(s):")
    print("-" * 40)
    
    for i, combo in enumerate(combinations, 1):
        print(f"{i:2}. {combo}")
    
    print("-" * 40)
    print(f"Total combinations: {len(combinations)}")

# Example usage

# Test with different values of n
for n in range(1, 5):
    print_parentheses(n)
    print()