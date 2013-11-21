# Enter your answrs for chapter 6 here
# Name: Steve Blank


# Ex. 6.6.1
# Type these functions into a file named palindrome and test them out.  What happens if you call middle with a string with two letters?  One letter?  What about the empty string, which is written '' and contains no letters?

def first(word):
	return word[0]
def last(word):
	return word[-1]
def middle(word):
	return word[1:-1]

print first('helicopter')	#ans: h
print last('helicopter')	#ans: r
print middle('helicopter')	#ans: elicopte

print middle('it')			#ans: nothing, zero, zilch, nada, ""
print middle('a')			#ans: crickets (as-in-nothing)
print middle('')			#ans: more nothing. blank space, like my last name.

# Ex. 6.6.2
# Write a function called is_palindrome that takes a string argument and returns True if it is apalindrome and False otherwise.  Remember that you can use the built-in function len to check the length of a string.

def is_palindrome(word):
	if len(word) >= 3:
		if first(word) == last(word):
			return is_palindrome(middle(word))
		else:
			return False

	if len(word) < 3:
		if first(word) == last(word):
			return True
		else:
			return False

print is_palindrome("uyyu")
print is_palindrome("nope")
print is_palindrome("redivider")
print is_palindrome("resdfasdlfkjder")


# Ex 6.8
# The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
# One way to find the GCD of two numbers is Euclid's algorithm, which is based on the observation that if r is the remainder when a is divided by b, then gcd(a,b) = gcd(b,r). As a base, we can use gcd(a,0) = a.

# Write a function called gcd that takes parameters a and b and returns their greatest common divisor. 

def gcd(a,b):
	if b == 0:
		return a
	else:
		r = a % b
		return gcd(b,r)

print gcd(105,60)
print gcd(10,9)