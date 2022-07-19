
#Solve the following problem:
#In comments Provide the Time Complexity of your solution.
#Your mission is to solve this problem in O(n) time or better

#A phrase is a  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return truefalse.
 
a = "A man, a plan, a canal: Panama"
print(a)
print(True)
#"amanaplanacanalpanama" is a palindrome.

b = "race a car"
print(b)
print(False)
#"raceacar" is not a palindrome.

c = " "
print(c)
print(True)
#s is an empty string "" after removing non-alphanumeric characters.
#Since an empty string reads the same forward and backward, it is a palindrome.

def palindromes(s):
    x = ''.join(filter(str.isalnum, s)).lower()
    return x == x[::-1]
    

print(palindromes(a))

#O(n) This is only 1 loop through the fucttion is being done.