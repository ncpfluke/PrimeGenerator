import math
import time


x = 1
primes = [2] #the way the program is written, it will not display 2 as prime, so we have to manually put it in
print(2)

def display():
# displays the value of x, if its prime (1=prime)
    print(x)
    primes.append(x) # if x is prime, it adds it to an array of primes
    #time.sleep(0.5)
    return




def testprime():
#tests whether x is prime or not and sends 1 for prime and 0 for not prime to the display function
    global x
    x += 2 #adds 2 to x, this way it only tests odd numbers, bc even numbers arent prime(except 2) (makes the program more efficient)


    val = 0 # val is the index value of a prime number in the primes array that is closest to the sqrt(x) without being less than sqrt(x)
    prime = 1

    for h in range(len(primes)):
    #this loop looks for the ideal value of val
        if primes[h] >= math.ceil(math.sqrt(x)):
            val = h
            break

    for i in range(val + 1):# this checks all prime numbers between 2 and val to see if x is divisible by any of them (proving its prime or not )
        if x % primes[i] == 0:
            prime = 0 #if x fails the prime test, then it gets told its not prime :p

    # comment this to make the program Test numbers every so often(depending on the value above, 500 = 1 / 2 second),
    # instead of DISPLAYING a number every half a second(less pleasing visually)

    if prime == 1:
        display()  # tells the prime function whether or not to display the current x value and add it to the known list of primes

    return



count = 109 # this number sets the maximum number you would like to test, it will test every number form 0 to count, feel free to change it

for count in range(int((count-1)/2)):
    testprime()
