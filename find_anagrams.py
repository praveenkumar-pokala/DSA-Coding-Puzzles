def find_anagrams(word_list):
    anagrams = {}

    for word in word_list:
        # Sort the word and use it as a key
        key = ''.join(sorted(word))

        # Append the word to the list of anagrams for the key
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]

    # Return only the lists that have more than one anagram
    return {key: words for key, words in anagrams.items() if len(words) > 1}

# Example usage
words = ["listen", "silent", "enlist", "hello", "world", "dell", "led", "ell"]
anagrams = find_anagrams(words)

# Print the anagrams found
for key, words in anagrams.items():
    print(f"Anagrams for '{key}': {words}")
