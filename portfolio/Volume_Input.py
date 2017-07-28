### Ask The Person What They Want For Measurements
print('Hello we can calculate any volume just give me the length, width, and height.')

### Ask the User What They Want the Value of Length, Width, and Height
length= int(input('Put the value you want as length is:'))
width=int(input('Put the value you want as width is:'))
height=int(input('Put the value you want as height is:'))

### My List for Volume
Volume=[length,width,height]

### Equation of Volume Using Index of List
Answer=Volume[0]*Volume[1]*Volume[2]

### What The User Sees
print('The volume of this object is:')
print(Answer)
