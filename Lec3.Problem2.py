# Problem 2A
### print the following:
#print 2
#print 4
#print 6
#print 8
#print 10
#print Goodbye!

num = 2 
while num < 11:
    print num
    num +=2
print "Goodbye!"

###########################
# Problem 2B
#print Hello!
#print 10
#print 8
#print 6
#print 4
#print 2

num = 10 
print "Hello!"
while num > 0:
    print num
    num -=2

#####################
# Problem 2C
# Print the total sums of numbers from num to end 


num = 0
# end = 6 or whatever #they already definded 
while end > 0:
    num = end + num
    end -= 1
print num