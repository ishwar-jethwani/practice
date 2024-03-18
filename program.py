# Question 1
# Write a function to reverse a given string. For example, if the input is "hello", the output should be "olleh". # noqa

# Normal Function:
def reverse_string(string):
    return string[::-1]


# function calling
print(reverse_string("hello"))


# Lambda Function:
reverse_lambda_str = lambda s: s[::-1] # noqa


# function calling using lambda
print(reverse_lambda_str("hello"))


# Write a function to check if a given string is a palindrome. For example, "radar" is a palindrome. # noqa
def is_palindrome(word) -> bool:
    """Return True if word is a palindrome"""
    return word == word[::-1]


print(is_palindrome("naman"))

# as a lambda expression
is_palindrome_lambda = lambda w: w == w[::-1] # noqa
print(is_palindrome_lambda("madam"))


# Write a function to count the number of vowels and consonants in a given string. For example, in the string "hello", there are 2 vowels and 3 consonants. # noqa
def count_vowels(string):
    vowels = "aeiou"
    count = {}
    for char in string:
        if char.lower() in vowels:
            if char.lower() in count.keys():
                count[char] += 1
            else:
                count[char] = 1
    return count


print(count_vowels("Hello World!"))

#  Write a function to check if two strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. # noqa
# "listen" - "silent"
# "triangle" - "integral"
# "astronomer" - "moonstarer"
# "schoolmaster" - "the classroom"
# "debit card" - "bad credit"
# "funeral" - "real fun"
# "astronomers" - "moon starers"
# "dormitory" - "dirty room"
# "eleven plus two" - "twelve plus one"
# "conversation" - "voices rant on"


def check_anagrams(str1, str2):
    """Check if two strings are anagram of each other."""
    return sorted(str1) == sorted(str2)


print(check_anagrams("listen", "silent"))
print(check_anagrams("triangle", "new"))

# Write a function to perform basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string would not become smaller than the original string, your function should return the original string. # noqa

def compress_string(s):
    compressed = ""
    count = 1

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1

    return compressed if len(compressed) < len(s) else s

# Example usage:
original_string = "aabcccccaaa"
compressed_string = compress_string(original_string)
print("Compressed string:", compressed_string)

# Write a function to check if one string is a rotation of another. For example, "abcd" is a rotation of "cdab" but not of "bcda".


def is_rotation(s1, s2):
    """Check if two strings are rotations of each other."""
    rotation = s1*2
    if s2 in rotation:
        return True
    else:
        return False


print(is_rotation("abcd", "cdab"))
print(is_rotation("abcd", "bcda"))


def longest_substring_without_repeating(s):
    # Dictionary to store the index of the last occurrence of each character
    last_seen = {}
    start = 0
    max_length = 0

    for end, char in enumerate(s):
        # If the character is already in the dictionary and its index is after the start of the current substring # noqa
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1

        # Update the last seen index of the character
        last_seen[char] = end

        # Calculate the length of the current substring
        current_length = end - start + 1

        # Update the maximum length if needed
        max_length = max(max_length, current_length)

    return max_length

# Example usage:


input_str = "abcabcbb"
print("Length of the longest substring without repeating characters:", longest_substring_without_repeating(input_str)) # noqa


def rotation(a, b):
    c = ""
    if b < len(a):
        c += a[:b]
    elif b > len(a):
        remainer = b % len(a)
        repetation = b // len(a) 
        c += a * repetation + a[:remainer]
    print(c)


string = "abcd"
target = 3
rotation(string, target)

a = [10,5,4,5,8,4,7,6]
max = float("-inf")
second_max = float("-inf")
third_max = float("-inf")
fourth_max = float("-inf")
for i in a:
    if i > max:
        fourth_max = third_max
        third_max = second_max
        second_max = max
        max = i
    elif second_max != max and i > second_max:
        second_max = i
    elif third_max != second_max and i > third_max:
        third_max = i
    elif fourth_max != third_max and i > fourth_max:
        fourth_max = i

print(max, second_max, third_max, fourth_max)


    