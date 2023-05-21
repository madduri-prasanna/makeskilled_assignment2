a = input("Enter the string: ")
b = input("Enter the string: ")
c = input("Enter the string: ")
#checking whether above words are palindrome or not
if(a == a[::-1]):
print(f"{a} is palindrome")
else:
print(f"{a} is not palindrome")
if(b == b[::-1]):
    print(f"{b} is palindrome")
else:
    print(f"{b} is not palindrome")
    if(c == c[::-1]):
        print(f"{c} is palindrome")
    else:
        print(f"{c} is not palindrome")
        

