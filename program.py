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
