def if_palindrome(var):
    checking = var[::-1]
    if var == checking:
        return True
    else:
        return False

result = if_palindrome("121")
print(result)

result2 = if_palindrome("234")
print(result2)


# s = str(121)

# result = s[::-1]
# if (s == result):
#     print ("yes")
# else:
#     print("no")