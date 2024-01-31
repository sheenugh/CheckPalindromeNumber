
# ----- FUNCTIONS -----
def if_palindrome(string_num):
    checking = string_num[::-1]
    if string_num == checking:
        print("The given number", string_num, "is a palindrome number.")
        return 
    else:
        print("The given number", string_num, "is not a palindrome number.")
        return 

# >>>>>>>>>> PSEUDO CODE <<<<<<<<<<
# ----- ACTUAL CODES -----
# - String given number
given_number1 = "121"
given_number2 = "125"

# - This section is for the variable 'result' and printing a str, especially the result
print("The original number is", given_number1 + ".")
result1 = if_palindrome(given_number1)

print("\n")
print("In addition, the original number is", given_number2 + ".")   
result2 = if_palindrome(given_number2)









# - Caller of the def function/s

