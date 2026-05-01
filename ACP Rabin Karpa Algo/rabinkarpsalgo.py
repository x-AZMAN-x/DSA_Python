def robinKarpsearch(text, pattern):
    size = len(text)
    pat = len(pattern)
    matches = []

    prime = 101
    base = 256
    mod = 10**9 + 7

    h = 1
    for i in range(pat-1):
        h = (h*base) % mod

    pattern_hash = 0
    window_hash = 0

    for i in range(pat):
            pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
    for i in range(pat):
            window_hash = (base * window_hash + ord(pattern[i])) % mod

    for i in range(size - pat + 1):
            if pattern_hash == window_hash:
                if text[i:i+pat] == pattern:
                    matches.append(i)
                    print(f"Match Found At Index, {i}")

            if i < size - pat:
                window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + pat])) % mod

                if window_hash < 0:
                    window_hash += mod

    return matches

text = "ABABDACACDABABCABAB"
pattern = "ABAB"
print(f"Seacrching For '{pattern}' In '{text}'")
res = robinKarpsearch(text, pattern)
print(f"Matches At Positions: {res}\n")