def robinKarpsearch(text, pattern):
    """
    Find All Occurences Of Pattern In Text Using Robin-Karp Algorithm
    Args:
        Text: The Text String To Search In
        Pattern: The Pattern String To Find
    Returns:
        List Of Indices Where Pattern Is Found
    """
    size = len(text)
    pat = len(pattern)
    matches = []

    # Chose A Prime Number For Hashing
    # Larger Prime: Fewer Hash Collisons
    prime = 101
    base = 256   # We Can Use 256 For All ASCII Characters 
    mod = 10**9 + 7   # Large Prime To Prevent Overflow
    
    # Step-1: Calculate The Highest Power Needed
    # For Pattern "ABC" with pat = 3: Base^(pat-1) = 256^2
    # We Will Use This To Remove The First Character
    h = 1
    for i in range(pat-1):
        h = (h*base) % mod

    # Step-2: Compute Hash Of Pattern And First Window Of Text
    pattern_hash = 0
    window_hash = 0

    # Calculate Hash For Pattern
    for i in range(pat):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
    # Calculate Window For First Window Of Text
    for i in range(pat):
        window_hash = (base * window_hash + ord(pattern[i])) % mod

    # Step-3: Glide The Window Through Text
    for i in range(size - pat + 1):
        # Check If Hashes Match
        if pattern_hash == window_hash:
            # Hash Collision Possible, Verify Actual Strings
            if text[i:i+pat] == pattern:
                matches.append(i)
                print(f"Match Found At Index, {i}")

        # Step 4 And 5: Calculate Hash For Next Window Using Rolling Hash
        if i < size - pat:
            # Remove First Characters Of Current Window And Add New Character
            # Formula: new_hash == (old_hash - first_char * h) * base + new_char
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + pat])) % mod

            # Handle Negative Values(Modulo Of Negative Number)
            if window_hash < 0:
                window_hash += mod

    return matches

text = "ABABDACACDABABCABAB"
pattern = "ABAB"
print(f"Seacrching For '{pattern}' In '{text}'")
res = robinKarpsearch(text, pattern)
print(f"Matches At Positions: {res}\n")