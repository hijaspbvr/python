str1=input("Enter the string:")
str2=input("Enter the second string:")
new_a=str2[:1]+str1[1:]
new_b=str1[:1]+str2[1:]
print("The new string after swapping first two charaters of both string:",(new_a+''+new_b))
