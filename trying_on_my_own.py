def if_palindrome(var = "121"):
    checking = var[::-1]
    if var == checking:
        return True
    else:
        return False

result = if_palindrome()
print(result)


# s = str(121)

# result = s[::-1]
# if (s == result):
#     print ("yes")
# else:
#     print("no")