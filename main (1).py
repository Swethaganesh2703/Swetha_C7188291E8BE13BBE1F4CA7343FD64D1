#write a program that determines whether a year entered by the user is a leap year or not using ifelif-else Statements

#get the year from the user
year = int(input("Enter the year:"))

#check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")
