#for adding the required classes 0:sitting and 1:walking
import fileinput
for line in fileinput.input('sitting_large.txt', inplace=1):
    print ('{0}{1}{2}'.format('', line.rstrip('\n'), ',0'))
