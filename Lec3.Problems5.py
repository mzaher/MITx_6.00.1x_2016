# L3 PROBLEM 5A
# print 2
# print 4
# print 6
# print 8
# print 10
# print "Goodbye!"
for count in range(11):
    if count != 0 and count % 2 == 0:
        print count
print "Goodbye!"

# L3 PROBLEM 5B
# print "Hello!"
# print 10
# print 8
# print 6
# print 4
# print 2

print "Hello!"
for num in range(0, 10, 2):
    print 10 - num

# L3 PROBLEM 5C
# 3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

total = end
for next in range(end):
    total += next
print total
