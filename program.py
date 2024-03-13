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
