### The Start of the Story
start = '''
You left your baby brother in the library after you went to the bathroom. When you come back, your brother is gone!
You make a list of places where your brother could be.
A piece of paper is in your hand: "Post Office, Hospital, and Home"
You have to decide which one to go to first...
'''
def otherwise():
    print('Invalid input (you lose)')

print(start)

### First Conditional: Post Office
place = input('Enter the place you want to go to:')
if place == "Post Office":
    print('Now you wil be going to Post Office.')
    place = input('You look all over the Post Office you even search in the mail boxes and still no sign of your brother! You check the other two places that your brother could be: Hospital or Home. Pick either the Hospital or Home:')
        ### If You Go To Hospital
    if place == 'Hospital':
        print('Now you will be going to the Hospital')
        decision=input('You look all over the Hospital and you cannot find your brother! You have to make a decision either go home and tell your mom or call the police:')
        if decision == "go home and tell mom":
            print ('You will go home and tell your mom and you are grounded for 6 months (you lose).')
        elif decision == "call the police":
            print ('You call the police and they find your brother and you hope they do not tell your parents (you win).')
        else:
            otherwise()
    ### If You Go Home
    elif place == "Home":
        print('Now you will be going Home')
        print ('Your mom found out that you lost your younger brother so now you are grounded (you lose)')
    else:
        otherwise()


### Second Conditional: Hospital
elif place == "Hospital":
    print('Now you will be going to the Hospital')
    place = input('You look all over the Hospital and you cannot find your brother! Should you go to the Post Office or Home?:')
        ###If You Go To The Post Office
    if place == "Post Office":
        print('Now you wil be going to Post Office.')
        decision=input('You look all over the Post Office you even search in the mail boxes and still no sign of your brother! You have to make a deicison either go home or call the police?:')
        if decision == "go home and tell mom":
            print('Now you will be going Home')
            print ('You told your mom that you lost your younger brother so now you are grounded (you lose)')
        elif decision == "call the police":
            print ('You call the police and they find your brother and you hope they do not tell your parents (you win).')
        else:
            otherwise()
        ### If You Go Home
    elif place == "Home":
        print('Now you will be going Home')
        print ('Your mom found out that you lost your younger brother so now you are grounded (you lose)')
    else:
        otherwise()



### Third Conditional: Home
elif place == "Home":
        print('Now you will be going Home')
        print ('Your mom found out that you lost your younger brother so now you are grounded (you lose)')
else:
        print('Invalid input (you lose)')
