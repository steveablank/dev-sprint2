# Enter your answrs for chapter 7 here
# Name: Steve Blank


# Ex. 7.5
import math

def factorial(n):		#Computers factorial of n
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

def estimate_pi():		#Computes an estimate of pi
	total = 0
	k = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		num = factorial(4*k) * (1103 + 26390*k)
		den = factorial(k)**4 * 396**(4*k)
		term = factor * num / den
		total += term

		if abs(term) < 1e-15: break
		k += 1

	return 1 / total

print estimate_pi()
print math.pi


# How many iterations does it take to converge?
# 4