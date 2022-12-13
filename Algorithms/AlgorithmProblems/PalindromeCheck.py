def palindrome_check_founding_the_reverse(input_string):
    reversed_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string = reversed_string + input_string[i]
    if reversed_string == input_string:
        return True
    else:
        return False


def palindrome_check(input_string):
    for i in range(len(input_string) // 2):
        if not input_string[i] == input_string[len(input_string)-i-1]:
            return False
    return True
def palindrome_check_recursive(input_string,i=0):
    j=len(input_string)-i-1
    return True if i>=j else input_string[j]==input_string[i] and palindrome_check_recursive(input_string,i+1)

string1 = "abbfbnfbba"
print(palindrome_check(string1))
print(palindrome_check_founding_the_reverse(string1))
print(palindrome_check_recursive(string1))
