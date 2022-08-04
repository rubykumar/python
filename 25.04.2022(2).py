num=(input("Enter the number"))
i=0
for i in range(len(num)):
   if num[i]!=num[-1-i]:
        print(num,'It is not a palindrome')
        break
   else:
       print(num,'It is palindrome')
       break
