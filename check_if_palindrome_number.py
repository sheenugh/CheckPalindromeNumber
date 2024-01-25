
# ----- FUNCTIONS -----
def if_palindrome(string_num):
    checking = string_num[::-1]
    if string_num == checking:
        return True
    else:
        return False

# >>>>>>>>>> PSEUDO CODE <<<<<<<<<<
# ----- ACTUAL CODES -----
# - String given number
given_number1 = "121"
given_number2 = "125"

# - This section is for the variable 'result' and printing the result
print("The original number is", given_number1 + ".")
print("In addition, the original number is", given_number2 + ".")








# - Caller of the def function/s
result1 = if_palindrome(given_number1)
print("Thus, the given number " + given_number1 + " is a palindrome number.")

result2 = if_palindrome(given_number2)
print("Thus, the given number " + given_number2 + " is a palindrome number.")