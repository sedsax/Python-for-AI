def longest_unique_substring(s):
    index_map = {}
    max_length = 0
    left = 0
    max_substring = ""

    for right, char in enumerate(s):
        if char in index_map and index_map[char] >= left:
            left = index_map[char] + 1
        index_map[char] = right

        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            max_substring = s[left:right + 1]

    return f"{max_substring} - {max_length}"

# Test
print(longest_unique_substring("abcabcbb"))  # abc - 3
print(longest_unique_substring("bbbbb"))    # b - 1
print(longest_unique_substring("pwwkew"))   # wke - 3
print(longest_unique_substring(" "))        #   - 1
print(longest_unique_substring("au"))       # au - 2
print(longest_unique_substring("aab"))      # ab - 2
print(longest_unique_substring("dvdf"))     # vdf - 3
print(longest_unique_substring("abba"))     # ab - 2
print(longest_unique_substring("abcde"))    # abcde - 5
print(longest_unique_substring("abcda"))    # bcda - 4
print(longest_unique_substring("abac"))     # bac - 3
