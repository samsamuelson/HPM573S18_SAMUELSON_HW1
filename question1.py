x = 17
print('Setting x =', x)

# integer
y1 = x
print('y1 is a ' , type(y1))


# float
y2 = float(x)
print('y2 is a ' , type(y2))

# string
y3 = str(x)
print('y3 is a ' , type(y3))

# Boolean, '17 < 18'
y4 = bool(x < 18)
print('y4 is a ' , type(y4))
print(y4)

text = 'The value of x is ' + repr(y1)
print(text)
