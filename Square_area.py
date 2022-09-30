# python program to find the area of Square

a=8
b=8
c=4
d=4

#Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
# d = float(input('Enter fourt side: '))

# calculate the semi-perimeter
s = (a + b + c + d) / 2

#calculate the area
area = (s*(s-a)*(s-b)*(s-c)*(s-d)) ** 0.2
print('The area of the Square is % 0.5f' %area)