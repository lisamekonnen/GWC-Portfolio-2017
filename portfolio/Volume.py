### Ask The Person What They Want For Measurements
print('Hello we can calculate any volume just give me the length, width, and height.')

length= int(input('Put the value you want as length is:'))
width=int(input('Put the value you want as width is:'))
height=int(input('Put the value you want as height is:'))
### My List of Volume
Volume=[length,width,height]

### How To Find Volume
Answer=Volume[0]*Volume[1]*Volume[2]

print('The volume of this object is:')
print(Answer)
