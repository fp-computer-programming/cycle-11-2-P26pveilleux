def is_palindrome(input_string): 
    clean_string = ''.join(input_string.spilt()).lower()
    return clean_string == clean_string[::-1]
name = 0 

if name ==0:
    test_input = input("word")

if is_palindrome(test_input):
    print("palindrome")
else:
    print("not palindrome")
