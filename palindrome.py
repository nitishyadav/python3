#python program for palindrome
'''
print("enter a string")
s = input()
rev_s = reversed(s)
if list(rev_s)== list(s):
    print("string is palindrome")
else:
    print("String Not Palindrome")

 '''

#Another method to do the same 
def reverse(s):
    return s[::-1]
    
def isPalindrome(s):
    rev =reverse(s)
    
    if(rev == s):
        return True
    return False
    
s =input("enter a string:")
print(s[::-1])

result = isPalindrome(s)
if result ==1:
    print("Plaindrome")
else:
    print("Not Palindrome")