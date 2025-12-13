num=int(input("enter num:"))
original=num
reverse=0
while num>0:
 digit=num%10
 reverse=reverse*10+digit
 num=num//10
if original==reverse:
   print("number is palindrome")
else:
  print("number not palindrome")