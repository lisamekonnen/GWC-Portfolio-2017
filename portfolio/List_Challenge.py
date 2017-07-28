
from random import *


### Create 5 Syllable Line
word_list1 = ['Lisa is so cool, Diet Coke Is Yum', 'La la la la la']

### Create 7 Syllable Line
word_list2 =['Everyone should love Lisa','It is better than cola', 'do do do do do']


#Generates a random integer.
x = randint(0, len(word_list1)-1)
y= randint(0, len(word_list2)-1)


### Prints Name
haiku=word_list1[x]+ " \n"+word_list2[y]+ " \n"+word_list1[x]

print(haiku)
