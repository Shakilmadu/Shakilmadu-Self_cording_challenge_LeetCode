# // https://leetcode.com/merge-strings-alternately/description/
def merge_alternately(word1: str, word2: str) -> str:
    merged_string = []
    i, j = 0, 0

    # Add letters
    while i < len(word1) and j < len(word2):
        merged_string.append(word1[i])
        merged_string.append(word2[j])
        i += 1
        j += 1

    # Append remaining letters from word1 if any
    if i < len(word1):
        merged_string.append(word1[i:])

    # Append remaining letters from word2 if any
    if j < len(word2):
        merged_string.append(word2[j:])

    # Join the list into a string and return
    return ''.join(merged_string)


# Example usage:
word1 = "abc"
word2 = "pqr"
result = merge_alternately(word1, word2)
print(result)
