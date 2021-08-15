str_1 = "hi, let us code."
str_2 = "Python Is Easy Language To Code."
str_3 = "Python"
str_4 = "coding\tis\tfun"
str_5 = "Python254"
str_6 = "89076"
mylist = ["Python", "is", "coding", "language"]
str_7 = "       apple       "
# capitalize and lowercase the first word
a = str_1.capitalize()
print(a)
b = str_2.casefold()
print(b)
# centers
x = str_3.center(20, '*')
print(x)
# counts
x = str_1.count("code")
print(x)
# checking for endwith or startwith
y = str_2.endswith("code.", 3, 15)
print(y)
x = str_5.startswith("pt")
print(x)
# tab expansion
print(str_4.expandtabs(2))
# finds the first occurance of substring
res1 = str_2.index("Easy")
print(res1)
res2 = str_1.find("python")
print(res2)
# adds the required string later
print("My name is {} and my age is {age}".format("Jhon", age=25))
# is function which returns the boolean character
print(str_5.isalnum())
print(str_3.isalpha())
print(str_6.isdigit())
print(str_6.isdecimal())
print(str_1.islower())
print(str_4.isprintable())
print(str_2.isspace())
print(str_2.istitle())
print(str_1.isupper())
# joins all the element of list into string
m = " ".join(mylist)
print(m)
# returns a justified version of string
lj = str_3.ljust(10)
print(lj, " is simple")
rj = str_3.rjust(10)
print(rj, "is simple")
# makes all character upper and lower
print(str_3.lower())
print(str_3.upper())
# removes the left or right spacing
x = str_7.lstrip()
print("Doctor advices to take ", x, " a day")
y = str_7.rstrip()
print("Doctor advices to take ", y, " a day")
# swapes the character
print(str_2.swapcase())
# converts first letter of each word to caps
print(str_1.title())
